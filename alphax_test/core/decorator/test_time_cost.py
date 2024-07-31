import time
from unittest import TestCase

from alphax.core.decorator.time_cost import time_cost


class TestTimeCostDecorator(TestCase):
    def test_timeit_decorator(self):
        result, elapsed_time = TestTimeCostDecorator.my_function(5, 3)
        print(result)
        print(elapsed_time)
        assert result == 8
        assert elapsed_time >= 2000

    def test_timeit_warp(self):
        @time_cost
        def _do_something():
            time.sleep(2)
            return 1

        result, elapsed_time = _do_something()
        print(result)
        print(elapsed_time)
        assert result == 1
        assert elapsed_time >= 2000

    def test_empty_function(self):
        elapsed_time = TestTimeCostDecorator.empty_function()
        print(elapsed_time)
        assert elapsed_time >= 3000

    @staticmethod
    @time_cost
    def my_function(x, y):
        # 模拟一些计算
        time.sleep(2)
        return x + y

    @staticmethod
    @time_cost
    def empty_function():
        # 模拟一些计算
        time.sleep(3)
