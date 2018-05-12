import unittest
import os
import logging
import inspect

from solution_3a import *

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
        t = "4"

        ans = minimum_steps( t )
        self.assertEqual( ans, 2 )

    @print_function_name
    def test_basic_2(self):
        t = "15"

        ans = minimum_steps( t )
        self.assertEqual( ans, 5 )


if __name__ == '__main__':
    unittest.main()
