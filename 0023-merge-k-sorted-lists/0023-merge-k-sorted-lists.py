# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []

        for i, head in enumerate(lists):
            if head:   heappush(pq, (head.val, i, head)) # i is put in there in case val is same for 2 ListNode, then idx will be used for sorting by heap. Since ListNode obj can't be compared

        dummy = ListNode(0)
        current = dummy
        while pq:
            _, i, node = heappop(pq)
            current.next = node
            current = current.next

            if node.next:
                heappush(pq, (node.next.val, i, node.next))

        return dummy.next
        

        


        