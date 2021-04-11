import asyncio
import zmq
from zmq.asyncio import Context

context = Context()


async def do_receiver():
    receiver = context.socket(zmq.PULL)
    receiver.connect("tcp://localhost:5557")
    while message := await receiver.recv():
        print(f'Via PULL: {message}')


async def do_subscriber():
    subscriber = context.socket(zmq.SUB)
    subscriber.connect("tcp://localhost:5556")
    subscriber.set(zmq.SUBSCRIBE, '')
    while message := await subscriber.recv():
        print(f'Via SUB: {message}')


async def main():
    await asyncio.gather(
        do_receiver(),
        do_subscriber(),
    )

if __name__ == "__main__":
    asyncio.run(main())