# docker run -d --name redis-weather-api -p 6379:6379 redis
FROM redis:latest

EXPOSE 6379

CMD ["redis-server"]