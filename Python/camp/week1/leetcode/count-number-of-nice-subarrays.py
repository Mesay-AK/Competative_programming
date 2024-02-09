class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd, total, left, final = 0, 0, 0, 0

        for r in range(len(nums)):
            if nums[r] % 2:
                odd += 1
                total = 0
            while odd == k:
                if nums[left] % 2:
                    odd -= 1
                total += 1
                left += 1
            final += total

        return final 

                


        



            
                

            
                