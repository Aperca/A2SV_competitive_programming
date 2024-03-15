class Solution:
    def isPalindrome(self, x: int) -> bool:
        d=0
        y=x
        while x>0:
            rem=x%10
            x//=10
            d=d*10+rem
        
        if d==y:
            return True
    
