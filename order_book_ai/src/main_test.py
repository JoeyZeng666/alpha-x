import os
import sys


from order_book_ai.src.data_cleaner import DataCleaner
import pandas as pd

from order_book_ai.src.feature_builder import FeatureBuilder
from order_book_ai.src.model_tainer import ModelTrainer
from order_book_ai.src.target_builder import TargetBuilder
from sklearn.model_selection import train_test_split
import joblib
from sklearn import metrics


data_base_path = "/Users/zengyan/Excelsior/ai-trader/order_book_ai/data/result_test/"


def handle_data(raw_data):

    # print(f"开始清洗数据...")
    data_cleaner = DataCleaner()
    cleaned_data = data_cleaner.clean(raw_data)
    cleaned_data.to_csv(f"{data_base_path}cleaned.csv", index=False)
    # print(f"数据清洗完成，清洗后的数据保存在 {data_base_path}cleaned.csv")

    feature_builder = FeatureBuilder()
    featured_data = feature_builder.build(cleaned_data)
    featured_data.to_csv(f"{data_base_path}featured.csv", index=False)
    # print(f"特征构建完成，特征构建后的数据保存在 {data_base_path}featured.csv")

    target_builder = TargetBuilder()
    target_data = target_builder.build(featured_data)
    target_data.to_csv(f"{data_base_path}target.csv", index=False)
    # print(f"目标构建完成，目标构建后的数据保存在 {data_base_path}target.csv")

    return target_data



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


if __name__ == "__main__":

    test_data = pd.read_csv(
        "/Users/zengyan/Excelsior/ai-trader/order_book_ai/data/hours/data_2024-04-21 02.csv"
    )
    # test_data = test_data.head(10)

    target_data = handle_data(test_data)
    x_test,y_test = select_features(target_data)

        # 定义模型文件路径
    model_file_path = '/Users/zengyan/Excelsior/ai-trader/order_book_ai/data/result/model.pkl'

    # 加载模型
    model = joblib.load(model_file_path)
    df1 = pd.DataFrame(x_test.columns,columns=['Variable'])
    df2 = pd.DataFrame(model.feature_importances_,columns=['Importance'])
    variable_importances = pd.concat([df1,df2],axis=1).sort_values(by='Importance',ascending=False)
    variable_importances.to_csv(f"{data_base_path}variable_importances.csv", index=False)

    # 正式预测
    y_pred = model.predict(x_test)
    # 与真实值比较
    print("预测结束：")
    # 计算性能指标
    accuracy = metrics.accuracy_score(y_test, y_pred)
    precision = metrics.precision_score(y_test, y_pred, average='weighted')  # 平均方式可根据需要调整
    recall = metrics.recall_score(y_test, y_pred, average='weighted')
    f1 = metrics.f1_score(y_test, y_pred, average='weighted')

    # 打印性能指标
    print("随机森林模型预测结果：")
    print(f"准确率：{accuracy:.2f}")
    print(f"精确率：{precision:.2f}")
    print(f"召回率：{recall:.2f}")
    print(f"F1分数：{f1:.2f}")

    

