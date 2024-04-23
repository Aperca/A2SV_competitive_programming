class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n=len(nums)
        Csum=0
        c=0
        mp={0:1}
        for n in nums:
            Csum+=n
            x=Csum%k
            if x in mp:
                c+=mp[x]
            mp[x]=mp.get(x,0)+1
        return c
                
        
