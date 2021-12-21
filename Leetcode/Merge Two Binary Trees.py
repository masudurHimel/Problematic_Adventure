# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs(root):
    queue = []

    queue.append(root)
    visited = {}
    res = []
    while queue:
        _ = queue.pop(0)
        res.append(_.val)

        for i in [_.left, _.right]:
            if i and visited.get(i, False) == False:
                queue.append(i)
                visited[i] = True
    return res


class Solution:
    def mergeTrees(self, root1, root2):
        res = []
        res.append([root1, root2])
        while res:
            if t1 is None:
                return t2
            _ = res.pop(0)
            if _[1] is None:
                continue
            _[0].val += _[1].val

            if _[0].left is None:
                _[0].left = _[1].left
            else:
                res.append([_[0].left, _[1].left])
            if _[0].right is None:
                _[0].right = _[1].right
            else:
                res.append([_[0].right, _[1].right])
        return root1


t1 = TreeNode(val=1, left=TreeNode(val=3, left=TreeNode(val=5)), right=TreeNode(val=2))
t2 = TreeNode(val=2, left=TreeNode(val=1, right=TreeNode(val=4)),
              right=TreeNode(val=3, right=TreeNode(val=7)))
s = Solution()
# print(s.mergeTrees(t1, t2))
s.mergeTrees(t1, t2)
print(bfs(t1))
