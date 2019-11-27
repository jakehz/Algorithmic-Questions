"""
Rotate a 2D matrix by 90 degrees
better than 82%
in place modification with space complexity of O(1)
"""
class Solution:
    
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # this portion does a typical matrix transform like you would see in linear alg.
        # I didn't import numpy for this bc thats cheating lol. but numpy does do transforms
        SIZE = len(matrix)
        start = 0
        for i in range(0,SIZE):
            for j in range(start,SIZE):
                if i != j:
                    # swap elements at opposite indices 
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            # increment start to avoid repeating combinations and swapping back to orig. position
            start += 1
        
        # increment column wise and swap each element of the column on opposite sides 
        # until we get to the middle or past that 
        begin = 0
        end = SIZE - 1
        while begin < end:  
            for i in range(0,SIZE):
                matrix[i][begin], matrix[i][end] = matrix[i][end], matrix[i][begin]  
            begin += 1
            end -= 1