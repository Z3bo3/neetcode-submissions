class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) > 1:
            profit = 0
            lowestbuy = prices[0]
            for i in prices[1:]:
                if i < lowestbuy:
                    lowestbuy = i
                if (i - lowestbuy) > profit:
                    profit = i - lowestbuy
            return profit
        return 0

        