import logging

import colorlog

from alphax.core.logger import config


class AlphaxLogger:

    def __init__(self, tag='alphax'):
        self.tag = tag
        self.logger = logging.getLogger()
        self.logger.setLevel(config.LOG_LEVEL)
        if config.LOG_CONSOLE:
            self.logger.addHandler(self._create_stream_handler())

    @staticmethod
    def _create_stream_handler():
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(config.LOG_LEVEL)
        log_colors = {
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'purple'
        }
        stream_handler.setFormatter(colorlog.ColoredFormatter(
            fmt=config.LOG_FORMAT,
            log_colors=log_colors))
        return stream_handler

    def debug(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)

    def exception(self, msg, *args, exc_info=True, **kwargs):
        self.logger.exception(msg, *args, exc_info=exc_info, **kwargs)
