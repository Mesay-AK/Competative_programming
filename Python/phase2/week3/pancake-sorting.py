class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result=[]
        for i in range(len(arr)):
            k=0
            for j in range(len(arr)-i):
                if arr[j] > arr[k]:
                    k=j
            
            temp=arr[:k+1]
            arr[:k+1]=temp[::-1]

            temp2=arr[:len(arr)-i]
            arr[:len(arr)-i]=temp2[::-1]
            
            result.append(k+1)
            result.append(len(arr)-i)

        return result


