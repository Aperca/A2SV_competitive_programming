# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy= ListNode(0,head)
        curr = head
        prev=dummy
        for i in range(left-1):
            prev=prev.next
        start = prev.next 
        nxt = start .next

        for i in range(right -left):
            start.next= nxt.next
            nxt.next=prev.next
            prev.next=nxt 
            nxt = start.next
        return dummy.next
