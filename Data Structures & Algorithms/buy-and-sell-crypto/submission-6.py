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

        for i in range(len(prices)):
            lowest_price = min(prices[i], lowest_price)
            best_profit = max(best_profit, prices[i] - lowest_price)
        
        return best_profit

        