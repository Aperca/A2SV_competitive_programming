class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        t = 0
       
        while tickets[k] > 0:
            for i in range(n):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    t += 1
                    if i == k and tickets[i] == 0:
                        break
        return t
        
