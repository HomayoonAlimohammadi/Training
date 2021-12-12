from typing import List

def least_perm(self, l):
    result = []
    while len(l) != 0:
        result.append(min(l))
        l = l[:l.index(min(l))] + l[l.index(min(l))+1:]
    return result
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        for i in range(len(nums)-2, -1,-1):
            left = sorted(list(set(nums[i:])), reverse=True)
            ref = nums[i]
            if left.index(ref) - 1 >= 0:
                next_high = left[left.index(ref) - 1]
                j = nums.index(next_high)
                nums[i], nums[j] = nums[j], nums[i]
                nums = nums[:i+1] + self.least_perm(nums[i+1:])
                break
        else:
            nums = self.least_perm(nums)
        return nums
             
        
        
        
        
S = Solution()
nums = [3,2,1]
ans = S.nextPermutation(nums)
print(ans)