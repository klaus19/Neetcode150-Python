class Solution(object):

    def profit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit


if __name__ == '__main__':
    lt = [7, 1, 5, 3, 6, 4]
    print(Solution().profit(lt))
