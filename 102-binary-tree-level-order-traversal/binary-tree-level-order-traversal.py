# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = []
    def helper (self, root: Optional[TreeNode], level: int):
        if not root:
            return

        if len(self.res) <= level :
            sub = [root.val]
            self.res.append(sub)
        else:
            self.res[level].append(root.val)

        self.helper (root.left, level+1)
        self.helper(root.right, level+1)
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []
        self.helper(root, 0)

        return self.res