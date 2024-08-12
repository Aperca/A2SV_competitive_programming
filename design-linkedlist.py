class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)  
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        count = 0
        while curr:
            if count == index:
                return curr.val
            curr = curr.next
            count += 1
        return -1

    def addAtHead(self, val: int) -> None:
        nn = ListNode(val)
        nn.next = self.head.next
        self.head.next = nn

        if not nn.next: 
            self.tail = nn

    def addAtTail(self, val: int) -> None:
        nn = ListNode(val)
        self.tail.next = nn
        self.tail = nn

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head
        count = 0
        while curr and count < index:
            curr = curr.next
            count += 1
        
        if count == index:
            nn = ListNode(val)
            nn.next = curr.next
            curr.next = nn
            
            if nn.next is None: 
                self.tail = nn

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        count = 0
        while curr.next and count < index:
            curr = curr.next
            count += 1

        if count == index and curr.next:
            if curr.next == self.tail:  
                self.tail = curr
            curr.next = curr.next.next
