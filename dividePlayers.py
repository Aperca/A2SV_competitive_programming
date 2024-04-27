class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        l = 0
        r = n - 1
        total = 0 
        
        while l < r:
            if skill[l+1] + skill[r-1]!=skill[l] + skill[r] :
                return -1
            t = skill[l] + skill[r] 
            total += skill[l] * skill[r]
            l += 1
            r -= 1
            
        return total
