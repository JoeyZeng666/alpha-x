import os
import sys


from order_book_ai.src.data_cleaner import DataCleaner
import pandas as pd

def main():

    data_base_path = "/Users/zengyan/Excelsior/ai-trader/order_book_ai/data/"
    data_file_name = "okxorderbook20240421_1"

    print(f"开始清洗数据:  {data_base_path}{data_file_name}.csv")

    raw_data = pd.read_csv(f"{data_base_path}{data_file_name}.csv")

    data_cleaner = DataCleaner()
    cleaned_data = data_cleaner.clean(raw_data)
    cleaned_data.to_csv(f"{data_base_path}{data_file_name}_cleaned.csv", index=False)


if __name__ == "__main__":
    main()
    

