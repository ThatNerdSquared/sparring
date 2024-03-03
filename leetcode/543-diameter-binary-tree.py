# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.result

    def dfs(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        else:
            l = self.dfs(node.left)
            r = self.dfs(node.right)
            self.result = max(
                self.result,
                l + r
            )
            return 1 + max(l, r)
