class Solution:
    def interpret(self, command: str) -> str:
        out=""
        command = command.replace("()", "o")
        for i in range(len(command)):
            if command[i]=="(" or command[i]==")":
                continue
            else:
                out+=command[i]
            
        return out
