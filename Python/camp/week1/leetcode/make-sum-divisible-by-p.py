class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        target = total % p

        if target == 0:
            return 0

        prev = {}
        best = float('inf') 
        
        current = 0
        
        for idx, x in enumerate(nums):
            current += x
            current %= p

            if current == target:
                best = min (best, idx + 1)

            if (current - target) % p in prev:
                best = min(idx- prev[(current - target) % p], best)

            prev[current] = idx

        if best >= len(nums):
            return -1

        return best