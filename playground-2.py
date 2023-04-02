# Definition for a binary tree node.
from collections import Counter
from copy import deepcopy


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, node):
        if not node:
            return None

        print(node.val)
        l = self.dfs(node.left)
        r = self.dfs(node.right)

        temp = node.left
        node.left = node.right
        node.right = temp
        return node

    def invertTree(self, root):
        self.dfs(root)


s = Solution()
x = TreeNode(val=1, left=TreeNode(val=0, left=TreeNode(val=0), right=TreeNode(val=1)),
             right=TreeNode(val=1, left=TreeNode(val=0), right=TreeNode(val=1)))
print(s.invertTree(x))
