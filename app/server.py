import asyncio
import datetime
import random
from typing import Dict
from logger import get_logger

logger = get_logger("server")

clients: Dict[int, asyncio.StreamWriter] = {}
response_counter: int = 0


async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    global response_counter
    client_id: int = len(clients) + 1
    clients[client_id] = writer
    addr: str = writer.get_extra_info('peername')

    while True:
        data: bytes = await reader.readline()
        if not data:
            break
        request: str = data.decode().strip()
        request_date: str = datetime.datetime.now().strftime('%Y-%m-%d')
        request_time: str = datetime.datetime.now().strftime('%H:%M:%S.%f')[:-3]
        if random.random() < 0.1:
            logger.info(f'{request_date};{request_time};{request};(проигнорировано)')
        else:
            await asyncio.sleep(random.uniform(0.1, 1))
            response: str = f"[{response_counter}]/[{request.split()[0][1:]}] PONG ({client_id})"
            response_counter += 1
            writer.write(response.encode() + b'\n')
            await writer.drain()
            response_time: str = datetime.datetime.now().strftime('%H:%M:%S.%f')[:-3]
            logger.info(f'{request_date};{request_time};{request};{response_time};{response}')

    writer.close()
    del clients[client_id]


async def keep_alive() -> None:
    global response_counter
    while True:
        await asyncio.sleep(5)
        response_counter += 1
        response: str = f"[{response_counter}] keepalive"
        for writer in clients.values():
            writer.write(response.encode() + b'\n')
            await writer.drain()


async def main() -> None:
    server: asyncio.Server = await asyncio.start_server(handle_client, '0.0.0.0', 8888)
    async with server:
        await asyncio.gather(server.serve_forever(), keep_alive())


asyncio.run(main())
