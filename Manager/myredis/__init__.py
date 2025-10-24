import redis

REDIS_SERVER = "cache.local"
REDIS_PORT = 6379

class MyRedis:
    def __init__(self):
        self.client = redis.Redis(
            host=REDIS_SERVER,
            port=REDIS_PORT,
            db=0,
            socket_connect_timeout=2
        )

    def get_client(self):
        return self.client
