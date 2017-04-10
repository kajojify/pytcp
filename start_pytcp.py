import logging

from argparse import ArgumentParser
from pytcp.server import TCPServer


def tune_logging(logfile):
    logger = logging.getLogger()

    loglevel = logging.INFO
    logger.setLevel(logging.INFO)

    default_formatter = logging.Formatter('%(asctime)-15s %(message)s')

    console_log = logging.StreamHandler()
    console_log.setLevel(loglevel)
    console_log.setFormatter(default_formatter)

    file_log = logging.FileHandler(logfile)
    file_log.setFormatter(default_formatter)
    file_log.setLevel(loglevel)

    logger.addHandler(file_log)
    logger.addHandler(console_log)


def drop_privileges(uid_name='nobody', gid_name='nogroup'):
    pass


if __name__ == '__main__':
    parser = ArgumentParser(description="Simple Python 3 TCP server - pytcp.")
    parser.add_argument("-p", "--port", default=8888, help="Port to listen", type=int)
    parser.add_argument("-l", "--logfile", default="pytcp.log", help="The path to the logfile")
    args = parser.parse_args()

    tune_logging(args.logfile)
    server = TCPServer('127.0.0.1', args.port)
    try:
        server.start()
    except KeyboardInterrupt:
        pass
    finally:
        server.stop()
