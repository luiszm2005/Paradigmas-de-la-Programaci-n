import asyncio

async def handle_connection(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    print(f"Recibido: {message}")
    writer.close()

async def main():
    server = await asyncio.start_server(handle_connection, '127.0.0.1', 8888)
    async with server:
        await server.serve_forever()

asyncio.run(main())