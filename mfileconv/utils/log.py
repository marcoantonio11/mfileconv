import logging
import os
from logging import handlers

LOG_LEVEL = os.getenv("LOG_LEVEL", "WARNING").upper()
LOG_LEVEL_NUM = getattr(logging, LOG_LEVEL, logging.WARNING)
log = logging.getLogger("mfileconv")
log.setLevel(LOG_LEVEL_NUM)
fmt = logging.Formatter(
    "%(asctime)s  %(name)s  %(levelname)s  l:%(lineno)d"
    "  f:%(filename)s: %(message)s"
)


def get_logger(logfile="mfileconv.log") -> logging.Logger:
    """Returns a configured logger"""
    if not log.handlers:
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)
        ch.setFormatter(fmt)

        fh = handlers.RotatingFileHandler(
            logfile, maxBytes=10**6, backupCount=10
        )
        fh.setLevel(LOG_LEVEL_NUM)
        fh.setFormatter(fmt)

        log.addHandler(ch)
        log.addHandler(fh)
    return log
