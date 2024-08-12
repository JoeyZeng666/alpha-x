import numpy as np


class MathUtil:

    # 计算斜率
    @staticmethod
    def slope(x: list, y: list) -> float:
        if len(x) != len(y):
            raise ValueError("The length of x and y must be the same")
        if len(x) < 2:
            raise ValueError("At least two points are needed")
        else:
            coeffs = np.polyfit(x, y, 1)
            slope = round(coeffs[0], 10)  # 保留10位小数
            return slope


