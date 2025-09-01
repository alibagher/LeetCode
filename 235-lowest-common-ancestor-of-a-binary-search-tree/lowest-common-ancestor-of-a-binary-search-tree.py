# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findAncestors (self, root: TreeNode, p: TreeNode, ancestors: list) -> list:
        if not root:
            return ancestors
        if p.val < root.val:
            # left
            ancestors.append(root.val)
            return self.findAncestors(root.left, p, ancestors)
        elif p.val > root.val:
            # right
            ancestors.append(root.val)
            return self.findAncestors(root.right, p, ancestors)
        # equal
        ancestors.append(root.val)
        return ancestors

    def findNode(self, root: TreeNode, p: int) -> TreeNode:
        if not root:
            return root
        if p < root.val:
            # left
            return self.findNode(root.left, p)
        elif p > root.val:
            # right
            return self.findNode(root.right, p)
    
        return root


    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ancestorsP = []
        ancestorsQ = []
        ancestorsP = self.findAncestors (root, p, ancestorsP)
        ancestorsQ = self.findAncestors (root, q, ancestorsQ)
        print (ancestorsP,ancestorsQ)

        out = -101
        for i in range(0,len(ancestorsP)):
            if i > len(ancestorsQ) - 1:
                out = ancestorsQ[i-1]
                break

            if ancestorsQ[i] != ancestorsP[i]:
                out = ancestorsQ[i-1]
                break

        if out == -101:
            out = ancestorsP[-1]

        print (out)

        return self.findNode(root,out)