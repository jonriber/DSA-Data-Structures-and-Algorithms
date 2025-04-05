import unittest
from solution import minimumBribe

class TestMinimumBribe(unittest.TestCase):
    def test_case_1(self):
        with self.assertLogs() as log:
            minimumBribe([2, 1, 5, 3, 4])
            self.assertIn("3", log.output[0])

    def test_case_2(self):
        with self.assertLogs() as log:
            minimumBribe([2, 5, 1, 3, 4])
            self.assertIn("Too chaotic", log.output[0])

    def test_case_3(self):
        with self.assertLogs() as log:
            minimumBribe([5, 1, 2, 3, 7, 8, 6, 4])
            self.assertIn("Too chaotic", log.output[0])

    def test_case_4(self):
        with self.assertLogs() as log:
            minimumBribe([1, 2, 5, 3, 7, 8, 6, 4])
            self.assertIn("7", log.output[0])

if __name__ == '__main__':
    unittest.main()
