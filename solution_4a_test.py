import unittest
import os
import logging
import inspect

from solution_4a import *

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

def print_function_name(func):

    def wrapper(*args, **kwargs):

        print( "Running test ", func.__name__ )
        return func(*args, **kwargs)


    return wrapper

class SolutionTest( unittest.TestCase ):


    @print_function_name
    def test_basic_0(self):

        times = [
                  [0, 2, 2, 2, -1],
                  [9, 0, 2, 2, -1],
                  [9, 3, 0, 2, -1],
                  [9, 3, 2, 0, -1],
                  [9, 3, 2, 2,  0]
                ]

        time_limit = 1

        ts = TimeScenario( times, time_limit )

        self.assertEqual( ts(), [1,2] )

    # @print_function_name
    # def test_basic_1(self):
    #
    #     times = [[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]]
    #     time_limit = 3
    #
    #     ts = TimeScenario( times, time_limit )
    #
    #     self.assertEqual( ts(), [0,1] )
    #
    # @print_function_name
    # def test_basic_2(self):
    #
    #     times = [[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]]
    #     time_limit = 1
    #
    #     ts = TimeScenario( times, time_limit )
    #
    #     self.assertEqual( ts(), [1,2] )

if __name__ == '__main__':
    unittest.main()
