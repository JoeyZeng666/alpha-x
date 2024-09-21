from unittest import TestCase

from alphax.core.logger import get_log_uploader
from alphax.core.logger.alphax_log_uploader import TopicID


class TestAlphaxLogUploader(TestCase):

    def test_upload(self):
        uploader = get_log_uploader()
        result = uploader.upload(TopicID.NORMAL_LOG, content_dict={
            "key1": "value1",
            "key2": "value2"
        })
        assert result