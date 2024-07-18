import logging


class AlphaxLogger:
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

    def __init__(self, tag=None, level=logging.INFO):
        self.tag = tag
        logging.basicConfig()
        self.logger = logging.getLogger()
        self.logger.

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
