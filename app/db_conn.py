import redis

from app.config import REDIS_HOST, REDIS_PORT


def get_free_db():
    redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
    lock = redis_client.lock("redis_db_lock", blocking_timeout=10)
    try:
        lock.acquire()
        for db_num in range(1, 4):
            exists = redis_client.exists(f"redis_db_{db_num}")
            if not exists:
                redis_client.set(f"redis_db_{db_num}", "1")
                return db_num
        else:
            raise Exception("Can't connect to Redis database, maximum limit reached.")
    finally:
        lock.release()
        redis_client.close()
