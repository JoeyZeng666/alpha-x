
import datetime
from math import inf, nan
import sys
import pandas as pd
import talib

window_size = 5

# 读取数据，
def read_data(file_path):
    data = pd.read_csv(file_path)
    return data

def build_sma(data):
    data['close_sma'] = talib.SMA(data['close'], timeperiod=window_size)
    return data

def build_ema(data):
    data['close_ema'] = talib.EMA(data['close'], timeperiod=window_size)
    return data

def build_rsi(data):
    data['close_rsi'] = talib.RSI(data['close'], timeperiod=window_size)
    return data


def build_bb_bands(data):
    upper_band,middle_band,lower_band = talib.BBANDS(data['close'], timeperiod=window_size)
    # data['close_bb_upper_band'] = upper_band
    # data['close_bb_middle_band'] = middle_band
    # data['close_bb_lower_band'] = lower_band
    data['close_bb_position'] = ((data['close'] - lower_band) / (upper_band - lower_band))
    # 替换无穷大和负无穷大值
    data['close_bb_position'].replace([inf, -inf], nan, inplace=True)
    return data



def go_clean_data(file_path):
    data_all = read_data(file_path)
    data_all = build_sma(data_all)
    data_all = build_ema(data_all)
    data_all = build_bb_bands(data_all)
    return data_all

file_path = '/Users/zengyan/Excelsior/ai-trader/temp/doge_5m_0701_0705.csv'
data_cleaned = go_clean_data(file_path)
data_cleaned.head(50)
# data_cleaned.to_csv('/Users/zengyan/Excelsior/ai-trader/order_book_ai/data/okxorderbook20240421_1_cleaned.csv', index=False)


