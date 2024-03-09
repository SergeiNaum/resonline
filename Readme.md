
# Test task for the position of middle python backend developer from resoline company

## Quick start

##### Download image from docker hub

---
```
docker pull sergeynaum/resoline:latest
```
---
##### Start the microservice by executing the command where app={nunber} number of application replications
```
docker-compose up --scale api=2
```
---
##### CONGRATULATIONS THE CONTAINER IS UP AND RUNNING AND THE API IS READY FOR TESTING_🚀

---
### Available methods for API requestsAvailable methods for API requests

To verify the initial inspection by GET method:
return:
    "message": "Connected to Redis database {num}"  
    [key: value]

```
curl http://0.0.0.0:8000/
```

SET value entry in redis by POST method if not Query Params ttl is passed ttl=infinity

```
curl -X POST -H "Content-Type: application/json" -d '{"values": [144, 120, 500]}' http://0.0.0.0:8000/values
```


SET value entry in redis by POST method if Query Params ttl is passed ?ttl=5 - data lifetime in redis

```
curl -X POST -H "Content-Type: application/json" -d '{"values": [144, 120, 500]}' http://0.0.0.0:8000/values?ttl=5
```


The query should return a list of all values on the server for which prime_factor is a multiplier. If prime_factor is not prime, it will return an empty response.  
http://127.0.0.1:8000/values/{int: number}

```
curl http://0.0.0.0:8000/values/5
```

To stop the microservice, execute the command

```
make docker-compose_down
```
