class MyCircularDeque:

    def __init__(self, k: int):
        self.capacity = k
        self.deque = []
        
    def insertFront(self, value: int) -> bool:
        if len(self.deque) < self.capacity:
            self.deque.insert(0, value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if len(self.deque) < self.capacity:
            self.deque.append(value)
            return True
        return False

    def deleteFront(self) -> bool:
        if self.deque:
            self.deque.pop(0)
            return True
        return False

    def deleteLast(self) -> bool:
        if self.deque:
            self.deque.pop()
            return True
        return False

    def getFront(self) -> int:
        return self.deque[0] if self.deque else -1

    def getRear(self) -> int:
        return self.deque[-1] if self.deque else -1

    def isEmpty(self) -> bool:
        return len(self.deque) == 0

    def isFull(self) -> bool:
        return len(self.deque) == self.capacity
