from datetime import datetime

from alphax.dataset.candle.candle_downloader import CandleDownloader
from alphax.dataset.candle.constants import CandleTimeframe
from alphax.dataset.candle.okx_candle_downloader import OkxCandleDownloader


def get_downloader() -> CandleDownloader:
    return OkxCandleDownloader()
