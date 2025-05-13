# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, _min, _max):
            if not node:    return True
            if not (_min < node.val < _max):    
                return False
            
            ans = True
            if node.left:
                ans &= dfs(node.left, _min, min(_max, node.val))
            if node.right:
                ans &= dfs(node.right, max(_min, node.val), _max)
            return ans

        return dfs(root, -math.inf, math.inf)