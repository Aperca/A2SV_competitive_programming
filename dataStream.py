class DataStream:
    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.count = 0
        self.last_k_elements = [None] * k
        self.num_value_elements = 0

    def consec(self, num: int) -> bool:
        idx = self.count % self.k

        if self.last_k_elements[idx] == self.value:
            self.num_value_elements -= 1
       
        self.last_k_elements[idx] = num
        
        if num == self.value:
            self.num_value_elements += 1

        self.count += 1
        if self.count < self.k:
            return False

        return self.num_value_elements == self.k

