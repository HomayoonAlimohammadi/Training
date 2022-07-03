from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        final = nums[0]+nums[1]+nums[2]
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                triple_sum = nums[i] + nums[j] + nums[k]
                
                if triple_sum == target:
                    return target
                
                if abs(triple_sum - target) < abs(final-target):
                    final = triple_sum
                
                if target - triple_sum < 0:
                    k -= 1
                else:
                    j += 1
        return final
    
S = Solution()

nums,target  = [0,2,1,-3], 1
S.threeSumClosest(nums,target)





############## My Code! (Time limit :( )


from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        final = float('inf')
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1, len(nums)):
                    triple_sum = nums[i]+nums[j]+nums[k]
                    if abs(triple_sum - target) <= abs(final-target):
                        final = triple_sum
                        
        return final
    
S = Solution()

nums,target  = [84,58,16,-6,-34,72,96,56,-31,45,-6,53,-79,-43,-92,-88,3,16,-6,33,84,-62,0,-29,-88,58,-14,21,51,61,1,17,26,57,-55,39,95,50,-16,25,85,65,-25,23,-82,-85,-99,-20,34,89,67,93,60,-21,-87,47,62,-1,63,-96,75,94,81,-29,56,69,-78,49,36,-80,49,-26,3,-29,52,-77,38,31,-49,-100,-44,-60,62,-24,45,-88,63,-36,7,-99,22,18,77,11,9,-63,44,6,-30,71,-68,0,37,29,-68,71,-35,83,4,-3,-3,-100,-88,-19,3,92,-47,33,-61,-96,-23,51,87,2,26,72,38,-42,77,-43,17,83,-59,82,45,-81,-41,-58,30,-85,-67,51,-27,63,-54,83,-6,68,81,-17,24,-59,96,59,-78,48,-100,-81,25,-28,-82,15,-76,86,65,-48,-67,-20,90,-89,-89,9,1,46,-67,71,-51,69,-2,14,89,-89,-1,85,-20,-57,75,28,22,-35,81],-48
S.threeSumClosest(nums,target)