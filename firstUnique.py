"""Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters."""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # creates a count of each character and stores in a dictionary
        lettCount = {x: s.count(x) for x in set(s)}
        # returns the first character to have a count of 1
        # this is the first unique character
        for i,v in enumerate(s):
            if lettCount[v] == 1:
                return i
        return -1