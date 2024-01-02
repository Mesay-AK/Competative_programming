class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mark={}
        for i in range(len(arr2)):
            mark[arr2[i]]=i
        
        def comparator(num):
            if num not in mark:
                return len(arr2) + num
            return mark[num]

        arr1.sort(key=comparator)

        return arr1