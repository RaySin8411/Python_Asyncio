import argparse
import asyncio
from random import randint, uniform
from datetime import datetime
from datetime import timezone
from contextlib import suppress
import zmq
import zmq.asyncio
import psutil

ctx = zmq.asyncio.Context()


async def starts_reporter(color: str):
    p = psutil.Process()
    sock = ctx.socket(zmq.PUB)
    sock.setsockopt(zmq.LINGER, 1)
    sock.connect('tcp://localhost:5555')
    with suppress(asyncio.CancelledError):
        while True:
            await sock.send(data=dict(
                color=color,
                timestamp=datetime.now(tz=timezone.utc).isoformat(),
                cpu=p.cpu_percent(),
                mem=p.memory_full_info().rss / 1024 / 1024
            ))
            await asyncio.sleep(1)

    sock.close()


async def main(args):
    asyncio.create_task(starts_reporter(args.color))
    leak = []
    with suppress(asyncio.CancelledError):
        while True:
            sum(range(randint(1000, 10000000)))
            await asyncio.sleep(uniform(0, 1))
            leak += [0] * args.leak


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--color', type=str)
    parser.add_argument('--leak', type=int, default=0)
    args = parser.parse_args()
    try:
        asyncio.run(main(args))
    except KeyboardInterrupt:
        print('Leaving...')
        ctx.term()
