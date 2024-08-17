# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
        prev=None 
        while slow:
            temp= slow 
            slow=slow.next
            temp.next=prev
            prev=temp
        reversed_right_half=temp

        while reversed_right_half:
            if reversed_right_half.val!=head.val:
                return False
            head=head.next
            reversed_right_half=reversed_right_half.next
        return True
