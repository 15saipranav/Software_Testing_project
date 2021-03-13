import unittest
import math
from app import Application
class Test(unittest.TestCase):
    def setUp(self):
        self.obj = Application()
    def test_sum(self):
        assert self.obj.add(3,1) , 4
    def test_diff(self):
        assert self.obj.sub(4,1) , 3
    def test_mul(self):
        assert self.obj.mul(4,3) , 12
    def test_div(self):
        assert self.obj.div(4,2) , 2
    def test_sqrt(self):
        assert self.obj.sqrt(9) , 3
    def test_log(self):
        assert self.obj.log(10) , 1
    def test_exp(self):
        assert  self.obj.exp(3,3) , 9

if __name__ == "__main__":
    unittest.main()
