class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        track = set()

        result = set()
        self.sum = 0
        arr = []

        def combine(i, track):

            if len(arr) == k and self.sum == n:
                result.add(tuple(arr[:]))
                return

            for j in range(i, 10):

                if self.sum > n:
                    return
                if j in track:continue
                arr.append(j)
                self.sum += j
                track.add(j)

                combine(j + 1, track)

                arr.pop()
                self.sum -= j
                track.remove(j)

            

        combine(1,track)
        return result

            