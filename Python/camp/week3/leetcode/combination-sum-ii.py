class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        result = set()
        self.sum = 0
        arr = []

        def combine(i):
            if self.sum == target:
                result.add(tuple(arr))
                return

            for j in range(i, len(candidates)):

                if i!=j and candidates[i] == candidates[i-1]:continue
                val = candidates[j]
                if self.sum + val > target: break

                
                arr.append(val)
                self.sum += val

                combine(j+1)

                arr.pop()
                self.sum -= val


        combine(0)
        return result
















