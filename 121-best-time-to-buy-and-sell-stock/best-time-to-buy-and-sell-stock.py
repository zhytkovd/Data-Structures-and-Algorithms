class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res = 0
        l,r = 0,0
        n = len(prices)

        while r < n:
            if prices[r] < prices[l]:
                l = r
            else:
                res = max(res,prices[r]-prices[l])
            r += 1
        return res