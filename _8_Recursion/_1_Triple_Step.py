# Jacob Wahl
# 4/6/21
#
# Problem 8.1 - A child is running up a staircase of n steps and can hop either
#               1, 2, or 3 steps at a time. Implement a method to count how
#               many possible ways the child can climb the stairs.

import sys


def count_ways(n):
    li = [0] * n
    return count_ways_recurse(n, li)


def count_ways_recurse(n, li):
    # Base Cases
    if n == 1:
        li[n-1] = 1
    elif n == 2:
        li[n-1] = 2
    elif n == 3:
        li[n-1] = 4
    # Recursive Case
    else:
        if li[n-1] == 0:
            ways = count_ways_recurse(
                n-1, li) + count_ways_recurse(n-2, li) + count_ways_recurse(n-3, li)
            li[n-1] = ways
    return li[n-1]


num = int(sys.argv[1])
print(count_ways(num))
