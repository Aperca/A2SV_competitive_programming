class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        result_stack = []
        included = set()
        last_index = {char: idx for idx, char in enumerate(s)}
        
        for idx, char in enumerate(s):
            if char not in included:
                while result_stack and char < result_stack[-1] and idx < last_index[result_stack[-1]]:
                    included.remove(result_stack.pop())
                result_stack.append(char)
                included.add(char)
        
        return ''.join(result_stack)
