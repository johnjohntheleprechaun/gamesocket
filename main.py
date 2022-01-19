import websockets
import asyncio

class Server:
	future: any
	addr: str
	port: int
	should_close = False

	async def client_handler(self, conn: any, path: str):
		self.stop()
	
	async def main(self):
		async with websockets.serve(self.client_handler, self.addr, self.port):
			loop = asyncio.get_running_loop()
			self.future = loop.create_future()
			await self.future
	
	def start(self):
		asyncio.run(self.main())
		print(self.future.result())
	
	def stop(self, reason = "just because"):
		self.future.set_result(f"server stopped ({reason})")
	
	def __init__(self, addr: str, port: int):
		self.addr = addr
		self.port = port


server = Server("0.0.0.0", 33205)
server.start()