class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = ""
        l = 0
        r = 0
        while l < len(word1) and r < len(word2):
            if word1[l:] > word2[r:]:
                merge += word1[l]
                l += 1
            else:
                merge += word2[r]
                r += 1
        merge += word1[l:]
        merge += word2[r:]
        return merge
