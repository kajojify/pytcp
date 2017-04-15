import asyncio
import logging
import concurrent.futures

from pytcp.misc import drop_privileges

logger = logging.getLogger(__name__)


class TCPServer:

    """

    """

    def __init__(self, host, port, loop=None):
        """

        :param host:
        :param port:
        :param loop:
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
        self._loop.run_forever()

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
        finally:
            self._loop.close()

    async def _handle_connection(self, reader, writer):
        """

        :param reader:
        :param writer:
        """
        peername = writer.get_extra_info('peername')
        logger.info("Accepted connection from {}:{}.".format(*peername))
        try:
            data = await asyncio.wait_for(reader.readline(), timeout=30.0)
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
