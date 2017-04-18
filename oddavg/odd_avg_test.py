import unittest
from odd_avg import Average

class TestAverage(unittest.TestCase):

 
    def test_odd_average_one_even_number(self): # unittest for input only one number if it is even
        average = Average()
        average.odd_average()
        self.assertEqual(average.odd_average([2]), None)

    def test_odd_average_one_number(self): # unittest for input only one number if it is odd
        average = Average()
        average.odd_average()
        self.assertEqual(average.odd_average([3]), 3)


    def test_odd_average_empty(self): # unittest for empty list
        average = Average()
        self.assertEqual(average.odd_average([]), None)

    def test_odd_average(self): # basic unittest
        average = Average()
        self.assertEqual(average.odd_average([1,2,3]),2.0)



if __name__ == '__main__':
    unittest.main()