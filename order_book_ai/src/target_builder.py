import datetime
import sys
import pandas as pd
import numpy as np
import sklearn


class TargetBuilder:

    @staticmethod
    def build(data):
        gap = -60
        feature_price = data["price"].shift(gap)
        rise_percent = round((feature_price - data["price"]) / data["price"], 4)
        data.insert(0, "target", (rise_percent > 0.003).astype(int))
        data.loc[data.index[gap:], "target"] = np.nan
        return data
