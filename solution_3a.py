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


def largest_power_2(x):
    return 2**(x-1).bit_length()

def smallest_power_2(x):
    return 2**(x).bit_length()

def mod_2(x):
    return int( 2 * round( x / 2 ))

def minimum_steps(x):

    reduced_value = int(x)
    op_counter = 0

    while True:

        print( "Current value: ", reduced_value )

        nearest_mod_2 = mod_2( reduced_value )

        print( "Nearest number divisible by 2: ", nearest_mod_2 )

        multiple_2_steps = abs( reduced_value - nearest_mod_2 )

        print( "Had to move ", multiple_2_steps, " to reach nearest value mod 2.")

        op_counter += multiple_2_steps

        reduced_value = nearest_mod_2

        reduced_value /= 2

        if( reduced_value == 1 ):
            return op_counter + 1
        if( reduced_value == 0 ):
            return op_counter

        op_counter += 1
