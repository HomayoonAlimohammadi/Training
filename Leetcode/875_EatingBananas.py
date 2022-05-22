from typing import List


class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        piles_sorted = sorted(piles)
        all_k = range(1, piles_sorted[-1]+1)
        start, end = 0, len(all_k)
        while True:


            hops = 0
            index = (start + end) // 2
            corr = (start, end)
            k = all_k[index]
            for pile in piles:
                if pile / k == pile // k:
                    hops += pile // k
                else:
                    hops += pile // k + 1

            # print(f'{k=}, {hops=}')
            # print(f'{start=}, {end=}, {index=}')
            # print()
            if hops <= h:
                end = index
            else:
                start = index

            if corr == (start, end):
                break
        
        final_range = range(all_k[start], all_k[end])
        index = 0
        while final_range:
            
            hops = 0
            k = final_range[index]
            for pile in piles:
                if pile / k == pile // k:
                    hops += pile // k
                else:
                    hops += pile // k + 1

            if hops > h:
                index += 1
                if index == len(final_range):
                    return all_k[end]
            else:
                break

        return k

            
func = Solution().minEatingSpeed
piles = [312884470]

h = 312884469
print(func(piles, h))
