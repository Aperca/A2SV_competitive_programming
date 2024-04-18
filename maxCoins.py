class Solution:
    def maxCoins(self, piles: List[int]) -> int:
       piles.sort()
       n=len(piles)
       coins=0
       for i in range(n//3):
        coins+=piles[n-2]
        n-=2
       return coins

