class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        write=0
        for num in nums:
            if num != 0:
                nums[write]=num
                write += 1
        while write < len(nums):
            nums[write]=0
            write += 1
        return nums
