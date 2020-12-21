import pytest
from pythoncode.calculator import Calculator


class TestCalc:
    def setup_class(self):
        self.cal = Calculator
        print("开始计算！每个类开始前输出！")

    def teardown_class(self):
        print("结束计算！每个类结束后输出！")

    def setup_method(self):
        print("每个方法前输出！！！")

    def teardown_method(self):
        print("每个方法结束后输出！！")

    @pytest.mark.parametrize("a,b,excepted", [(1, 2, 3), (100, 200, 300), (-1, -2, -3)], ids=["int", "bigint", "minus"])
    def test_add(self, a, b, excepted):
        assert excepted == self.cal.add(self, a, b)

    @pytest.mark.parametrize("a,b,excepted", [(1, 2, -1), (100, 200, -100), (-1, -2, 1)],
                             ids=["int", "bigint", "minus"])
    def test_sub(self, a, b, excepted):
        assert excepted == self.cal.sub(self, a, b)

    @pytest.mark.parametrize("a,b,excepted", [(1, 2, 2), (100, 200, 20000), (-1, -2, 2)],
                             ids=["int", "bigint", "minus"])
    def test_mult(self, a, b, excepted):
        assert excepted == self.cal.mult(self, a, b)

    @pytest.mark.parametrize("a,b,excepted", [(2, 1, 2), (200, 100, 2), (-4, -2, 2)], ids=["int", "bigint", "minus"])
    def test_devi(self, a, b, excepted):
        assert excepted == self.cal.devi(self, a, b)
