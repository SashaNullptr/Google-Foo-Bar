import unittest
import os
import logging

import solution

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

class SolutionTest( unittest.TestCase ):

    def test_substring(self):
        test_string = "abcabcabcabc"
        sub_strs=solution.get_all_substrings( test_string )

        # print( sub_strs )
        self.assertTrue(True)

    def test_basic_1(self):
        print( "Basic test 1.")
        test_string = "abcabcabcabc"
        max_seq = solution.max_sequence_length( test_string )

        print( max_seq )
        self.assertTrue(max_seq==4)

    def test_basic_2(self):
        print( "Basic test 2.")
        test_string = "abccbaabccba"
        max_seq = solution.max_sequence_length( test_string )

        print( max_seq )
        self.assertTrue(max_seq==2)

    def test_cyclic(self):
        print( "Cyclic test")
        test_string = solution.string_shift("abcabcabcabc", 1)
        print( test_string )
        max_seq = solution.max_sequence_length( test_string )

        print( max_seq )
        self.assertTrue(max_seq==4)

    def test_unique(self):
        print( "Non-repeating test")
        test_string = "abcdefg"
        max_seq = solution.max_sequence_length( test_string )

        print( max_seq )
        self.assertTrue(max_seq==1)

    def test_long(self):
        print( "Long test")
        test_string = ''.join(["abc" * 50])
        max_seq = solution.max_sequence_length( test_string )

        print( max_seq )
        self.assertTrue(max_seq==50)

if __name__ == '__main__':
    unittest.main()
