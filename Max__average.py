class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        m_s=0
        curr_s=0
        for i in range(k):
            curr_s+=nums[i]
        m_s=curr_s
        l=0
        r=k
        while r<len(nums):
            curr_s+=nums[r]
            curr_s-=nums[l]
            l+=1
            r+=1
            m_s=max(curr_s,m_s)
        return m_s/k
