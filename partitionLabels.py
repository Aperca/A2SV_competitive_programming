class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        l, r = 0, 0
        last_indices = {m: s.rindex(m) for m in s}
        for i, m in enumerate(s):
            r = max(r, last_indices[m])
            if i == r:
                ans.append(r - l + 1)
                l = r + 1
        return ans
