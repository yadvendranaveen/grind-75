# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(node, lvl):
            if not node: return
            if lvl == len(ans):
                ans.append(node.val)
            dfs(node.right, lvl+1), dfs(node.left, lvl+1)

        dfs(root, 0)
        return ans
        