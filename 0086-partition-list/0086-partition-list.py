# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head: return head
        before, after = head, head
        while before and before.val>=x:    before = before.next
        while after and after.val<x:  after = after.next

        before_head, after_head = before, after
        curr = head
        while curr:
            if curr not in (before_head, after_head):
                if curr.val<x:
                    before.next = curr
                    before = before.next
                else:
                    after.next = curr
                    after = after.next
            curr = curr.next
        if before_head and after_head:
            after.next, before.next = None, after_head
        return before_head or after_head
