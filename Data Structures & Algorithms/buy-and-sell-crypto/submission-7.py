class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy = 0
        # sell = 1

        # max_profit = 0

        # while sell < len(prices):
        #     if prices[buy] < prices[sell]:
        #         max_profit = max(max_profit, prices[sell] - prices[buy])
        #     else:
        #         buy = sell
        #     sell += 1


        # return max_profit


        lowest_price = prices[0]
        best_profit = 0

        for p in prices[1:]:
            lowest_price = min(p, lowest_price)
            best_profit = max(best_profit, p - lowest_price)
        
        return best_profit

        