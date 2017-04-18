import unittest
from odd_avg import Average

class TestAverage(unittest.TestCase):


    def test_odd_average_one_number(self):
        average = Average()
        average.odd_average()
        self.assertEqual(average.odd_average([3]), 3)


    def test_odd_average_empty(self):
        average = Average()
        self.assertEqual(average.odd_average([]), None)

    def test_odd_average(self):
        average = Average()
        self.assertEqual(average.odd_average([1,2,3]),2.0)



if __name__ == '__main__':
    unittest.main()