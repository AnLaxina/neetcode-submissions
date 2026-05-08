class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Using two pointers
        # Represent L: Buy stock (lowest price) R: Sell stock (highest "price")
        L, R = 0, 1
        max_profit = 0

        while R < len(prices):
            if prices[L] < prices[R]:
                profit = prices[R] - prices[L]
                max_profit = max(max_profit, profit)
            else:
                L = R
            
            R += 1
        return max_profit
