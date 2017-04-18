import asyncio
import unittest

from pytcp.server import TCPServer
from pytcp.utils.client import tcp_client


class TCPServerTests(unittest.TestCase):
    def setUp(self):
        # Creates new event loop for each test. It isolates them from each other.
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(None)

    def test_correct_bytes_number(self):
        test_host = '0.0.0.0'
        test_port = 8888
        server = TCPServer(test_host, test_port, loop=self.loop)
        server.start()

        test_sequences = [
            ('Hello World!\n', b'13\n'),
            ('\n', b'1\n'),
            ("пайтон\n", b'13\n')  # word 'python' in cyrillic
        ]
        for string in test_sequences:
            with self.subTest(string=string):
                actual_result = self.loop.run_until_complete(
                    tcp_client('127.0.0.1', test_port, string[0], loop=self.loop)
                )
                self.assertEqual(actual_result, string[1])
        server.stop()

    def tearDown(self):
        self.loop.close()
