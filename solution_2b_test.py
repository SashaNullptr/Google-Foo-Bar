import unittest
import os
import logging
import inspect

from solution_2b import *

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

def print_function_name(func):

    def wrapper(*args, **kwargs):

        print( "Running test ", func.__name__ )
        return func(*args, **kwargs)


    return wrapper

class SolutionTest( unittest.TestCase ):

    # @print_function_name
    # def test_fib(self):
    #
    #     fib_seq_1 = [ fibonacci_seq(n) for n in range(0, 1000) ]
    #     fib_seq_2 = [ fib(n) for n in range(0, 1000) ]
    #
    #     diff = [x for x in fib_seq_1 if x not in fib_seq_2]
    #     print( diff )
    #
    #     self.assertTrue( not diff )

    @print_function_name
    def test_basic_1(self):

        t = 10

        ans = get_diff( t )
        self.assertEqual( ans, 1 )

    @print_function_name
    def test_basic_2(self):

        t = 143

        ans = get_diff( t )
        self.assertEqual( ans, 3 )

    @print_function_name
    def test_singleton(self):

        t = 1

        ans = get_diff( t )
        self.assertEqual( ans, 0 )

    @print_function_name
    def test_power_2(self):

        t = 2**3

        ans = get_diff( t )
        self.assertEqual( ans, 1 )

    @print_function_name
    def test_power_2(self):

        t = 2**3

        ans = get_diff( t )
        self.assertEqual( ans, 1 )

if __name__ == '__main__':
    unittest.main()
