import datetime
import pandas as pd
import numpy as np


class DataCleaner:

    def __init__(self):
        pass

    def clean(self, raw_data):
        raw_data = DataCleaner._data_preprocess(raw_data)
        raw_data = DataCleaner._cut_out(raw_data)
        raw_data = DataCleaner._merge_same_time_data(raw_data)

        return raw_data

    @staticmethod
    def _convert_to_timestamp(time_str):
        dt = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S.%f")
        return int(dt.timestamp() * 1000)

    # 数据预处理
    @staticmethod
    def _data_preprocess(data_all):
        # 把time_level裁剪掉 level
        result = data_all["time_level"][0].replace(str(data_all["level"][0]), "")
        # 减去level，得到标准时间戳
        data_all["time"] = data_all.apply(
            lambda x: x["time_level"].replace(str(x["level"]), ""), axis=1
        )
        # 把data_all['time']转换为时间戳 long 类型
        data_all["time"] = data_all["time"].astype(np.int64)
        # 标记一下是买单还是卖单，卖单为1 ，卖单为-1
        data_all["side"] = data_all["level"].apply(lambda x: 1 if x > 0 else 0)
        #  排序 先按time从小到大，如果time相同，按level从大到小
        data_all = data_all.sort_values(
            by=["server_time", "level"], ascending=[True, False]
        )
        # 调整顺序,并且只保留需要的
        data_all = data_all[["server_time", "level", "price", "amount", "side"]]

        # 把 server_time 转成时间戳
        data_all["server_time"] = data_all["server_time"].apply(
            DataCleaner._convert_to_timestamp
        )

        return data_all

    # 裁剪一些数据
    @staticmethod
    def _cut_out(data_all):
        # 保留level在-3到3之间的数据(先简单实现)
        data_all = data_all[data_all["level"] <= 3]
        data_all = data_all[data_all["level"] >= -3]
        return data_all

    # 按时间拍平数据数据
    @staticmethod
    def _merge_same_time_data(data_all):
        # 把同一时间的数据打平
        asks = data_all[data_all["side"] == 1]
        asks_weight_pivot = asks.pivot(
            index="server_time", columns="level", values="amount"
        )
        asks_weight_pivot.columns = [
            f"ask_{i}_amount" for i in asks_weight_pivot.columns
        ]

        asks_price_pivot = asks.pivot(
            index="server_time", columns="level", values="price"
        )
        asks_price_pivot.columns = [f"ask_{i}_price" for i in asks_price_pivot.columns]

        bids = data_all[data_all["side"] == 0]
        bids_weight_pivot = bids.pivot(
            index="server_time", columns="level", values="amount"
        )
        bids_weight_pivot.columns = [
            f"bid_{abs(i)}_amount" for i in bids_weight_pivot.columns
        ]

        bids_price_pivot = bids.pivot(
            index="server_time", columns="level", values="price"
        )
        bids_price_pivot.columns = [
            f"bid_{abs(i)}_price" for i in bids_price_pivot.columns
        ]

        # 合并bid和ask订单
        data_all = pd.concat(
            [asks_price_pivot, bids_price_pivot, asks_weight_pivot, bids_weight_pivot],
            axis=1,
        ).reset_index()
        # 去重

        data_all.sort_index()
        return data_all
