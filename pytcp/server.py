import asyncio
import logging
import concurrent.futures

from pytcp.misc import drop_privileges

logger = logging.getLogger(__name__)


class TCPServer:
    """Implements TCP echo-like server logic."""

    def __init__(self, host, port, loop=None):
        """Initialize event loop for our server. Declares a socket server,
        with a coroutine function (method) for each client connected.

        :param host: string, which defines the host to bind.
        :param port: int number, which defines the port to bind.
        :param loop: specific event loop if needed.
        """
        self._loop = loop or asyncio.get_event_loop()
        self._server_coro = asyncio.start_server(self._handle_connection,
                                                 host, port, loop=self._loop)

    def start(self):
        """Starts pytcp server."""
        self._server = self._loop.run_until_complete(self._server_coro)
        serving_port = self._server.sockets[0].getsockname()[1]
        logger.info("Serving on {} port.".format(serving_port))
        drop_privileges()

    def stop(self):
        """Stops pytcp server."""
        try:
            # self._server can be undefined if an exception is raised in
            # self.start method before self._server declaration.
            # So, we handle such situation here.
            self._server.close()
            self._loop.run_until_complete(self._server.wait_closed())
        except AttributeError:
            pass

    async def _handle_connection(self, reader, writer):
        """Handles each client connected.

        Receives bytes from the client and sends back overall number
        of received bytes. Timeout is set to 30 seconds, so the client must send
        something to the server in this period. It also logs the result of its working.
        Next args are passed automatically:
        :param reader: StreamReader object. It's used to read data from the client.
        :param writer: StreamWriter object. It's used to send data to the client.
        """
        peername = writer.get_extra_info('peername')
        logger.info("Accepted connection from {}:{}.".format(*peername))
        try:
            data = await asyncio.wait_for(reader.readline(),
                                          timeout=30.0, loop=self._loop)
            # Number of bytes including CRLF
            bytes_number = get_bytes_number_str(data)
            writer.write(bytes_number)
            logger.info("Received {} bytes from {}:{}.".format(len(data), *peername))
        except concurrent.futures.TimeoutError:
            pass
        writer.close()
        logger.info("Connection with {}:{} was terminated.".format(*peername))


def get_bytes_number_str(data):
    """Returns string, which contains number of bytes and newline symbol."""
    bytes_number_str = str(len(data)) + '\n'
    return bytes_number_str.encode()
