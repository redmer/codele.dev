#! python

import math
import typing as t
from itertools import islice


def window(seq: t.Sequence[t.Any], n=2):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result


def maxProduct(nums: list[int]):
    biggest_product = 0

    for window_size in range(1, len(nums) + 1):
        for w in window(nums, window_size):
            p = math.prod(w, start=1)
            print(f"{window_size=}, {p=} ({w=})")
            if p > biggest_product:
                biggest_product = p

    return biggest_product


print(maxProduct([2, 3, -2, 4]), "=? 6 ")
print(maxProduct([-2, 0, -1]), "=? 0 ")
print(maxProduct([-2, 3, -4]), "=? 24")
