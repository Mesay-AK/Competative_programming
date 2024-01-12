class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        i, j = 0, 0
        rslt = []

        while i < len(firstList) and j < len(secondList):
            start, end = max(firstList[i][0],secondList[j][0]), min(firstList[i][1], secondList[j][1])

            if start <= end:
                rslt.append([start, end])
            if firstList[i][1]< secondList[j][1] :
                i+=1
            else:

                j+=1
        return rslt