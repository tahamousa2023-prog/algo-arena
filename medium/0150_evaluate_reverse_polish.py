class Solution:
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token in ("+", "-", "*", "/"):
                b = stack.pop()
                a = stack.pop()
                if token == "+": stack.append(a + b)
                elif token == "-": stack.append(a - b)
                elif token == "*": stack.append(a * b)
                else: stack.append(int(a / b))
            else:
                stack.append(int(token))
        return stack[0]

if __name__ == "__main__":
    sol = Solution()
    assert sol.evalRPN(["2","1","+","3","*"]) == 9
    assert sol.evalRPN(["4","13","5","/","+"]) == 6
    print("All tests passed v")
