class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        l=0
        counts={}
        for i in range(len(s)):
            if s[i] not in counts:
                counts[s[i]]=0
            counts[s[i]]+=1
            if len(counts)!=(i-l+1):
                counts[s[l]]-=1
                if counts[s[l]]==0:
                    del counts[s[l]]
                l+=1
            res=max(res,i-l+1)
        return res
