"""
    find substring in string
    needle is substring haystack is string

    passed all test cases except the last (timed out)
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # solution but timed out on last test case
        # O(N^2) 
        foundWord = ""
        if needle == "":
            return 0
        for i,v in enumerate(haystack):
            if v == needle[0]:
                for j in range(i,i + len(needle)):
                    if not j >= len(haystack) and needle[j - i] == haystack[j]:
                            foundWord += haystack[j]
                    else: 
                        break
                if foundWord == needle:
                    return i
                else:
                    foundWord = ""
                                         
        return -1