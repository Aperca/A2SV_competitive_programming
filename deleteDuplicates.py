class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy= ListNode(0,head)

        curr= dummy.next

        while curr and curr.next:
            if curr.val==curr.next.val:
                curr.next=curr.next.next
            curr= curr.next
        return head
