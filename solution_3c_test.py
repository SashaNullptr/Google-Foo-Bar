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
    def test_queue(self):
        s = 17
        l = 4

        self.assertEqual( generate_queue( s, l, 0 ), [17,18,19,20] )
        self.assertEqual( generate_queue( s, l, 1 ), [21,22,23] )
        self.assertEqual( generate_queue( s, l, 2 ), [25,26] )
        self.assertEqual( generate_queue( s, l, 3 ), [29] )
        self.assertEqual( generate_queue( s, l, 4 ), [] )

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

if __name__ == '__main__':
    unittest.main()
