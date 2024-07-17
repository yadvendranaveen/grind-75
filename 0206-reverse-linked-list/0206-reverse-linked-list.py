# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def dfs(node):
            if not node or not node.next: return node
            last_node = dfs(node.next)
            node.next.next = node
            node.next = None
            return last_node

        return dfs(head)
        