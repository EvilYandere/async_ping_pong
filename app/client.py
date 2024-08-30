import asyncio
import datetime
import random
from logger import get_logger

logger = get_logger("client")


async def client() -> None:
    reader: asyncio.StreamReader
    writer: asyncio.StreamWriter
    reader, writer = await asyncio.open_connection('server', 8888)

    request_counter: int = 0
    while True:
        await asyncio.sleep(random.uniform(0.3, 3))
        request: str = f"[{request_counter}] PING"
        request_date: str = datetime.datetime.now().strftime('%Y-%m-%d')
        request_time: str = datetime.datetime.now().strftime('%H:%M:%S.%f')[:-3]
        writer.write(request.encode() + b'\n')
        await writer.drain()
        data: bytes = await reader.readline()
        response: str = data.decode().strip()
        response_time: str = datetime.datetime.now().strftime('%H:%M:%S.%f')[:-3]
        if "keepalive" in response:
            logger.info(f'{request_date};{request_time};{response_time};{response}')
        else:
            logger.info(f'{request_date};{request_time};{request};{response_time};{response}')
        request_counter += 1


asyncio.run(client())
