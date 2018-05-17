import unittest
import os
import logging
import inspect

from solution_3b import *

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
        t = 3
        ans = num_staircases( t )

        self.assertEqual( ans, 1 )

    @print_function_name
    def test_basic_2(self):
        t = 5
        ans = num_staircases( t )

        self.assertEqual( ans, 2 )

    def test_basic_3(self):
        t = 200
        ans = num_staircases( t )

        self.assertEqual( ans,487067745 )

if __name__ == '__main__':
    unittest.main()
