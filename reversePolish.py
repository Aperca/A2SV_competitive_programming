class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        valid_op = ["+", "-", "*", "/"]

        for t in tokens:
            if t not in valid_op:
                stack.append(int(t))
            else:
                y = stack.pop()
                x = stack.pop()
                if t == "+":
                    z = x + y
                elif t == "-":
                    z = x - y
                elif t == "*":
                    z = x * y
                else:  
                    z = int(x / y) 
                stack.append(z)

        return int(stack[0])  

        
