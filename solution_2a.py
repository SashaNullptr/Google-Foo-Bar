# Numbers Station Coded Messages
# ==============================
#
# When you went undercover in Commander Lambda's organization, you set up a coded messaging system with Bunny Headquarters to allow them to send you important mission updates. Now that you're here and promoted to Henchman, you need to make sure you can receive those messages - but since you need to sneak them past Commander Lambda's spies, it won't be easy!
#
# Bunny HQ has secretly taken control of two of the galaxy's more obscure numbers stations, and will use them to broadcast lists of numbers. They've given you a numerical key, and their messages will be encrypted within the first sequence of numbers that adds up to that key within any given list of numbers.
#
# Given a non-empty list of positive integers l and a target positive integer t, write a function answer(l, t) which verifies if there is at least one consecutive sequence of positive integers within the list l (i.e. a contiguous sub-list) that can be summed up to the given target positive integer t (the key) and returns the lexicographically smallest list containing the smallest start and end indexes where this sequence can be found, or returns the array [-1, -1] in the case that there is no such sequence (to throw off Lambda's spies, not all number broadcasts will contain a coded message).
#
# For example, given the broadcast list l as [4, 3, 5, 7, 8] and the key t as 12, the function answer(l, t) would return the list [0, 2] because the list l contains the sub-list [4, 3, 5] starting at index 0 and ending at index 2, for which 4 + 3 + 5 = 12, even though there is a shorter sequence that happens later in the list (5 + 7). On the other hand, given the list l as [1, 2, 3, 4] and the key t as 15, the function answer(l, t) would return [-1, -1] because there is no sub-list of list l that can be summed up to the given target value t = 15.
#
# To help you identify the coded broadcasts, Bunny HQ has agreed to the following standards:
#
# - Each list l will contain at least 1 element but never more than 100.
# - Each element of l will be between 1 and 100.
# - t will be a positive integer, not exceeding 250.
# - The first element of the list l has index 0.
# - For the list returned by answer(l, t), the start index must be equal or smaller than the end index.
#
# Remember, to throw off Lambda's spies, Bunny HQ might include more than one contiguous sublist of a number broadcast that can be summed up to the key. You know that the message will always be hidden in the first sublist that sums up to the key, so answer(l, t) should only return that sublist.
#
# Languages
# =========
#
# To provide a Python solution, edit solution.py
# To provide a Java solution, edit solution.java
#
# Test cases
# ==========
#
# Inputs:
#     (int list) l = [4, 3, 10, 2, 8]
#     (int) t = 12
# Output:
#     (int list) [2, 3]
#
# Inputs:
#     (int list) l = [1, 2, 3, 4]
#     (int) t = 15
# Output:
#     (int list) [-1, -1]
#
# Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.

def check_sum( message, magic_value ):
    """
    Find the first continous substring of 'message' with sum(sub_string) = magic_value.

    This function will return the starting and ending indices of the first appropiate substring, if
    it is present.

    If there is no such substring present this function will return [-1,-1].

    If multiple sublists would fufill the criteria this function will return the substring with the smallest
    lexicographically sorted indices from among all matching sublists.
    """

    n = len( message )

    # Our strategy here is to look at all elements to the right of index 'i'
    # and the form all possible continous sublists starting at 'i' and ending
    # with at most 'n'. Note we will never have to the left of 'i' due to the
    # lexicographic sort condition since we know if the appropiate list does
    # not have a leading index 'i' it will not have a leading index smaller than 'i'.

    for i in range( 0, n ):

        for j in range( i, n ):
            # The continuity condition given in the problem means forming all possible
            # sublists only requires starting at the single element located at 'i' and
            # appending the element to the immediate right until we have a sublist ranging
            # between 'i' and 'n'.
            #
            # For each sublist formed in this way we check to see if the sum of all
            # the elements present is equal to 'magic_value' and immediately return
            # the first time this condition is meet. We can do this since we are iterating
            # from left to right and the first match we find will be the
            # one with the smallest leading index. We do not have to worry about the trailing
            # index since each number in our sequence is strictly positive, meaning
            # we can never have sum(list[i:n]) == sum(list[i:n+k]) for any positive integer k.

            sub_list = message[ i:j+1 ]

            if sum( sub_list ) == magic_value:
                # If we have a matching value it is straight forward to compute the
                # leading index which is just our position in the current message, and
                # the trailing index which is len(sub_list) to the right of the
                # leading index.
                start = i
                end = i + ( len( sub_list ) - 1 )

                return [ start, end ]

    # If we haven't returned by this point we are assured that there is no appropiate
    # sublist in the main list, and we return a failure value of [-1,-1].
    return [ -1, -1 ]
