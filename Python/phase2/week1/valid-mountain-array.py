class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        maxim=max(arr)
        if len(arr)<3 or arr[-1]==maxim or arr[0]==maxim:
            return False
        up=True
        for i in range(1,len(arr)):
            if arr[i]==maxim:
                up=False

            elif up==True and arr[i-1] > arr[i]:
                return False

            elif up==False and arr[i-1] < arr[i]:
                return False

            if arr[i-1]==arr[i]:
                return False
        return True
