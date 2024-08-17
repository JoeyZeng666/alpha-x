import datetime
import json

import ccxt.pro
import time

import pandas as pd

from alphax.core.utils import TimeUtil, FileUtil
from alphax.dataset.candle import DATASET_ORDERBOOK_DIR


class OkxOrderbookCollecter:
    exchange = ccxt.okx()

    def start(self, symbol: str, interval_time: int, file_dir: str = DATASET_ORDERBOOK_DIR):

        file_path = f"{file_dir}/{symbol.replace('/', '_')}_orderbook_{interval_time}_{TimeUtil.to_str(TimeUtil.now())}.csv"
        print(f"Start collecting order book data to {file_path}...")
        FileUtil.create_file(file_path)
        # 创建空的 CSV 文件并写入表头
        with open(file_path, 'w', newline='') as file:
            header = ['symbol', 'timestamp', 'datetime', 'bids', 'asks']
            df = pd.DataFrame(columns=header)
            df.to_csv(file, index=False)
        index = 0
        while True:
            index += 1
            order_book = self._fetch_order_book(symbol)
            if not order_book:
                continue
            print(f"第{index}次获取数据...")
            self._save_order_book_to_csv(order_book, file_path)
            time.sleep(interval_time)
            # 每5秒获取一次订单簿数据

    def _save_order_book_to_csv(self, order_book, file_path):
        # 将 bids 和 asks 转换为字符串
        order_book['bids'] = json.dumps(order_book['bids'])
        order_book['asks'] = json.dumps(order_book['asks'])

        # 创建 DataFrame
        df = pd.DataFrame([order_book], columns=['symbol', 'timestamp', 'datetime', 'bids', 'asks'])

        # 保存 DataFrame 到 CSV 文件
        df.to_csv(file_path, mode='a', header=False, index=False)

    def _fetch_order_book(self, symbol):
        try:
            order_book = self.exchange.fetch_order_book(symbol)
            return order_book
        except Exception as e:
            print(f"Error fetching order book: {str(e)}")
            return None


if __name__ == '__main__':
    collecter = OkxOrderbookCollecter()
    collecter.start("BTC/USDT", 5)
