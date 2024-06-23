import os
import sys


from order_book_ai.src.data_cleaner import DataCleaner
import pandas as pd

from order_book_ai.src.feature_builder import FeatureBuilder
from order_book_ai.src.model_tainer import ModelTrainer
from order_book_ai.src.target_builder import TargetBuilder
from sklearn.model_selection import train_test_split
import joblib


data_base_path = "/Users/zengyan/Excelsior/ai-trader/order_book_ai/data/"
input_file_name = "okxorderbook20240421"
output_file_name = "okxorderbook20240421_second"


if __name__ == "__main__":
    # 输入文件路径
    input_file_path = os.path.join(data_base_path, input_file_name + '.csv')
    # 输出文件路径
    output_file_path = os.path.join(data_base_path, output_file_name + '.csv')
    chunksize = 100000  # 每块数据的大小

# time_level,server_time,recvice_time,price,amount,level
    column_names = ['time_level', 'server_time', 'recvice_time','price','amount','level']
    # 处理和保存数据
    for i, chunk in enumerate(pd.read_csv(input_file_path, chunksize=chunksize,header=None)):
        print(f"正在处理第 {i} 块数据...")
        # 在这里处理每个 chunk
        chunk.columns = column_names
        # 示例：在每块数据中添加一列
        chunk = chunk[chunk["level"] <= 3]
        chunk = chunk[chunk["level"] >= -3]
        # 保存处理后的数据到新的 CSV 文件
        if i == 0:
            chunk.to_csv(output_file_path, index=False, mode='w')  # 创建新文件并写入
        else:
            chunk.to_csv(output_file_path, index=False, mode='a', header=False)  # 追加到现有文件中


    

