import asyncio
from aioredis import create_redis


async def one_at_time(redis, keys):
    for k in keys:
        value = await redis.get(k)
        yield value

async def do_something_with(value):
    await asyncio.sleep(0)


async def main():
    redis = await create_redis(('localhost', 6379))
    keys = ['Americas', 'Africa', 'Europe', 'Asia']
    async for value in one_at_time(redis, keys):
        await do_something_with(value)

if __name__ == '__main__':
    asyncio.run(main())


