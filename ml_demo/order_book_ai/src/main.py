from ml_demo.order_book_ai.src.data_cleaner import DataCleaner
import pandas as pd

from ml_demo.order_book_ai.src.feature_builder import FeatureBuilder
from ml_demo.order_book_ai.src.model_tainer import ModelTrainer
from ml_demo.order_book_ai.src.target_builder import TargetBuilder
import joblib


data_base_path = "/Users/zengyan/Excelsior/ai-trader/order_book_ai/data/result/"


def handle_data(raw_data):

    print(f"开始清洗数据...")
    data_cleaner = DataCleaner()
    cleaned_data = data_cleaner.clean(raw_data)
    cleaned_data.to_csv(f"{data_base_path}cleaned.csv", index=False)
    print(f"数据清洗完成，清洗后的数据保存在 {data_base_path}cleaned.csv")

    feature_builder = FeatureBuilder()
    featured_data = feature_builder.build(cleaned_data)
    featured_data.to_csv(f"{data_base_path}featured.csv", index=False)
    print(f"特征构建完成，特征构建后的数据保存在 {data_base_path}featured.csv")

    target_builder = TargetBuilder()
    target_data = target_builder.build(featured_data)
    target_data.to_csv(f"{data_base_path}target.csv", index=False)
    print(f"目标构建完成，目标构建后的数据保存在 {data_base_path}target.csv")

    return target_data


def train(target_data):
    x_train, y_train= select_features(target_data)

    model_trainer = ModelTrainer()
    print("开始训练模型...")
    final_model = model_trainer.train_model(x_train, y_train)
    print("模型训练完成...")
    model_path = f"{data_base_path}model.pkl"
    joblib.dump(final_model, model_path)
    print(f"模型保存在 {model_path}")


def select_features(data):
    """选择特征"""
    print("选择特征...")
    # 删除有缺失值的行
    data = data.dropna()
    # 目标列
    target = data["target"]
    # 删除无用的列，如时间列
    only_features = data.drop(["target", "datetime", "server_time"], axis=1)
    # 最后拆分数据，返回训练集和测试集
    return only_features, target
    # return train_test_split(only_features, target, test_size=0.4, random_state=42)


if __name__ == "__main__":
    raw_data = pd.read_csv(
        "/Users/zengyan/Excelsior/ai-trader/order_book_ai/data/hours/data_2024-04-21 00.csv"
    )
    target_data = handle_data(raw_data)
    train(target_data)
