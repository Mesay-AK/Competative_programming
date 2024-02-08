class NumArray:

    def __init__(self, nums: List[int]):
        self.total = 0
        self.prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.total += nums[i]
            self.prefix[i+1] = self.total


    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1] - self.prefix[left]
     
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)