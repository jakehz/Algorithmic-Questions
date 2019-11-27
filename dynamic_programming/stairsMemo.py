class Solution:
    def climbStairs(self, n: int) -> int:
        """Memoization method of dynamic programming"""
        table = [None]*(n+1)
        def helper(n, table):
            if table[n] == None:
                if n <= 3:
                    table[n] = n
                else:
                    table[n] = helper(n-1,table) + helper(n-2,table)
            return table[n]
        return helper(n,table)