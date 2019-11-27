"""Better than 98% 
    here I utilized the python set data type to easily eliminate duplicates and remove (pop) chars when I was done

    INSTRUCTIONS:
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        match = ""
        lettSet = set()
        # if empty array return empty string
        if not strs:
            return match
        # only interate through to the length of the smallest string (min)
        for i in range(len(min(strs))):
            for v in strs:
                lettSet.add(v[i])
            if len(lettSet) > 1:
                return match
            else:
                match += lettSet.pop()
            
        return match
            