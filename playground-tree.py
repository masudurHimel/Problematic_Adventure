# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, node, level):
        if not node:
            return level - 1

        l = self.dfs(node.left, level + 1)
        r = self.dfs(node.right, level + 1)

        if l == "hoinai" or r == "hoinai":
            return False

        if abs(l - r) > 1:
            return "hoinai"
        return max(l, r)

    def isBalanced(self, root):
        x = self.dfs(root, 0)
        if x != "hoinai":
            return True
        return False


s = Solution()
# tree = TreeNode(
#     1,
#     left=TreeNode(
#         2,
#         left=TreeNode(
#             3,
#             left=TreeNode(4),
#             right=TreeNode(4)),
#         right=TreeNode(3)),
#     right=TreeNode(2)
# )
tree = TreeNode(1)

s.isBalanced(tree)
