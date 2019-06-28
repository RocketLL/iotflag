import asyncio
import websockets
import datetime
import uuid

"""
This is the IoT client's source code.
Each client is supplied with an UUID at initialization.
"""

def generate_uuid():
    return uuid.uuid4().hex[:6]


async def check_date(date):
    async with websockets.connect("ws://localhost:8765") as websocket:

        await websocket.send(date)
        print(f"> {date}")

        resp = await websocket.recv()
        print(f"< {resp}")


asyncio.get_event_loop().run_until_complete(check_date())
asyncio.get_event_loop().run_forever()
