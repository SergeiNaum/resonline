import redis
from typing import List

from fastapi import FastAPI, Query

from app.chemas import CreateValuesRequest, CalculatedValueEntity
from app.db_conn import get_free_db
from app.utils import get_prime_factors, is_prime
from app.config import REDIS_HOST, REDIS_PORT, REDIS_CLIENT, REDIS_DB  # noqa: F401


app = FastAPI()


@app.on_event("startup")
def startup_event():
    global REDIS_DB, REDIS_CLIENT
    app.state.redis = None

    try:
        if REDIS_DB is None:
            REDIS_DB = get_free_db()
            REDIS_CLIENT = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

            app.state.redis = REDIS_CLIENT

    except Exception as e:
        print(f"Error: {str(e)}")


@app.post("/values", response_model=List[CalculatedValueEntity])
async def set_values(values: CreateValuesRequest, ttl: int = Query(default=None)):
    result = []

    for value in values.values:

        prime_factors = get_prime_factors(value)
        key = int(value)

        if app.state.redis:
            app_redis = app.state.redis
            value_exists = app_redis.exists(key)
            if not value_exists:
                app.state.redis.set(key, ",".join(map(str, prime_factors)), ex=ttl)

        result.append({"value": value, "prime_factors": prime_factors})

    return result


@app.get("/values/{prime_factor:int}", response_model=List[CalculatedValueEntity])
async def get_values(prime_factor: int):

    result = []

    if not is_prime(prime_factor):
        return []

    if app.state.redis:
        app_redis = app.state.redis

        for key in app_redis.keys():

            prime_factors = list(
                map(int, app_redis.get(key).decode("utf-8").split(","))
            )

            if prime_factor in prime_factors:
                value = int(key)
                result.append({"value": value, "prime_factors": prime_factors})

        return result


@app.get("/")
async def root():

    if app.state.redis:
        app_redis = app.state.redis
        all_keys = app_redis.keys()

        d = {}
        if all_keys:
            for key in all_keys:
                value = app_redis.get(key)
                d[int(key)] = value

        return {"message": f"Connected to Redis database {REDIS_DB}"}, d
    else:
        return {"message": "Redis connection is not established[MAX_LIMIT]."}
