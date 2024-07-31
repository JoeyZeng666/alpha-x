from unittest import TestCase

import alphax.core.logger as alphax_logger


class TestAlphaxLogger(TestCase):

    def test_debug_log(self):
        alphax_logger.init_log(log_is_debug=True)
        logger = alphax_logger.get_logger("alphax_test")
        logger.debug("alphax_test debug")
        logger.info("alphax_test info")
        logger.warning("alphax_test warning")
        logger.error("alphax_test error")
        logger.exception("alphax_test exception")

    def test_not_debug(self):
        alphax_logger.init_log(log_is_debug=False)
        logger = alphax_logger.get_logger("alphax_test")
        logger.debug("alphax_test debug")
        logger.info("alphax_test info")
        logger.warning("alphax_test warning")
        logger.error("alphax_test error")
        logger.exception("alphax_test exception")

