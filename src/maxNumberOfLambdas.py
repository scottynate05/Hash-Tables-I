# Given a string text, you need to use the characters of text to form as many instances of the word "lambda" as possible.

# You can use each character in text at most once.

# Write a function that returns the maximum number of instances of "lambda" that can be formed.

# Example 1:

# Input: text = "mbxcdatlas"
# Output: 1
# Example 2:

# Input: text = "lalaaxcmbdtsumbdav"
# Output: 2
# Example 3:

# Input: text = "sctlamb"
# Output: 0

from collections import Counter

def csMaxNumberOfLambdas(text):
    cnt = Counter(text)
    cntLambdas = Counter('lambda')
    return min([cnt[c] // cntLambdas[c] for c in cntLambdas])