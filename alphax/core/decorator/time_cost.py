import functools
from datetime import time, datetime

from alphax.core.utils.time_util import TimeUtil


def time_cost(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 记录开始时间
        start_time = TimeUtil.millisecond(datetime.now())

        # 调用被装饰的函数
        result = func(*args, **kwargs)

        # 记录结束时间
        end_time = TimeUtil.millisecond(datetime.now())

        # 计算耗时
        elapsed_time = end_time - start_time

        if result is None:
            return elapsed_time
        else:
            return result, elapsed_time

    return wrapper
