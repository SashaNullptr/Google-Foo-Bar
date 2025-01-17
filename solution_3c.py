# Queue To Do
# ===========
#
# You're almost ready to make your move to destroy the LAMBCHOP doomsday device, but the security checkpoints that guard the underlying systems of the LAMBCHOP are going to be a problem. You were able to take one down without tripping any alarms, which is great! Except that as Commander Lambda's assistant, you've learned that the checkpoints are about to come under automated review, which means that your sabotage will be discovered and your cover blown - unless you can trick the automated review system.
#
# To trick the system, you'll need to write a program to return the same security checksum that the guards would have after they would have checked all the workers through. Fortunately, Commander Lambda's desire for efficiency won't allow for hours-long lines, so the checkpoint guards have found ways to quicken the pass-through rate. Instead of checking each and every worker coming through, the guards instead go over everyone in line while noting their security IDs, then allow the line to fill back up. Once they've done that they go over the line again, this time leaving off the last worker. They continue doing this, leaving off one more worker from the line each time but recording the security IDs of those they do check, until they skip the entire line, at which point they XOR the IDs of all the workers they noted into a checksum and then take off for lunch. Fortunately, the workers' orderly nature causes them to always line up in numerical order without any gaps.
#
# For example, if the first worker in line has ID 0 and the security checkpoint line holds three workers, the process would look like this:
# 0 1 2 /
# 3 4 / 5
# 6 / 7 8
# where the guards' XOR (^) checksum is 0^1^2^3^4^6 == 2.
#
# Likewise, if the first worker has ID 17 and the checkpoint holds four workers, the process would look like:
# 17 18 19 20 /
# 21 22 23 / 24
# 25 26 / 27 28
# 29 / 30 31 32
# which produces the checksum 17^18^19^20^21^22^23^25^26^29 == 14.
#
# All worker IDs (including the first worker) are between 0 and 2000000000 inclusive, and the checkpoint line will always be at least 1 worker long.
#
# With this information, write a function answer(start, length) that will cover for the missing security checkpoint by outputting the same checksum the guards would normally submit before lunch. You have just enough time to find out the ID of the first worker to be checked (start) and the length of the line (length) before the automatic review occurs, so your program must generate the proper checksum with just those two values.
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
#     (int) start = 0
#     (int) length = 3
# Output:
#     (int) 2
#
# Inputs:
#     (int) start = 17
#     (int) length = 4
# Output:
#     (int) 14

def XOR_1_to_n( n ):
    """
    Compute the exclusive or of all elements in the sequence (1,2,..,n)

    This function relies on the fact that the following holds for any n.

    1^2^...^n = f(n mod 4) for ^ the XOR operator and
    f(n) = {
            n, n = 0
            1, n = 1
            n+1, n = 2
            0, n = 3
            }
    """
    remainder = [n,1,n+1,0]
    return remainder[n%4]

def XOR_int_seq( a, b ):
    """
    Compute the exclusive or off all elements in the sequence (a,a+1,...,b-1,b)
    for a >= 1 and b > a.

    Let a ^ b be the exclusive or of integers a and b.
    Define ( a ^ a+1 ^ .. ^ b-1 ^ b ) = S
    Define ( 1 ^ 2 ^ .. ^ a ) = A
    Define ( 1 ^ 2 ^ ... ^ b ) = B

    Then B = (1 ^ 2 ^ ... ^ b )
           = ( 1 ^ 2 ^ ,,, ^ a-1 ) ^ ( a ^ a+1 ^ ... ^ b ) ( since a < b )
           = XOR_1_to_n( a-1 ) ^ ( a ^ ... ^ b ) ( definition of XOR_1_to_n )
           = XOR_1_to_n( a-1 ) ^ S ( definition of S )
           => S = XOR_1_to_n(b) ^ XOR_1_to_n(a-1) ( by commutativity ).
    Then
    """
    return XOR_1_to_n(b)^XOR_1_to_n(a-1)

def queue_check_sum( start, queue_size, level ):
    """
    Compute the checksum for a particular queue.

    We define the queue "level" to be zero for the first queue, one for the second etc.
    It is easy enough to show that the queue at the n'th level will take on values from
    [ s + l*q_s, (s+l*q_s)+(q_s-l) ] for s the starting number, l the current level,
    and q_s the size of each queue.
    """

    queue_start = start + level*queue_size
    queue_end = queue_start + (queue_size - level)


    if( queue_start == 0 ):
        # Compensate for the condition that XOR_1_to_n must start at 1.
        return 0^XOR_int_seq( queue_start+1, queue_end-1 )
    else:
        return XOR_int_seq( queue_start, queue_end-1 )

def check_sum( start, length ):
    """
    Compute the checksum over all queues starting with security ID "start" and
    with a queue size of "length".
    """

    checksum = queue_check_sum( start, length, 0 )

    level = 1
    while ( length - level ) > 0:
        checksum ^= queue_check_sum( start, length, level )
        level += 1

    return checksum
