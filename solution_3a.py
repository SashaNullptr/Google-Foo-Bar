# Fuel Injection Perfection
# =========================
#
# Commander Lambda has asked for your help to refine the automatic quantum antimatter fuel injection system for her LAMBCHOP doomsday device. It's a great chance for you to get a closer look at the LAMBCHOP - and maybe sneak in a bit of sabotage while you're at it - so you took the job gladly.
#
# Quantum antimatter fuel comes in small pellets, which is convenient since the many moving parts of the LAMBCHOP each need to be fed fuel one pellet at a time. However, minions dump pellets in bulk into the fuel intake. You need to figure out the most efficient way to sort and shift the pellets down to a single pellet at a time.
#
# The fuel control mechanisms have three operations:
#
# 1) Add one fuel pellet
# 2) Remove one fuel pellet
# 3) Divide the entire group of fuel pellets by 2 (due to the destructive energy released when a quantum antimatter pellet is cut in half, the safety controls will only allow this to happen if there is an even number of pellets)
#
# Write a function called answer(n) which takes a positive integer as a string and returns the minimum number of operations needed to transform the number of pellets to 1. The fuel intake control panel can only display a number up to 309 digits long, so there won't ever be more pellets than you can express in that many digits.
#
# For example:
# answer(4) returns 2: 4 -> 2 -> 1
# answer(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1
#
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
#     (string) n = "4"
# Output:
#     (int) 2
#
# Inputs:
#     (string) n = "15"
# Output:
#     (int) 5
#

# We need to increase the recursion depth so we don't error out on large inputs.
from sys import setrecursionlimit
setrecursionlimit(1500)

def count_factors_of_2( n ):
    """
    Count the number of times n is divisible by 2.
    """

    reduced_value = n
    counter = 0

    while reduced_value % 2 == 0 and reduced_value != 0:
            reduced_value = reduced_value//2
            counter += 1

    return counter

def most_factors( n ):
    """
    For an odd number n, identify the closest even number with the most factors of 2.
    """

    num_factors_2_up = count_factors_of_2( n + 1 )
    num_factors_2_down = count_factors_of_2( n - 1 )

    if num_factors_2_up > num_factors_2_down:
        return n + 1
    elif num_factors_2_up < num_factors_2_down:
        return n - 1
    elif num_factors_2_up == num_factors_2_down:
        return n - 1

def minimum_steps( n ):
    """
    Find the minimum number of operations to transform an integer n into 1.

    The operations that can be performed are:
        * Divide by 2
        * Add 1
        * Subtract 1

    We know that dividing by two is the "cheapest" of our three possible options,
    so we would like to do it as often as possible.

    With this in mind we will reduce our number recursively until we hit 1
    trying to divide by 2 as often as we can.

    Our procedure will go as follows:

        * For each step check to see if our number is even or odd.
        * If it's even, divide it by two ( the "cheap" option )
        * If it's odd check the number plus 1 and minus 1. Pick the option with the most
            factors of 2. If both have the same number of factors, pick option closest to 1 ( n - 1 ).
        * Add one to the total operations count and recurse
        * Stop if the we hit our target of 1.
    """

    # Pathological case when n = 0 to begin with.
    if n == 0:
        return 1

    # Our non-pathological base-case.
    if n == 1:
        return 0

    # We shouldn't need this base care, but the algorithm as written struggles
    # when it gets to three. For the time being we can help it out and manually
    # return the number of operations we need to get to 1 from 3.
    if n == 3:
        return 2

    if n % 2 == 0: # Even
        return 1 + minimum_steps( n // 2 )
    else: # Odd
        return 1 + minimum_steps( most_factors( n ) )

def answer(n):

    # Luckily for us Python has arbitrary precision Integers by default and we
    # will never have the case where we fail to cast a string to and int. At least
    # for # bits <= 309.
    x = int(n)
    return minimum_steps(x)
