import yaml
from allurepython.demo1 import demo1
import pytest


class TestCalc:
    @pytest.mark.parametrize(('a','b'),[(1,2),(2,1),(0,0),(-1,-2),(-2,-1)])
    def test_add_1(self,a,b):
        self.demo1=demo1()
        result=self.demo1.add(a,b)
        print(result)
        assert (a+b)==result
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






if __name__=='__main__':
    pytest.main(['-vs','testPython::TestCalc::test_div_1'])