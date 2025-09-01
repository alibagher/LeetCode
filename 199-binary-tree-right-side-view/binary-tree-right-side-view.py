# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxLevelReached : int= 0
    def helper (self, root : Optional[TreeNode], answer:List[int], level: int) -> List[int]:

        if not root:
            return answer

        if level >= self.maxLevelReached:
            answer.append(root.val)
            self.maxLevelReached += 1
            answer = self.helper(root.right, answer, level+1)
            answer = self.helper(root.left, answer, level+1)
        else:
            answer = self.helper(root.right, answer, level+1)
            answer = self.helper(root.left, answer, level+1)
        
        return answer

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        return self.helper(root, [], 0)