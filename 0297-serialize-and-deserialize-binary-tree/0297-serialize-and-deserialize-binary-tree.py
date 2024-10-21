# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        ans = []
        def dfs(node):
            if not node: 
                ans.append('#')
                return
            ans.append(str(node.val))
            dfs(node.left), dfs(node.right)
        dfs(root)
        return ','.join(ans)

    def deserialize(self, data):
        data = data.split(',')
        i = 0
        def dfs():
            nonlocal i
            if data[i]=='#':    return None
            node = TreeNode(int(data[i]))
            i+=1
            node.left = dfs()
            i+=1
            node.right = dfs()
            return node
        return dfs()


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))