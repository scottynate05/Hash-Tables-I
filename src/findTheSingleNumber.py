# You are given a non-empty array of integers.

# One element appears exactly once, with every other element appearing at least twice, perhaps more.

# Write a function that can find and return the element that appears exactly once.

# Example 1:

# Input: [1,1,2,1]
# Output: 2
# Example 2:

# Input: [1,2,1,2,1,2,80]
# Output: 80

from collections import defaultdict

def csFindTheSingleNumber(nums):
    tbl = defaultdict(int)
    for i in nums:
        tbl[i] += 1
    for i in tbl:
        if tbl[i] == 1:
            return i