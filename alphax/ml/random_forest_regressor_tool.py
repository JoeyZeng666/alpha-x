import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

from alphax import core
from alphax.core.decorator.time_cost import time_cost


class RandomForestRegressorTool:
    _logger = core.get_logger(__name__)

    def __init__(self,name:str):
        self.best_params = None
        self.best_score = None
        self.ramdom_state = 42
        self.n_jobs = -1
        self._param_grid = {
            "n_estimators": [5, 25, 50, 75, 100],
            'max_features': ['sqrt', 'log2'],
            'max_depth': [10, 20, 30, 40, 50],
            'min_samples_split': [2, 5, 10, 16, 24],
            'min_samples_leaf': [1, 2, 4, 8, 12],
            'bootstrap': [True, False]
        }

    def find_best_params(self, x_train, y_train, param_grid=None, cv=5):
        self.best_params, used_time = self._do_find_best_params(x_train, y_train, param_grid, cv)
        self._logger.info(f"Finding best params used time: {used_time} ms")
        return self.best_params

    def train(self, x_train, y_train):
        model, cost_time = self._do_train(x_train, y_train)
        self._logger.info(f"Training model used time: {cost_time} ms")
        return model

    def save

    @time_cost
    def _do_train(self, x_train, y_train):
        self._logger.info("Training model with best params")
        model = RandomForestRegressor(random_state=self.ramdom_state, n_jobs=self.n_jobs)
        model.set_params(**self.best_params)
        model.fit(x_train, y_train)
        variable_importance = self._find_variable_importance(model, x_train)
        self._logger.info(f"Variable importance: {variable_importance}")
        return model

    @time_cost
    def _do_find_best_params(self, x_train, y_train, param_grid=None, cv=5):
        if param_grid is not None:
            self._param_grid = param_grid

        self._logger.info(f"Finding best params with param_grid: {self._param_grid}")
        model = RandomForestRegressor(random_state=self.ramdom_state, n_jobs=self.n_jobs)
        grid_search = GridSearchCV(model, param_grid, cv=cv, n_jobs=self.n_jobs)
        grid_search.fit(x_train, y_train)
        self.best_params = grid_search.best_params_
        self.best_score = grid_search.best_score_
        self._logger.info(f"Best score: {self.best_score}")
        self._logger.info(f"Best params: {self.best_params}")
        return grid_search.best_params_

    @staticmethod
    def _find_variable_importance(model, x_train):
        """ 查找变量的重要性，得到一个按重要性排序的列表"""
        variable = pd.DataFrame(x_train.columns, columns=['Variable'])
        importance = pd.DataFrame(model.feature_importances_, columns=['Importance'])
        variable_importance = pd.concat([variable, importance], axis=1).sort_values(by='Importance', ascending=False)
        return variable_importance



