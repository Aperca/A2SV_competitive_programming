class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
       pre_fix=[nums[0]]
       for i in range(1,len(nums)):
            pre_fix.append(pre_fix[-1]+nums[i])
       return pre_fix
