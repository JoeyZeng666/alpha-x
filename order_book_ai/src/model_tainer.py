import datetime
import sys
import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier


class ModelTrainer:

    @staticmethod
    def train_model(x_train,y_train):
        '''训练模型'''
        best_params = ModelTrainer.find_best_params(x_train,y_train)
        rf = ModelTrainer.train(x_train,y_train,best_params)
        return rf


    @staticmethod
    def find_best_params(x_train,y_train):
        # 用GridSearchCV来找到最佳参数
        print("寻找最佳的超参数 ..... ")
        rf = RandomForestClassifier(max_features='sqrt', random_state=1, n_jobs=-1)
        param_grid = {
                        "criterion": ['gini','entropy'],
                        "min_samples_leaf": [1, 5, 10, 25],
                        'min_samples_split': [2, 4, 10, 12, 16, 18, 25, 35],
                        "n_estimators": [25, 50,100, 150], 
                        'max_depth': [3, 5, 15, 25, 30],
                        'max_features': ['sqrt'],
                        'oob_score': [True]
                    }
        gs = GridSearchCV(estimator=rf, param_grid=param_grid, scoring='accuracy', cv=3, n_jobs=-1)
        gs = gs.fit(x_train, y_train)
        print("结束!，最佳参数为：")
        print(gs.best_params_)
        print(f"最佳准确率为：{gs.best_score_}")
        return gs.best_params_


    @staticmethod
    def train(x_train,y_train,best_params):
        '''训练模型'''
         # 创建一个新的随机森林对象，放入最佳参数, 重新fit
        rf = RandomForestClassifier(criterion=best_params['criterion'], 
                                    n_estimators=best_params['n_estimators'],
                                    min_samples_split=best_params['min_samples_split'],
                                    min_samples_leaf=best_params['min_samples_leaf'],
                                    max_features=best_params['max_features'],
                                    max_depth=best_params['max_depth'],
                                    oob_score=best_params['oob_score'],
                                    random_state=1,
                                    n_jobs=-1)
        rf.fit(x_train, y_train)
        df1 = pd.DataFrame(x_train.columns,columns=['Variable'])
        df2 = pd.DataFrame(rf.feature_importances_,columns=['Importance'])
        variable_importances = pd.concat([df1,df2],axis=1).sort_values(by='Importance',ascending=False)
        print("训练结束，特征重要性如下：")
        print(variable_importances)
        return rf
  
