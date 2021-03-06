import yaml
from allurepython.demo1 import demo1
import pytest


class TestCalc:
    @pytest.mark.parametrize(("a","b"),yaml.safe_load(open("./data.yaml")))
    def test_add_1(self,a,b):
        try:
            self.demo1=demo1()
            result=self.demo1.add(a,b)
            print(result)
            assert (a+b)==result
        except ValueError as e:
            assert False
            print(e)
    @pytest.mark.parametrize(("a","b"),yaml.safe_load(open("./data.yaml")))
    def test_div_1(self,a,b):
        try:
            self.demo1 = demo1()
            result = self.demo1.div(a,b)
            print(result)
            assert (a/b) == result
        except ZeroDivisionError as e:
            assert False
            print(e)
        except ValueError as e:
            assert False
            print(e)

    @pytest.mark.parametrize(("a", "b"), yaml.safe_load(open("./data.yaml")))
    def test_mul_1(self, a, b):
        try:
            self.demo1 = demo1()
            result = self.demo1.mul(a, b)
            print(result)
            assert (a * b) == result
        except ValueError as e:
            assert False
            print(e)

    @pytest.mark.parametrize(("a", "b"), yaml.safe_load(open("./data.yaml")))
    def test_sub_1(self, a, b):
        try:
            self.demo1 = demo1()
            result = self.demo1.sub(a, b)
            print(result)
            assert (a * b) == result
        except ValueError as e:
            assert False
            print(e)

