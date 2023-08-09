# https://bytepawn.com/writing-a-simple-python-async-message-queue-server.html
import sys, asyncio


async def handle_client(reader, writer):
    print("New client connected...")
    line = str()
    while line.strip() != "quit":
        line = (await reader.readline()).decode("utf8")
        if line.strip() == "":
            continue
        print(f"Received: {line.strip()}")
        writer.write(line.encode("utf8"))
    writer.close()
    print("Client disconnected...")


async def run_server(host, port):
    server = await asyncio.start_server(handle_client, host, port)
    print(f"Listening on {host}:{port}...")
    async with server:
        await server.serve_forever()


asyncio.run(run_server(host="localhost", port=int(sys.argv[1])))
