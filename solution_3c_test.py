import unittest
import os
import logging
import inspect

from solution_3c import *

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

def print_function_name(func):

    def wrapper(*args, **kwargs):

        print( "Running test ", func.__name__ )
        return func(*args, **kwargs)


    return wrapper

class SolutionTest( unittest.TestCase ):

    @print_function_name
    def test_basic_1(self):
        s = 0
        l = 3
        ans = check_sum( s, l )

        self.assertEqual( ans, 2 )

    @print_function_name
    def test_basic_2(self):
        s = 17
        l = 4
        ans = check_sum( s, l )

        self.assertEqual( ans, 14 )

    @print_function_name
    def test_large(self):
        s = 0
        l = 400000
        ans = check_sum( s, l )

        self.assertTrue( True )

if __name__ == '__main__':
    unittest.main()
