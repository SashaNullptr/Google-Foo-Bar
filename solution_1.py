# Problem description, must be implemented in Python 2.7 w/ standard library, more or less.
#
# Commander Lambda has had an incredibly successful week: she completed the first test run of her LAMBCHOP doomsday device, she captured six key members of the Bunny Rebellion, and she beat her personal high score in Tetris.
# To celebrate, she's ordered cake for everyone - even the lowliest of minions! But competition among minions is fierce, and if you don't cut exactly equal slices of cake for everyone, you'll get in big trouble.
#
# The cake is round, and decorated with M&Ms in a circle around the edge. But while the rest of the cake is uniform, the M&Ms are not: there are multiple colors, and every minion must get exactly the same sequence of M&Ms.
# Commander Lambda hates waste and will not tolerate any leftovers, so you also want to make sure you can serve the entire cake.
#
# To help you best cut the cake, you have turned the sequence of colors of the M&Ms on the cake into a string: each possible letter (between a and z) corresponds to a unique color, and the sequence of M&Ms is given clockwise (the decorations form a circle around the outer edge of the cake).
# Write a function called answer(s) that, given a non-empty string less than 200 characters in length describing the sequence of M&Ms, returns the maximum number of equal parts that can be cut from the cake without leaving any leftovers.
#
# Languages
# =========
# To provide a Python solution, edit solution.py
# To provide a Java solution, edit solution.java
#
# Test cases
# ==========
# Inputs: (string) s = "abccbaabccba"
# Output: (int) 2
#
# Inputs: (string) s = "abcabcabcabc"
# Output: (int) 4

def get_all_substrings( string ):
    """
    Build a list of all valid substrings of a given string.

    The continuity condition given in the problem implies that each string can
    be modeled as a repeated sequence of smaller strings. This function computes
    every possible substring formed by a given string and then filters based on
    the condition that the substring needs to "fit" in the original string by
    being repeated n times. That is the length of the string is evenly divisible
    by the length of the substring.
    """
    str_len = len( string )
    return [ string[i:j+1] for i in range(str_len) for j in range(i,str_len) if str_len%len(string[i:j+1]) == 0 ]

def string_shift( string, n ):
    """
    Shift all characters in a string over by n places, allowing wrapping.

    If a character had an index 'n' it will be assigned a new index n modulo length(string).
    """
    return string[n:] + string[:n]

def max_sequence_length( string ):
    """
    Compute the maximum number of times a substring can be repeated in a given string.

    We need to be careful to take into account the cylical nature of the problem.
    We not only need to consider the string in its original form, but every barrel
    shifted version of the string.

    That is we want to get the same answer if we altered the index of every
    character in our original string by char[n] <- char[(n+k)%len(string)] for any k.

    In this way we can view our function as applying to a group of chars modulo length(string)
    instead of a single string.
    """

    sub_strings = get_all_substrings( string )
    str_len = len(string)

    # We will use a running maximum sequence length that will we updates for each substring.
    max_seq_length = 0

    # Our general strategy will be to build a complete string by repeating a valid
    # substring enough times to get to the length of the original string.
    # For example if our original string was "abcabc" and our substring was
    # "abc" we would simply repeat it twice.
    for sub_string in sub_strings:

        sub_str_len = len( sub_string )

         # Compute how many times we need to repeat the substring to get to the
         # original string size. We already know that str_len % sub_str_len = 0
         # so there is no danger of an ambigous interger division.
        repeat_size = str_len//sub_str_len

        repeated_sub_string = ''.join([sub_string * repeat_size])

        current_seq_length = 0

        # We now need to handle the cylical problem mentioned earlier.
        # We will barrel shift the original string one step at a time a total
        # of length( string ) times. At each step we will see if our repeated
        # string matches the barrel shifted copy of the original string.
        # If we detect a match we know exactly how many times the repeated substring
        # appears, namely length(string)/length(substring).
        for idx in range( str_len ):
            wrapped_substring = string_shift( string, idx )

            if repeated_sub_string == wrapped_substring:
                current_seq_length = repeat_size
                break

        # Check to see if the number of repeated enteries is greater than our running maximum
        max_seq_length = current_seq_length if ( current_seq_length > max_seq_length ) else max_seq_length

    return max_seq_length

def answer( s ):
    return max_sequence_length( s )
