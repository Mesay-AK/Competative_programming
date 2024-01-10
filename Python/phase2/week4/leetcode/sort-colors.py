class Solution:
    def sortColors(self, arr: List[int]) -> None:
        n = len(arr)
        start = 0
        end = len(arr)-1
        i = 0

        while i <= end:
            
            if arr[i] == 0:
                arr[i], arr[start] = arr[start], arr[i]
                start += 1
            
            elif arr[i] == 2:
                arr[i], arr[end] = arr[end], arr[i]
                end -= 1
                i -= 1
            i += 1