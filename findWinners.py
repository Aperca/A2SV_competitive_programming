class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        out=[set(),set()]
        w={w[0] for w in matches}
        l={}
        for m in matches:
            if m[1] in l:
                l[m[1]]+=1
            else:
                l[m[1]]=1
        for m in w:
            if m not in l:
                out[0].add(m)
        for key, value in l.items(): 
            if value == 1:  
                out[1].add(key) 
        return [sorted(out[0]), sorted(out[1])] 
