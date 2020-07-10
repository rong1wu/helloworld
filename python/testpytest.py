from tesing.demo1 import demo1
import pytest

class TestCalc:
    def test_add_1(self):
        self.demo1=demo1()
        result=self.demo1.add(1,2)
        print(result)
        assert 3==result

    def test_div_1(self):
        self.demo1 = demo1()
        result = self.demo1.div(2, 2)
        print(result)
        assert 1 == result

if __name__=='__main__':
    pytest.main(['-vs','testPython::TestCalc::test_div_1'])