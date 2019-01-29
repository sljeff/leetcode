# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        node = root
        while True:
            if node is None:
                return None
            elif node.val == val:
                return node
            elif node.val < val:
                node = node.right
            else:
                node = node.left
