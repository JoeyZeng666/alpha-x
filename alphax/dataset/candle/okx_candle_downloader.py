import time
from datetime import datetime

import ccxt
import pandas as pd

from alphax.core.utils.time_util import TimeUtil
from alphax.dataset.candle.candle_downloader import CandleDownloader
from alphax.dataset.candle.constants import CandleTimeframe

class OkxCandleDownloader(CandleDownloader):

    def download(self, symbol: str, timeframe: CandleTimeframe, since: datetime, before: datetime,
                 file_path: str):
        exchange = ccxt.okx()
        print(f"Fetching data from {since} to {before} ...")
        since_mills = TimeUtil.millisecond(since)
        before_mills = TimeUtil.millisecond(before)
        all_ohlcvs = []
        count = 0
        while since_mills < before_mills:
            count += 1
            print(f"Fetching data since {count} ...")
            ohlcvs = exchange.fetch_ohlcv(symbol=symbol, timeframe=timeframe, since=since_mills, limit=100)
            if not ohlcvs:
                break
            since_mills = ohlcvs[-1][0] + 1
            all_ohlcvs.extend(ohlcvs)
            time.sleep(exchange.rateLimit / 1000)

        df = pd.DataFrame(all_ohlcvs, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df.to_csv(file_path, index=False)
        print(f"Data has been saved to {file_path}")
