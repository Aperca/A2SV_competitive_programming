class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_count = 0
        char_count = {}

        for r in range(len(s)):
            char_count[s[r]] = char_count.get(s[r], 0) + 1
            max_count = max(max_count, char_count[s[r]])

            if (r - l + 1) - max_count > k:
                char_count[s[l]] -= 1
                if char_count[s[l]] == 0:
                    del char_count[s[l]]
                l += 1

        return len(s) - l
