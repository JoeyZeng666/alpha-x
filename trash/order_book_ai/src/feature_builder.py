import datetime
import sys
import pandas as pd
import numpy as np
import sklearn


class FeatureBuilder:

    def build(self, data):
        data = FeatureBuilder._unique_second(data)
        data = FeatureBuilder._build_price_rise_radio(data)
        data = FeatureBuilder._build_weight_percentage(data)
        return data

    @staticmethod
    def _unique_second(data):
        # 每一秒只保留一个数据
        data["datetime"] = pd.to_datetime(data["server_time"], unit="ms")
        # 设置server_time为索引
        data.set_index("datetime", inplace=True)
        # 按秒对server_time进行分组，并选择每个组的第一个记录
        df_unique_second = data.groupby(data.index.floor("S")).first()
        # 如果需要，可以将结果转换回DataFrame，并重置索引
        df_unique_second = df_unique_second.reset_index()
        return df_unique_second

    @staticmethod
    def _build_price_rise_radio(data):
        """构建涨幅特征"""
        # 从5秒 到 60 秒，步长为5秒
        for i in range(5, 60, 5):
            data["rise_radio_" + str(i)] = data["price"].pct_change(i)
        return data


    @staticmethod
    def _build_weight_percentage(data_all):
        """构建量的比例特征"""
        # 生成权重，总权重为100，分为三个，每个步长为10，
        weights = []
        for i in range(0, 100, 10):
            for j in range(0, 100 - i, 10):
                weights.append([i, j, (100 - i - j)])

        # new_features = pd.DataFrame(index=data_all.index)
        new_columns = {}
        for weight in weights:
            weight_ask = (
                weight[0] * data_all["ask_1_amount"]
                + weight[1] * data_all["ask_2_amount"]
                + weight[2] * data_all["ask_3_amount"]
            )
            weight_bid = (
                weight[0] * data_all["bid_1_amount"]
                + weight[1] * data_all["bid_2_amount"]
                + weight[2] * data_all["bid_3_amount"]
            )
            w_ask_over_bid = weight_ask / weight_bid
            w_ask_bid_gap = (weight_ask - weight_bid) / (weight_ask + weight_bid)

            new_columns[f"w{weight[0]}_{weight[1]}_{weight[2]}_ask_over_bid"] = (
                w_ask_over_bid
            )
            new_columns[f"w{weight[0]}_{weight[1]}_{weight[2]}_ask_bid_gap"] = (
                w_ask_bid_gap
            )

         # 创建一个包含所有新特征的DataFrame
        new_features = pd.DataFrame(new_columns)
         # 将新特征合并到原始DataFrame中
        data_all = pd.concat([data_all, new_features], axis=1)
        return data_all

