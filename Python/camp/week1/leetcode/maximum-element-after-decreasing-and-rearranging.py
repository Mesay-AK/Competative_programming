class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        

        check = Counter(arr)
        surplus = 0
        n = len(arr)
        maxim = n
        i = n
        
        for i in check:
            if i > n :
                surplus += check[i]

        i = n
        while i > 0:
            if i not in check:
                if surplus:
                    surplus -= 1
                else:
                    maxim -= 1
            else:
                surplus += check[i] -1

            i -= 1
        
        return maxim



