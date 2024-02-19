class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:

        running, idx, patch, frequency = 0, 0, 0, Counter(nums)
        nums.append(n+1)

        if nums[0] != 1:
            running += 1
            patch += 1

        while running < n:

            if idx < len(nums) - 1 and running >= nums[idx]:
                running += nums[idx] * frequency[nums[idx]]
                idx += frequency[nums[idx]]

            elif running + 1 < nums[idx] :
       
                patch += 1
                running += (running + 1)
                
            else:
                running += nums[idx] * frequency[nums[idx]]
                idx += frequency[nums[idx]]
                
                # print(running + 1)

        return patch
