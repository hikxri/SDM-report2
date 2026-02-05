#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):
        # sample test cases
        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))

        # boundary value analysis (A)
        def test_A_below_min(self):
                self.assertEqual(-1, calc(0, 100))
        
        def test_A_min(self):
                self.assertEqual(100, calc(1, 100))

        def test_A_above_min(self):
                self.assertEqual(200, calc(2, 100))

        def test_A_nominal(self):
                self.assertEqual(50000, calc(500, 100))

        def test_A_below_max(self):
                self.assertEqual(99800, calc(998, 100))

        def test_A_max(self):
                self.assertEqual(99900, calc(999, 100))

        def test_A_above_max(self):
                self.assertEqual(-1, calc(1000, 100))

        # boundary value analysis (B)
        def test_B_below_min(self):
                self.assertEqual(-1, calc(100, 0))
        
        def test_B_min(self):
                self.assertEqual(100, calc(100, 1))

        def test_B_above_min(self):
                self.assertEqual(200, calc(100, 2))

        def test_B_nominal(self):
                self.assertEqual(50000, calc(100, 500))

        def test_B_below_max(self):
                self.assertEqual(99800, calc(100, 998))

        def test_B_max(self):
                self.assertEqual(99900, calc(100, 999))

        def test_B_above_max(self):
                self.assertEqual(-1, calc(100, 1000))

        # too small (A)
        def test_A_too_small(self):
                self.assertEqual(-1, calc(-5, 100))
        
        # too small (B)
        def test_B_too_small(self):
                self.assertEqual(-1, calc(100, -5))
        
        # too large (A)
        def test_A_too_large(self):
                self.assertEqual(-1, calc(1005, 100))
        
        # too large (B)
        def test_B_too_large(self):
                self.assertEqual(-1, calc(100, 1005))

        # invalid types (A)
        def test_A_string(self):
                self.assertEqual(-1, calc("abc", 100))
        
        def test_A_empty_string(self):
                self.assertEqual(-1, calc("", 100))

        def test_A_float(self):
                self.assertEqual(-1, calc(0.1, 100))
        
        def test_A_null(self):
                self.assertEqual(-1, calc(None, 100))
        
        # invalid types (B)
        def test_B_string(self):
                self.assertEqual(-1, calc(100, "abc"))
        
        def test_B_empty_string(self):
                self.assertEqual(-1, calc(100, ""))

        def test_B_float(self):
                self.assertEqual(-1, calc(100, 0.1))
        
        def test_B_null(self):
                self.assertEqual(-1, calc(100, None))