import asyncio


async def tcp_client(host, port, message, loop):
    """Simple TCP client coroutine. Sends bytes to the specific server.
    Receives bytes from it.

    :param host: str, which defines server's address to connect.
    :param port: int, which defines server's port to connect.
    :param message: string, that will be sent to the server.
    :param loop: specific event loop if needed.
    :return: received data from the server.
    """
    reader, writer = await asyncio.open_connection(host, port, loop=loop)
    writer.write(message.encode())
    data = await reader.read(100)
    writer.close()
    return data

