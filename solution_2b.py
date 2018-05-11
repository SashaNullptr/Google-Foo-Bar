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

M = {0: 0, 1: 1}

def fibonacci_seq(n):
    """
    A relatively fast but precise version of the Fibonacci Sequence.

    Note that naive recusrive implementations were causing the test harness to time-out
    where as fast closed-form solutions such as:
        phi = (math.sqrt(5) + 1) / 2
        F_n = int(phi ** n / math.sqrt(5) + 0.5)

    are prone to numerical errors for large n, which also showed up in the test harness.

    This approach seems to strike a good balance between speed and precision.
    """

    if n < 0:
        raise IndexError( "Index is too small!" )
    if n in M:
        return M[n]
    M[n] = fibonacci_seq(n - 1) + fibonacci_seq(n - 2)
    return M[n]

def fibonacci_series( n ):
    # It can be shown that sum( F[n] ) = F[n+2] - 1
    return fibonacci_seq( n + 2 ) - 1

def fibonacci_series_offset( n ):
    # We need to apply an offset to take into account that the 0'th minion gets
    # 1 LAMB instead of 0.
    return fibonacci_series( n + 1 )

def power_2( n ):
    # Power of two, but adjusted so negative values of n return 0.
    # Usless because this term will only appear in a sum.

    if n < 0:
        return 0
    else:
        return 2**n

def power_2_series( n ):
    # It can be shown that sum( 2^n ) = 2^(n+1) - 1
    # Again we apply the rule that negative n is mapped to zero.

    if n < 0:
        return 0
    else:
        return 2**( n + 1 ) - 1

def twiddle_factor( n ):
    # Not Cooley-Tukey FFT factors, unfortunately.
    # This term is designed to handle the fringe-case when computing the most generous
    # way to hand out LAMBs.
    # That is, we could possibly have the case that
    # sum_(n) 2^n > #LAMBs but 2^(n-2) + 2^(n-1) + sum_(n-1) 2^n <= # LAMBs
    # That is we can effectively squeeze one extra minion in by applying the least
    # generous rule even if we are dealing with the most generous case.

    return power_2(n-2) + power_2(n-1)

def find_nearest_p2( max_value ):
    """
    Find the number of minions that could be paid out for number of LAMBs given
    by "max_value" using the "Most Generous" ( Power of 2 ) rule, with twiddle
    factor to account for the case where
    sum_(n) 2^n > #LAMBs but 2^(n-2) + 2^(n-1) + sum_(n-1) 2^n <= # LAMBs.
    """

    counter = 0

    while True:

        current_lambds = power_2_series( counter )

        if current_lambds < max_value:
            counter += 1
            continue

        elif current_lambds == max_value:
            return counter

        elif current_lambds > max_value:

            check = ( twiddle_factor(counter) + power_2_series(counter-1) )

            if check > max_value:
                return counter - 1 # Somtimes this needs to be counter?
            elif check == max_value:
                return counter
            else:
                return counter

def find_nearest_fib( max_value ):
    """
    Find the number of minions that could be paid out for a given number of LAMBs
    using the "Least Generous" ( Fibonacci Sum ) rule.
    """

    counter = 0

    while True:

        current_lambds = fibonacci_series_offset( counter )

        if current_lambds < max_value:
            counter += 1
            continue

        if current_lambds > max_value:
            return counter - 1
        elif current_lambds == max_value:
            return counter

def get_diff( max_value ):

    # Note we will always have # Minions Stingey > # Minions Generous so we don't
    # need to worry about negative values.
    return find_nearest_fib( max_value ) - find_nearest_p2( max_value )


# Our general startegy for this problem relies on identifying what series
# models the "Most Generous" and "Least Generous" cases. In the most generous case
# the sequence of minion pay-outs will look like the following:
#     [NULL]->[1]->[2]->[4]-> ... ->[2^(n-1)]->[2^n]
# This is simply a power-of-two sequence, so we want to find the smallest number n
# such that sum_{k=0}^{n} 2^n < #LAMBs.
#
# If we apply the least geneous rule we would expect our sequence to look like:
#     [NULL]->[1]->[1]->[2]->[3]-> ... ->[F_(n-1)]->[F_n]
# Which can recongnize right away as the Fibonacci sequence expect for F_0 = 0.
# So in this case we want to find the smallest n s.t. sum_{k=0}^{n} F_(n+1) < #LAMBs.
#
# Note that the way we compute this is slightly different -- we compute the smallest
# n in each case MINUS 1. This does not effect our final results since the difference
# between the most and least generous case absords this detail.

def answer(total_lambs):
    return get_diff( total_lambs )
