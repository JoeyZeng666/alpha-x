import datetime
import sys
import pandas as pd
import numpy as np
import sklearn

# 读取数据，
def read_data(file_path):
    data = pd.read_csv(file_path)
    return data

def convert_to_timestamp(time_str):
    dt = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S.%f")
    return int(dt.timestamp() * 1000)


# 数据预处理
def data_preprocess(data_all):
     # 把time_level裁剪掉 level
    result = data_all['time_level'][0].replace(str(data_all['level'][0]), '')
    # 减去level，得到标准时间戳
    data_all['time'] = data_all.apply(lambda x: x['time_level'].replace(str(x['level']), ''), axis=1)
    # 把data_all['time']转换为时间戳 long 类型
    data_all['time'] =data_all['time'].astype(np.int64)
    # 标记一下是买单还是卖单，卖单为1 ，卖单为-1
    data_all['side'] = data_all['level'].apply(lambda x: 1 if x > 0 else 0)
    #  排序 先按time从小到大，如果time相同，按level从大到小
    data_all = data_all.sort_values(by=['server_time', 'level'], ascending=[True, False])
    # 调整顺序,并且只保留需要的
    data_all = data_all[['server_time', 'level', 'price', 'amount','side']]

    # 把 server_time 转成时间戳
    data_all['server_time'] = data_all['server_time'].apply(convert_to_timestamp)
    print(data_all.head())

    return data_all

# 裁剪一些数据
def cut_out(data_all):
    # 保留level在-3到3之间的数据(先简单实现)
    data_all = data_all[data_all['level'] <= 3]
    data_all = data_all[data_all['level'] >= -3]
    return data_all

# 合并数据
def merge_data(data_all):
    # 把同一时间的数据打平
    asks = data_all[data_all['side'] == 1]
    asks_pivot = asks.pivot(index='server_time', columns='level', values='price')
    asks_pivot.columns =[f'ask_{i}_price' for i in asks_pivot.columns]

    bids = data_all[data_all['side'] == 0]
    bids_pivot = bids.pivot(index='server_time', columns='level', values='price')
    bids_pivot.columns =[f'bid_{abs(i)}_price' for i in bids_pivot.columns]
    

    # 合并bid和ask订单
    data_all = pd.concat([ asks_pivot,bids_pivot], axis=1).reset_index()
    # 去重

    data_all.sort_index()
    return data_all

def go_clean_data(file_path):
    data_all = read_data(file_path)
    data_all = data_preprocess(data_all)
    data_all = cut_out(data_all)
    data_all = merge_data(data_all)
    print(data_all.columns)
    return data_all


data = go_clean_data('order_book_ai/dataset_temp/okxorderbook20240421_1.csv')
data.to_csv('order_book_ai/dataset_temp/okxorderbook20240421_1_cleaned.csv', index=False)





