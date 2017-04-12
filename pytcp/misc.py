import logging
import os, pwd, grp


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
    logger = logging.getLogger(__name__)
    if os.getuid() != 0:
        return

    wanted_uid = pwd.getpwnam(uid_name).pw_uid
    wanted_gid = grp.getgrnam(gid_name).gr_gid

    try:
        os.setgid(wanted_gid)
        os.setuid(wanted_uid)
    except OSError as err:
        logger.error("Failed to drop privileges "
                    "to {}/{}: {}.".format(uid_name, gid_name, err))
        exit("Stopping...")

    new_uid_name = pwd.getpwuid(os.getuid()).pw_name
    new_gid_name = grp.getgrgid(os.getgid()).gr_name

    logger.info("Privileges dropped, "
                "running as {}/{}.".format(new_uid_name, new_gid_name))