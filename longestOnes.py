class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l,r,max_one,count=0,0,0,0
        n=len(nums)
        while r<n:
            if nums[r]==1:
                count+=1
            while (r-l+1-count) > k:
                if nums[l]==1:
                    count-=1
                l+=1
            max_one=max(max_one,r-l+1)
            r+=1
        return max_one
