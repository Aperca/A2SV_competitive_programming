# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
           if not head:
            return None
           slow= fast= head
           while fast and fast.next:
            fast= fast.next.next
            slow=slow.next
            if fast==slow: # fast and slow will eventually meet, not necessarly at the start of the cycle tho
                break
            # If the loop exits without breaking, it means no cycle was detected or fast.next points to null 
           if slow != fast:
            return None
            # start one of the pointers at head to keep the distance between them which is== to one full cycle in the list
            ''
           slow=head
           while slow!=fast: # the point where they meet again is the starting pt
            slow=slow.next
            fast=fast.next
            
           return slow


