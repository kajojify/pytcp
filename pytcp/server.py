import asyncio
import logging
import concurrent.futures


class TCPServer:
    def __init__(self, host, port, loop=None):
        self._loop = loop or asyncio.get_event_loop()
        self._server = asyncio.start_server(self.handle_connection, host=host, port=port)

    def start(self):
        self._server = self._loop.run_until_complete(self._server)
        logging.info('Listening established on {}:{}'.format(*self._server.sockets[0].getsockname()))
        self._loop.run_forever()

    def stop(self):
        self._server.close()
        self._loop.close()

    async def handle_connection(self, reader, writer):
        peername = writer.get_extra_info('peername')
        logging.info('Accepted connection from {}:{}'.format(*peername))
        try:
            data = await asyncio.wait_for(reader.readline(), timeout=20.0)
            bytes_number_str = get_number_of_bytes(data)
            writer.write(bytes_number_str)
            logging.info('Received {} bytes from the client.'.format(len(data)))
        except concurrent.futures.TimeoutError:
            pass
        writer.close()

def get_number_of_bytes(data):
    bytes_number_str = str(len(data)) + '\n'
    return bytes_number_str.encode()
