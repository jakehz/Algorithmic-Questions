"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

 

"""
class Solution:
    def countAndSay(self, n: int) -> str:
        output = "1"
        for k in range(n-1):
            newOut = ""
            count = 1
            for i,v in enumerate(output):
                if (i+1) < len(output) and v == output[i+1]:
                    count += 1
                else:
                    newOut += str(count)
                    newOut += v
                    count = 1
            output = newOut
        return output

                    
            