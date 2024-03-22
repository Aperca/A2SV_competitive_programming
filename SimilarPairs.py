class Solution:
    def similarPairs(self, words: List[str]) -> int:
        counter=0
        for i in range (len(words)-1):
            s1=list(words[i])
            s1.sort
            s1=set(s1)
            for j in range(i+1,len(words)):
                s2=list(words[j])
                s2.sort
                s2=set(s2)
                if s1==s2:
                    counter+=1
        return counter
