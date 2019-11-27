"""Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.

"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # where our palindrome of lowercase letters only goes
        plain = ""
        for l in s:
            # utilizing pythons built in alphanumeric identifier to make our palindrome only lowercase letters
            if l.isalnum():
                plain += l.lower()

        # compare beginning to end at the same time and move to the middle
        start = 0
        end = len(plain) - 1
        while start < end:
            if  plain[start] != plain[end]:
                return False
            start += 1
            end -= 1
        return True