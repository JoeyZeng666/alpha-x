from unittest import TestCase

import alphax.core.logger as alphax_logger


class TestAlphaxLogger(TestCase):

    def test_debug_log(self):
        alphax_logger.init_log(log_is_debug=True)
        logger = alphax_logger.get_logger("test")
        logger.debug("test debug")
        logger.info("test info")
        logger.warning("test warning")
        logger.error("test error")
        logger.exception("test exception")

    def test_not_debug(self):
        alphax_logger.init_log(log_is_debug=False)
        logger = alphax_logger.get_logger("test")
        logger.debug("test debug")
        logger.info("test info")
        logger.warning("test warning")
        logger.error("test error")
        logger.exception("test exception")

