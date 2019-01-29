# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        node = root
        smaller, bigger = list(sorted([p.val, q.val]))
        while True:
            if not node:
                return node
            if smaller <= node.val <= bigger:
                return node
            elif node.val < smaller:
                node = node.right
            else:
                node = node.left
