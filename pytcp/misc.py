import pytcp
import logging
import os, pwd, grp, sys


def tune_logging(logfile):
    """Tunes root logger, adding specific console/file handlers.

    It also sets log format and handles exceptions, which can be raised
    in case of incorrect input of logfile path.
    :param logfile: the path to the file for logging.
    """
    root_logger = logging.getLogger()

    default_logfile_name = "pytcp.log"
    # setting default logfile path for possible incorrect input of logfile
    default_logfile = get_logfile_abspath(default_logfile_name)

    loglevel = logging.INFO
    root_logger.setLevel(loglevel)

    default_formatter = logging.Formatter('%(asctime)-15s (%(name)s) %(message)s')

    console_log = logging.StreamHandler()
    console_log.setLevel(loglevel)
    console_log.setFormatter(default_formatter)
    root_logger.addHandler(console_log)

    try:
        file_log = logging.FileHandler(logfile)
    except (FileNotFoundError, IsADirectoryError) as err:
        root_logger.error("Wrong logfile name: {}."
                          " DEFAULT logfile is used.".format(err))
        file_log = logging.FileHandler(default_logfile)
    root_logger.info("Started logging to file - {}".format(file_log.baseFilename))

    file_log.setFormatter(default_formatter)
    file_log.setLevel(loglevel)
    root_logger.addHandler(file_log)


def get_logfile_abspath(logfile_name):
    """Returns absolute path for logfile_name depending
    on the directory, where pytcp was launched."""
    package_directory = os.path.dirname(os.path.abspath(pytcp.__file__))
    default_logfile = os.path.join(package_directory, logfile_name)
    return default_logfile


def drop_privileges(uid_name='nobody', gid_name='nogroup'):
    """Drops privileges to selected user and group.

    Handles exception in case of failure and logs the result of working.
    :param uid_name: desired user name;
    :param gid_name: desired group name;
    """
    logger = logging.getLogger(__name__)
    if os.getuid() != 0:  # If we aren't root
        return

    wanted_uid = pwd.getpwnam(uid_name).pw_uid
    wanted_gid = grp.getgrnam(gid_name).gr_gid

    try:
        os.setgid(wanted_gid)
        os.setuid(wanted_uid)
    except OSError as err:
        logger.error("Failed to drop privileges "
                     "to {}/{}: {}.".format(uid_name, gid_name, err))
        sys.exit("Stopping...")

    new_uid_name = pwd.getpwuid(os.getuid()).pw_name
    new_gid_name = grp.getgrgid(os.getgid()).gr_name

    logger.info("Privileges dropped, "
                "running as {}/{}.".format(new_uid_name, new_gid_name))
