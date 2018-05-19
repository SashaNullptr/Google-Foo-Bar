# The Grandest Staircase Of Them All
# ==================================
#
# With her LAMBCHOP doomsday device finished, Commander Lambda is preparing for her debut on the galactic stage - but in order to make a grand entrance, she needs a grand staircase! As her personal assistant, you've been tasked with figuring out how to build the best staircase EVER.
#
# Lambda has given you an overview of the types of bricks available, plus a budget. You can buy different amounts of the different types of bricks (for example, 3 little pink bricks, or 5 blue lace bricks). Commander Lambda wants to know how many different types of staircases can be built with each amount of bricks, so she can pick the one with the most options.
#
# Each type of staircase should consist of 2 or more steps.  No two steps are allowed to be at the same height - each step must be lower than the previous one. All steps must contain at least one brick. A step's height is classified as the total amount of bricks that make up that step.
# For example, when N = 3, you have only 1 choice of how to build the staircase, with the first step having a height of 2 and the second step having a height of 1: (# indicates a brick)
#
# #
# ##
# 21
#
# When N = 4, you still only have 1 staircase choice:
#
# #
# #
# ##
# 31
#
# But when N = 5, there are two ways you can build a staircase from the given bricks. The two staircases can have heights (4, 1) or (3, 2), as shown below:
#
# #
# #
# #
# ##
# 41
#
# #
# ##
# ##
# 32
#
# Write a function called answer(n) that takes a positive integer n and returns the number of different staircases that can be built from exactly n bricks. n will always be at least 3 (so you can have a staircase at all), but no more than 200, because Commander Lambda's not made of money!
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
#     (int) n = 3
# Output:
#     (int) 1
#
# Inputs:
#     (int) n = 200
# Output:
#     (int) 487067745

# It would be remiss of me to not mention that this question seems to be
# a copy of Timus 1017: Staircases ( http://acm.timus.ru/problem.aspx?space=1&num=1017&locale=en ).
# I have inevitably benefitted from the myriad of people who have discussed solutions
# and written about their thoughts process regarding this question. I do not think my
# current solution, which uses memoization, would have been possible without observing
# the work of other people who tackled this problem.

def new_combinations_at_level( level, off_diagonal, n, memo ):
    """
    Count the number of -new- combinations of staircases possible at a particular level.
    """

    if( level == n ):
        # We've hit the max possible level
        return 1

    if( memo[level][off_diagonal] != -1 ):
        # We've already visited this element, so return the computed value.
        return memo[level][off_diagonal]

    # Mark this element as one we've previously visited.
    memo[level][off_diagonal] = 0

    for i in range( off_diagonal+1, n-level+1 ):
        memo[level][off_diagonal] += new_combinations_at_level( level+i, i, n, memo )

    return memo[level][off_diagonal]

def num_staircases( n ):
    """
    Count the number of staircases possible for a given number of bricks.
    """
    # Initialize the "matrix" of previously computed values.
    # We will use "-1" as a marker for "this state has not been visited previously".
    memo = [[-1 for x in range(n+1)] for y in range(n+1)]

    tot_staircases = 0

    for j in range (1,n):
        # Note we will store the total numbers of combinations per level on the
        # main diagonal of our "matrix" of previously computed values.
        tot_staircases += new_combinations_at_level(j,j,n,memo)

    return tot_staircases
