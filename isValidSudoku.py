class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        SIZE = 9
        rowDict = {}
        colDict = {}
        boxDict = {}
        # check each row 
        for i in range(0,SIZE):
            for j in range(0, SIZE):
                if board[i][j] != '.':
                    # accessing of O(1) for dict
                    if board[i][j] in rowDict:
                        return False
                    else:
                        # assign arbitrary val 
                        rowDict[board[i][j]] = 1
                if board[j][i] != '.':
                    if board[j][i] in colDict:
                        return False
                    else: 
                        colDict[board[j][i]] = 1
                # generates a pattern that models the index of each box
                # eg. 00 01 02 10 11 12... 
                box = board[3*(i%3) + j//3][j%3 + 3*(i//3)]
                if box != '.':
                    if box in boxDict:
                        return False
                    else:
                        boxDict[box] = 1
            rowDict = {}
            colDict = {}
            boxDict = {}  
        return True