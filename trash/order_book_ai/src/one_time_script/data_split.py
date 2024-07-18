import pandas as pd

if __name__ == "__main__":
    raw_data = pd.read_csv(
        "/Users/zengyan/Excelsior/ai-trader/order_book_ai/data/okxorderbook20240421_second.csv"
    )
    raw_data["server_time"] = pd.to_datetime(raw_data["server_time"])


    # 添加小时字段
    raw_data['hour'] = raw_data['server_time'].dt.strftime('%Y-%m-%d %H')

    # 按小时分组并保存每个小时的数据到单独的 CSV 文件
    for hour, group in raw_data.groupby('hour'):
        output_file_path = f'/Users/zengyan/Excelsior/ai-trader/order_book_ai/data/hours/data_{hour.replace(":", "-")}.csv'
        group.drop(columns=['hour'], inplace=True)
        group.to_csv(output_file_path, index=False)
        print(f"Saved {output_file_path}")

    # # 拆分上半天和下半天
    # morning_data = raw_data[raw_data["server_time"].dt.hour < 12]
    # afternoon_data = raw_data[raw_data["server_time"].dt.hour >= 12]

    # morning_data.to_csv("/Users/zengyan/Excelsior/ai-trader/order_book_ai/data/morning_data.csv", index=False)
    # afternoon_data.to_csv("/Users/zengyan/Excelsior/ai-trader/order_book_ai/data/afternoon_data.csv", index=False)


    

