import websockets
import asyncio

async def main():
	async with websockets.connect("ws://localhost:33205") as websocket:
		print(await websocket.recv())

asyncio.run(main())