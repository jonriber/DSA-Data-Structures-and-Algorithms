import unittest
from two_sum_2 import two_sum

class TestTwoSum(unittest.TestCase):
  def test_two_sum(self):
    self.assertEqual(two_sum([2,7,11,15], 9), [1,2])
    self.assertEqual(two_sum([2,3,4], 6), [1,3])
    self.assertEqual(two_sum([-1,0], -1), [1,2])
    self.assertEqual(two_sum([5,25,75], 100), [2,3])
    self.assertEqual(two_sum([1,2,3,4,4,9,56,90], 8), [4,5])
    self.assertEqual(two_sum([1,2,3],7),[])
if __name__ == '__main__':
  unittest.main()