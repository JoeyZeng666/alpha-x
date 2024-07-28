from alphax.core.logger.alphax_logger import AlphaxLogger
from alphax.core.logger import config as logger_config

CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0


def init_log(log_is_debug: bool):
    logger_config.LOG_IS_DEBUG = log_is_debug
    if logger_config.LOG_IS_DEBUG:
        logger_config.LOG_CONSOLE = True
        logger_config.LOG_LEVEL = DEBUG
    else:
        logger_config.LOG_CONSOLE = False
        logger_config.LOG_LEVEL = INFO


def get_logger(tag=None) -> AlphaxLogger:
    return AlphaxLogger(tag=tag)
