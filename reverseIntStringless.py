"""Reversed a given integer. Doesn't use strings. O(n) worst case.

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            neg = True
            x *= -1
        else:
            neg = False
        
        num = 0
        while x != 0:
            num *= 10
            num += x % 10
            x = x // 10
        
        # ensures the number is less then 2^31 otherwise return 0
        if num > (1 << 31):
            return 0
        if neg:
            num *= -1
        return num