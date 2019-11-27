"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        numStr = ""
        neg = False
        # remove whitespace
        s = s.strip()
        if len(s) < 1:
            return 0
        if s[0] == '-':
            neg = True
        elif s[0] == '+':
            neg = False
        elif s[0].isnumeric():
            numStr += s[0]
        else: 
            return 0
        
        for i in range(1,len(s)):
            if s[i].isnumeric(): 
                numStr += s[i]
            else:
                break
                
        if len(numStr) < 1:
            return 0
        num = int(numStr)
        if neg:
            num *= -1
        # instructions specified that answers must be between 2^31 - and -2^31    
        if num > (1 << 31) - 1: 
            return (1 << 31) - 1
        elif num < -(1 << 31):
            return -(1 << 31)
        else:
            return num
            
            