class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=0
        for i in range (len(prices)):
            if max(prices[i:len(prices)])>prices[i]:
                maxi=max(max(prices[i:len(prices)])-prices[i],maxi)
        return maxi
        