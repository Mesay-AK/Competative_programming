class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result=[]
        for j in range(n):
          result.append(nums[j])
          result.append(nums[j+n])
          
        return result

