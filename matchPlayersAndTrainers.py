class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        count=0
        players.sort()
        trainers.sort()
        l,r=0,0
        while l<len(players) and r< len(trainers):
                if players[l]<=trainers[r]:
                    count+=1
                    l+=1
                    r+=1
                else:
                    r+=1
        return count
