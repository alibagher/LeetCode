class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        stack = []
        operands = ["+", "-", "/", "*"]
        res = 0

        for t in tokens:
            if t in operands:
                second = int(stack.pop())
                first = int(stack.pop())
                if t == "+":
                    stack.append(first + second)
                elif t == "-":
                    stack.append(first - second)
                elif t == "/":
                    stack.append(int(first / second))
                elif t == "*":
                    stack.append(first * second)
            else:
                stack.append(t)
        return int(stack.pop())