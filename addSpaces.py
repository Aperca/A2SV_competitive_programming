class Solution:
    def addSpaces(self, string: str, spaces: List[int]) -> str:
        temp=""
        l=0
        for i in range(len(string)):
            s=spaces[l]
            if(i==s):
                temp+=" "
                if(l!=len(spaces)-1):
                    l+=1
            temp+=string[i]
        
        return temp
