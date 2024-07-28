from abc import ABC, abstractmethod
from datetime import datetime

from alphax.dataset.candle.constants import CandleTimeframe


class CandleDownloader(ABC):

    @abstractmethod
    def download(self,
                       symbol: str,
                       timeframe: CandleTimeframe,
                       since: datetime,
                       before: datetime,
                       file_path: str):
        pass
