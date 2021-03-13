import unittest
import math
from app import Application
class Test(unittest.TestCase):
    def setUp(self):
        self.obj = Application()
    def test_int1(self):
        assert self.obj.add(self.obj.mul(2,3),self.obj.sub(self.obj.div(2,2),1)) , 7
    def test_int2(self):
        assert self.obj.div(self.obj.add(self.obj.mul(2,1),3),self.obj.sub(6,1)) , 1
    def test_int3(self):
        assert self.obj.log(self.obj.add(self.obj.sqrt(1),self.obj.exp(3,3))) , 1
if __name__ == "__main__":
    unittest.main()
