import redis

REDIS_SERVER = "cache.local"
REDIS_PORT = 6379

class MyRedis:
    class ConnectionError(redis.ConnectionError):
        pass

    def __init__(self):
        self.client = redis.Redis(
            host=REDIS_SERVER,
            port=REDIS_PORT,
            db=0,
            socket_connect_timeout=2
        )

    def get_client(self):
        return self.client
    
    def ping(self):
        try:
            return self.get_client().ping()
        except redis.ConnectionError:
            return False

    def getKey( self , key ):
        try:
            value = self.client.get(key)
            print(f"Key: {key} Value: {value}")
            return value.decode('utf-8') if value else None
        except:
            return None

    def keys( self , type = "*" ):
        try:
            return self.client.keys( type )
        except:
            return []

