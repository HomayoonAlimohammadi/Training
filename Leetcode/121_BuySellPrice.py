from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) == 0: return 0
        l, r = 0, 1
        maxProf = 0
        while r < len(prices):
            buy = prices[l]
            sell = prices[r]
            if sell - buy < 0:
                l = r
                r += 1
                continue

            elif (sell - buy) > maxProf:
                print(l, r)
                maxProf = sell - buy

            r += 1

        return maxProf


sol = Solution()
prices = [7, 1, 5, 3, 6, 4]
prices_2 = [2,1,4]
print(sol.maxProfit(prices_2))