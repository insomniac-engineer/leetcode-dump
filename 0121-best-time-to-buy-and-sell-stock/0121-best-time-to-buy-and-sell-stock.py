class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_buy = prices[0]
        max_sell = 0
        profit = 0 
        for p in prices:
            min_buy = min(min_buy, p)
            profit = max(profit,p - min_buy)
            print(f"{min_buy} minbuy, {max_sell} maxsell")
        return profit