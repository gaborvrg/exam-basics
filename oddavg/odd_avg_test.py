import unittest
import odd_avg


def test_get_apple(self):
    apple = Apple()
    apple.get_apple()
    self.assertEqual(apple.get_apple(),'apple')


def test_sum(self):
    summary = Apple()
    self.assertEqual(summary.sum([1,2,3]), 6)

def test_sum_empty(self):
    summary = Apple()
    self.assertEqual(summary.sum([]), 0)

def test_sum_one_element(self):
    summary = Apple()
    self.assertEqual(summary.sum([2]), 2)