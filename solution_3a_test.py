import unittest
import os
import logging
import inspect
from random import randint
from sys import setrecursionlimit
setrecursionlimit(1500)

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

    @print_function_name
    def test_null(self):
        t = "0"

        ans = minimum_steps( t )
        self.assertEqual( ans, 1 )

    @print_function_name
    def test_unitary(self):
        t = "1"

        ans = minimum_steps( t )
        self.assertEqual( ans, 0 )

    @print_function_name
    def test_factor(self):

        self.assertEqual( 0, count_factors_of_2( 15 ) )
        self.assertEqual( 1, count_factors_of_2( 14 ) )
        self.assertEqual( 3, count_factors_of_2( 2**3 ) )

    @print_function_name
    def test_large_1(self):

        t = str(2**64)
        ans = minimum_steps( t )

        self.assertEqual( 64, ans )

    @print_function_name
    def test_large_2(self):

        t = str(2**32 + 1)
        ans = minimum_steps( t )

        self.assertEqual( 33, ans )

    @print_function_name
    def test_large_3(self):

        t = str(self.__random_with_N_digits( 309 ))
        ans = minimum_steps( t )

        self.assertTrue( True )

    @print_function_name
    def test_str_cast(self):
        t = str(self.__random_with_N_digits( 309 ))
        test = str(int(t))

        self.assertEqual( t, test )

    def __random_with_N_digits(self, n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return randint(range_start, range_end)

if __name__ == '__main__':
    unittest.main()
