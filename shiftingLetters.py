class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        size = len(s)
        frequency = [0] * (size + 1)
    
        for start, end, direction in shifts:
            if direction == 1:
                frequency[start] += 1
                frequency[end + 1] -= 1
            else:
                frequency[start] -= 1
                frequency[end + 1] += 1
        
        for i in range(1, size + 1):
            frequency[i] += frequency[i - 1]
        
        shifted_string = []
        for i in range(size):
            shifted_char = chr((ord(s[i]) - ord('a') + frequency[i]) % 26 + ord('a'))
            shifted_string.append(shifted_char)
        
        return "".join(shifted_string)
