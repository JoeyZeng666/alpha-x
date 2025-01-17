from datetime import datetime
from unittest import TestCase

import pandas as pd

from alphax import OkxCandleDownloader


class TestOkxCandleDownloader(TestCase):
    def test_download(self):
        downloader = OkxCandleDownloader()

        file_path = downloader.download(symbol="DOGE/USDT:USDT",
                                        timeframe='1h',
                                        since=datetime(2024, 1, 1, 00, 00, 00),
                                        before=datetime(2024, 7, 1, 00, 00, 00),
                                        )
        data = pd.read_csv(file_path)
        # 判断data 的长度是否大于0
        assert len(data) > 0
