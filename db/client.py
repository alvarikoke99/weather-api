import redis, os

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"), 
    port=os.getenv("REDIS_HOST", 6379), 
    decode_responses=True
    )