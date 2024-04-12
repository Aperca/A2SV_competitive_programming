class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        out=[]
        cp=Counter(p)
        wCount=Counter(s[:len(p)])
        l=0
        r=len(p)
        while r<len(s):
            if cp==wCount:
                out.append(l)
            wCount[s[l]]-=1
            wCount[s[r]]+=1
            l+=1
            r+=1
        if wCount==cp:
            out.append(l)
        return out
            
