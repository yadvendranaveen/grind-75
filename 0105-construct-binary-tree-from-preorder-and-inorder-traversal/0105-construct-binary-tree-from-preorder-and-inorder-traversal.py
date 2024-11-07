# question- do they have unique values?
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorderIdx = 0
        inorderMap = {val:idx for idx,val in enumerate(inorder)}

        def arrayToTree(left, right):
            nonlocal preorderIdx
            if left>right:  return 

            rootVal = preorder[preorderIdx]
            root = TreeNode(rootVal)

            preorderIdx+=1

            root.left = arrayToTree(left, inorderMap[rootVal]-1)
            root.right = arrayToTree(inorderMap[rootVal]+1, right)

            return root
        
        return arrayToTree(0, len(preorder)-1)
        