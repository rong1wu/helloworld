import unittest

from tesing import demo1


class TestCal(unittest.TestCase):
    def test_add_1(self):
        self.demeo1=demo1()
        result=self.demo1.add(1,2)
        print(result)
        self.assertEqual(3,result)