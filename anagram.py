"""Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # create a dictionary of each letter and amount of instances
        # i've found that this way is somehow actually faster than using the Collections library's count function
        # for each unique letter x in the string s, make dict entry with key x and value count of x in s 
        lettDict = {x:s.count(x) for x in set(s)}
        for v in t:
            # if the letter of the second word exists in the other word, and the instances of it are greater than 0
            # the accessing of that dictionary is O(1) so it's also super fast
            if v in lettDict and lettDict[v] > 0:
                # subtract one from amount of instances
                # so we know the letter in the second string matches one in the first
                lettDict[v] -= 1
            else:
                return False
        return True
                