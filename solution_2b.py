# Lovely Lucky LAMBs
# ==================
#
# Being a henchman isn't all drudgery. Occasionally, when Commander Lambda is feeling generous, she'll hand out Lucky LAMBs (Lambda's All-purpose Money Bucks). Henchmen can use Lucky LAMBs to buy things like a second pair of socks, a pillow for their bunks, or even a third daily meal!
#
# However, actually passing out LAMBs isn't easy. Each henchman squad has a strict seniority ranking which must be respected - or else the henchmen will revolt and you'll all get demoted back to minions again!
#
# There are 4 key rules which you must follow in order to avoid a revolt:
#     1. The most junior henchman (with the least seniority) gets exactly 1 LAMB.  (There will always be at least 1 henchman on a team.)
#     2. A henchman will revolt if the person who ranks immediately above them gets more than double the number of LAMBs they do.
#     3. A henchman will revolt if the amount of LAMBs given to their next two subordinates combined is more than the number of LAMBs they get.  (Note that the two most junior henchmen won't have two subordinates, so this rule doesn't apply to them.  The 2nd most junior henchman would require at least as many LAMBs as the most junior henchman.)
#     4. You can always find more henchmen to pay - the Commander has plenty of employees.  If there are enough LAMBs left over such that another henchman could be added as the most senior while obeying the other rules, you must always add and pay that henchman.
#
# Note that you may not be able to hand out all the LAMBs. A single LAMB cannot be subdivided. That is, all henchmen must get a positive integer number of LAMBs.
#
# Write a function called answer(total_lambs), where total_lambs is the integer number of LAMBs in the handout you are trying to divide. It should return an integer which represents the difference between the minimum and maximum number of henchmen who can share the LAMBs (that is, being as generous as possible to those you pay and as stingy as possible, respectively) while still obeying all of the above rules to avoid a revolt.  For instance, if you had 10 LAMBs and were as generous as possible, you could only pay 3 henchmen (1, 2, and 4 LAMBs, in order of ascending seniority), whereas if you were as stingy as possible, you could pay 4 henchmen (1, 1, 2, and 3 LAMBs). Therefore, answer(10) should return 4-3 = 1.
#
# To keep things interesting, Commander Lambda varies the sizes of the Lucky LAMB payouts. You can expect total_lambs to always be a positive integer less than 1 billion (10 ^ 9).
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
#     (int) total_lambs = 10
# Output:
#     (int) 1
#
# Inputs:
#     (int) total_lambs = 143
# Output:
#     (int) 3

# def fibonacci_seq( n ):
#
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci_seq( n - 1 ) + fibonacci_seq( n - 2 )

from math import sqrt

def fibonacci_seq( n ):

    phi = (1 + sqrt(5)) / 2
    return int(phi ** n / sqrt(5) + 0.5)

def fibonacci_series( n ):
    # It can be shown that sum( F[n] ) = F[n+2] - 1
    return fibonacci_seq( n + 2 ) - 1

def fibonacci_series_offset( n ):
    # We need to apply an offset to take into account that the 0'th minion gets
    # 1 LAMB instead of 0.
    return fibonacci_series( n + 1 )

def power_2_series( n ):
    # It can be shown that sum( 2^n ) = 2^(n+1) - 1
    return 2**( n + 1 ) - 1

def find_nearest( series_func, max_value ):

    counter = 0

    while True:

        if series_func( counter ) > max_value:
            return counter - 1
        elif series_func( counter ) == max_value:
            return counter
        else:
            counter += 1

def get_diff( max_value ):

    # Note we will always have # Minions Stingey > # Minions Generous so we don't
    # need to worry about negative values.
    return find_nearest( fibonacci_series_offset, max_value ) - find_nearest( power_2_series, max_value )
