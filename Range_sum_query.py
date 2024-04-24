class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum=[0]
        for n in nums:
            self.prefix_sum.append(self.prefix_sum[-1]+n)
        
    def sumRange(self, left: int, right: int) -> int:
        left_sum=self.prefix_sum[left]
        right_sum=self.prefix_sum[right+1]

        return right_sum-left_sum
