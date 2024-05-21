class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            if stack:
                while stack and stack[-1][0] < t:
                    res[(stack[-1])[1]] = i - (stack[-1])[1]
                    stack.pop()
            stack.append((t,i))
        return res