import redis

from app.core.config import settings


class RedisConnector:
    def __init__(self):
        host=settings.REDIS_HOST
        port=settings.REDIS_PORT
        db=int(settings.REDIS_DATABASE)
        self.pool = redis.ConnectionPool(host=host, port=port, db=db)
    
    def ping(self):
        with redis.Redis(connection_pool=self.pool) as redis_conn:
            return redis_conn.ping()

    def read(self, key):
        with redis.Redis(connection_pool=self.pool) as redis_conn:
            return redis_conn.get(key)

    def write(self, key, value):
        with redis.Redis(connection_pool=self.pool) as redis_conn:
            redis_conn.set(key, value)

    def multi_get(self, keys):
        with redis.Redis(connection_pool=self.pool) as redis_conn:
            return redis_conn.mget(keys)

    def multi_set(self, items):
        with redis.Redis(connection_pool=self.pool) as redis_conn:
            redis_conn.mset(items)

redis_conn = RedisConnector()