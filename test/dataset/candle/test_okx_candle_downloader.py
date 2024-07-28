from datetime import datetime
from unittest import TestCase

import pandas as pd

from alphax import OkxCandleDownloader


class TestOkxCandleDownloader(TestCase):
    def test_download(self):
        downloader = OkxCandleDownloader()
        file_path = "/Users/zengyan/Excelsior/alpha-x/test/dataset/candle/test.csv"
        downloader.download(symbol="DOGE/USDT:USDT",
                            timeframe='5m',
                            since=datetime(2024, 7, 1, 00, 00, 00),
                            before=datetime(2024, 7, 5, 00, 00, 00),
                            file_path=file_path
                            )
        data = pd.read_csv(file_path)
        assert data.count() > 0
