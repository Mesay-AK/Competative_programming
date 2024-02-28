class Solution:
    def distance(self, nums: List[int]) -> List[int]:

        n = len(nums)

        result = [0] * n 
        track = defaultdict(list)
        for i, v in enumerate(nums):
            track[v].append(i)

        

        for i, value in track.items():
            
            l = len(value)
            prefix = [0] * (l+1)

            for j in range(l):

                prefix[j+1] = prefix[j] + value[j]
            
            for m in range(l):
                first = m * value[m] - prefix[m]
                second =( (l - m -1 )* value[m]) - (prefix[l] - prefix[m+1])
                result[value[m]] = abs(first) + abs(second) 



        return result