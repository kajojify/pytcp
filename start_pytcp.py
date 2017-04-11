import logging
import pytcp

from argparse import ArgumentParser
from pytcp.server import TCPServer

logger = logging.getLogger()


def tune_logging(logfile):
    root_logger = logging.getLogger()

    loglevel = logging.INFO
    root_logger.setLevel(loglevel)

    default_formatter = logging.Formatter('%(asctime)-15s (%(name)s) %(message)s')

    console_log = logging.StreamHandler()
    console_log.setLevel(loglevel)
    console_log.setFormatter(default_formatter)

    file_log = logging.FileHandler(logfile)
    file_log.setFormatter(default_formatter)
    file_log.setLevel(loglevel)

    root_logger.addHandler(file_log)
    root_logger.addHandler(console_log)



def drop_privileges(uid_name='nobody', gid_name='nogroup'):
    pass


if __name__ == '__main__':
    parser = ArgumentParser(description="Simple Python 3 TCP server - pytcp.")
    parser.add_argument("-p", "--port", default=8888, help="Port to listen on", type=int)
    parser.add_argument("-l", "--logfile", default="pytcp.log", help="The path to the logfile")
    args = parser.parse_args()

    tune_logging(args.logfile)
    logger.info("Welcome to pytcp v{}! Press Ctrl+C to stop the server.".format(pytcp.version))

    server = TCPServer('0.0.0.0', args.port)
    try:
        server.start()
    except KeyboardInterrupt:
        pass
    finally:
        server.stop()
