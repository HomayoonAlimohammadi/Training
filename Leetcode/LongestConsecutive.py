from typing import List


class Solution:

    def longestConsecutive(self, nums: List[int]) -> List[int]:

        set_nums = set(nums)

        longest = 0
        seen = set()

        for num in set_nums:
        
            if num in seen:
                continue
            
            seen.add(num)
        
            bigger = 0
            current = num
            set_bigger = set()
            while current + 1 in set_nums:
                bigger += 1
                current += 1
                set_bigger.add(current)

            smaller = 0
            current = num
            set_smaller = set()
            while current - 1 in set_nums:
                smaller += 1
                current -= 1
                set_smaller.add(current)

            if bigger >= smaller:
                total = bigger + 1
                seen |= set_bigger
            else:
                total = smaller + 1
                seen |= set_smaller

            if total >= longest:
                longest = total

        return longest


sol = Solution()
nums = [1,2,0,1]

print(sol.longestConsecutive(nums))



            

            
