from functools import lru_cache


class Solution:

    def climbStairs(self, n: int) -> int:

        def step(n_left, cache=None):
            
            if cache is None:
                cache = {}

            if n_left <= 0:
                if n_left == 0:
                    cache[0] = 1
                    return 1
                return 0

            if n_left in cache:
                return cache[n_left]
            
            ans = step(n_left - 1, cache) + step(n_left - 2, cache)
            cache[n_left] = ans
            return ans

        return step(n)
    
    def climbStairs_lru(self, n: int) -> int:

        @lru_cache
        def step(n_left):
            
            if n_left <= 0:
                if n_left == 0:
                    return 1
                return 0
            
            return step(n_left - 1) + step(n_left - 2)

        return step(n)

    def climbStairsDynamic(self, n: int) -> int:

        n1, n2 = 1, 1
        for i in range(n-1):
            n2, n1 = n1+n2, n2

        return n2


climb = Solution().climbStairsDynamic
print(climb(20))