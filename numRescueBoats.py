class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n=len(people)
        c=0 
        l=0
        r= n-1
        while r>=l:
            if people[r]>=limit:
                c+=1
                r-=1
            elif (people[r]+people[l])>limit:
                    c+=1
                    r-=1
            elif (people[r]+people[l])<=limit:
                c+=1
                r-=1
                l+=1
        return c
                
