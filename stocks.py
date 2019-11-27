class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        profit = 0
        # -1 when holding nothing
        holding = -1
        # buy on first day when next day is higher
        if prices[0] < prices[1]:
            holding = prices[0]
        # stop before last day
        for i in range(1, len(prices) - 1):
            # buy when already sold or haven't bought
            if holding == -1:
                if prices[i+1] > prices[i]:
                    # buy here
                    holding = prices[i]
            # sell only when bought
            if holding != -1:
                if prices[i+1] < prices[i]:
                    # sell here
                    profit += prices[i] - holding   
                    holding = -1
        # sell holding on last day
        if holding != -1:
            profit += prices[len(prices) - 1] - holding 
        return profit