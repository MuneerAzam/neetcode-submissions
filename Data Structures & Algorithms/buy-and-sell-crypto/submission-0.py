class Solution:
    def maxProfit(self, prices: List[int]) -> int:       
        mi=float('inf')
        ma=0
        for i in range(len(prices)):
            if prices[i]<mi:
                mi=prices[i]
                continue
            x=prices[i]-mi
            if x>ma:
                ma=x
        return ma