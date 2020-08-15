import yaml
from allurepython.demo1 import demo1
import pytest


class TestCalc:
    def step(self):
        with open("./step.yaml") as f:
            return yaml.safe_load(f)

    @pytest.mark.aaa
    @pytest.mark.parametrize(("a","b"),yaml.safe_load(open("./data.yaml")))
    def calc_add_1(self,a,b):
        try:
            self.demo1=demo1()
            result=self.demo1.add(a,b)
            print(result)
            assert (a+b)==result
        except ValueError as e:
            assert False
            print(e)
    @pytest.mark.parametrize(("a","b"),yaml.safe_load(open("./data.yaml")))
    def calc_div_1(self,a,b):
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
    def calc_mul_1(self, a, b):
        try:
            self.demo1 = demo1()
            result = self.demo1.mul(a, b)
            print(result)
            assert (a * b) == result
        except ValueError as e:
            assert False
            print(e)

    @pytest.mark.parametrize(("a", "b"), yaml.safe_load(open("./data.yaml")))
    def calc_sub_1(self, a, b):
        try:
            self.demo1 = demo1()
            result = self.demo1.sub(a, b)
            print(result)
            assert (a - b) == result
        except ValueError as e:
            assert False
            print(e)

# if __name__ == '__main__':
#     pytest.main()