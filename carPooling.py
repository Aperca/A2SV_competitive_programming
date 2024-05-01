class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passenger=0
        destination=[0]*1001
        for pas,frm,to in trips:
            destination[frm]+=pas
            destination[to]-=pas
        for d in destination:
            passenger+=d
            if passenger>capacity:
                return False
        return True
