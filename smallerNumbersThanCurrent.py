class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        out = []
        sorted_nums = sorted(nums)  
        n = len(nums)
        for i in range(n):
            c = 0
            for j in range(n):
                if sorted_nums[j] < nums[i]:
                    c += 1
            out.append(c)
        return out
