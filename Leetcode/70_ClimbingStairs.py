from functools import lru_cache


class Solution:

    def climbStairs(self, n: int) -> int:

        @lru_cache
        def step(n_left, ways=0):
            
            if n_left <= 0:
                if n_left == 0:
                    ways += 1
                return ways
            
            return step(n_left - 1) + step(n_left - 2)

        ways = 0
        ways = step(n, ways)
        
        return ways


climb = Solution().climbStairs
print(climb(45))