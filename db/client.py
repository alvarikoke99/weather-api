import redis, os

try:
    redis_client = redis.Redis(
        host=os.getenv("REDIS_HOST", "localhost"), 
        port=os.getenv("REDIS_PORT", 6379), 
        decode_responses=True
        )
except:
    print("ERROR connecting to Redis DB")
print(os.getenv("REDIS_HOST", "localhost"))