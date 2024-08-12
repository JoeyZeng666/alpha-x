from unittest import TestCase

from alphax.core.utils.math_util import MathUtil


class TestMathUtil(TestCase):

    def test_debug_log(self):
        slope = MathUtil.slope([1, 2], [1, 2])
        assert slope == 1.0
        slope = MathUtil.slope([1, 2], [1, 0])
        assert slope == - 1.0
        slope = MathUtil.slope([1, 2], [1, -1])
        assert slope == - 2.0