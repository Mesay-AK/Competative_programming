class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        srg= list(map(str,nums))

        for j in range(len(srg)):
            for i in range(len(srg)-1-j):
                first = srg[i] + srg[i+1]
                second = srg[i+1] + srg[i]

                if first < second:
                    srg[i], srg[i + 1] = srg[i + 1], srg[i]
        ans = ''.join(srg)
        ans = int(ans)
        return str(ans)
                




        # 3 30 34 5 9
        # 34 30 5 9 3
        # 34 5 9 3 30 
        # 5 9 34 3 30



        # 330 303  
        # 334 343
        # 35 53
        # 3430 3034
        # 305 530
        # 309 930
        # 345 534

