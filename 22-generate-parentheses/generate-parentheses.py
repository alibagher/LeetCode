class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(opened, closed):
            if opened == closed == n:
                print (stack)
                return res.append(stack.pop())
            
            if opened > closed:
                if opened < n:
                    # can do both closed and open.
                    curr = stack.pop()
                    stack.append(curr + "(")
                    l = backtrack (opened+1, closed)
                    stack.append(curr+")")
                    r = backtrack (opened, closed+1)
                else:
                    curr = stack.pop()
                    stack.append(curr+")")
                    backtrack (opened, closed+1)
            else:
                # only close.
                curr = stack.pop()
                stack.append(curr+"(")
                backtrack (opened+1, closed)
        stack.append("(")
        backtrack(1,0)
        return res