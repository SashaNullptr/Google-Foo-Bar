import unittest
import os
import logging
import inspect

from solution_2a import check_sum

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

def print_function_name(func):

    def wrapper(*args, **kwargs):

        print( "Running test ", func.__name__ )
        return func(*args, **kwargs)


    return wrapper

class SolutionTest( unittest.TestCase ):

    @print_function_name
    def test_basic(self):
        message = [ 4, 3, 5, 7, 8 ]
        t = 12

        ans = check_sum( message, t )
        self.assertEqual( ans, [0,2] )

    @print_function_name
    def test_repeated(self):
        message = [ 9, 1, 2, 3, 1, 1, 1, 2, 3 ]
        t = 6

        ans = check_sum( message, t )
        self.assertEqual( ans, [1,3] )

    @print_function_name
    def test_single_val(self):
        message = [ 1, 1, 15, 1 ]
        t = 15

        ans = check_sum( message, t )
        self.assertEqual( ans, [2,2] )

    @print_function_name
    def test_singleton(self):
        message = [ 1 ]
        t = 1

        ans = check_sum( message, t )
        self.assertEqual( ans, [0,0] )

    @print_function_name
    def test_whole_seq(self):
        message = [ 1, 2, 3, 4, 5 ]
        t = sum( message )

        ans = check_sum( message, t )
        self.assertEqual( ans, [0,4] )

    @print_function_name
    def test_not_in(self):
        message = [ 1, 2, 3, 4, 5 ]
        t = 45

        ans = check_sum( message, t )
        self.assertEqual( ans, [-1,-1] )

    @print_function_name
    def test_not_in_2(self):
        message = [ 1, 2, 3, 4 ]
        t = 15

        ans = check_sum( message, t )
        self.assertEqual( ans, [-1,-1] )

    @print_function_name
    def test_not_in_singleton(self):
        message = [ 1 ]
        t = 5

        ans = check_sum( message, t )
        self.assertEqual( ans, [-1,-1] )


if __name__ == '__main__':
    unittest.main()
