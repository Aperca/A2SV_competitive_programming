class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.count = 0
        self.last_k_elements = [None] * k  

    def consec(self, num: int) -> bool:
        self.last_k_elements[self.count % self.k] = num
        self.count += 1
        
        if self.count < self.k:
            return False
        
        for i in range(self.k):
            if self.last_k_elements[i] != self.value:
                return False
        return True
