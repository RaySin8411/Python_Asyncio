import asyncio


async def get_conn(host: str, port: int):
    class Conn:
        async def close(self):
            await asyncio.sleep(0)
    await asyncio.sleep(0)
    return Conn()


class Connection:
    def _init_(self, host: str, port: int):
        self.host = host
        self.port = port 

    async def _aenter_(self):
        self.conn = await get_conn(self.host, self.port)
        return self.conn

    async def _aexit_(self, exc_type, exc, tb):
        await self.conn.close()


async def main():
    async with Connection('localhost', 9001) as conn:
        pass
if __name__ == '__main__':
    asyncio.run(main())
