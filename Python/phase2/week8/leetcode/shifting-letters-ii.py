class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        n = len(s)
        slist = list(map(ord, list(s)))
        arr = [0] * (n+1)
        

        for sh in shifts:
            left, right, shift = sh[0], sh[1], sh[2]
            if shift == 0:
                arr[left] -= 1
                arr[right+1] += 1
            else:
                arr[left] += 1
                arr[right+1] -= 1

        for i in range(1,n):
            arr[i] += arr[i-1]
            
        print(arr)

        for idx, value in enumerate(slist):
            order = value + arr[idx]
            slist[idx] = chr((order - 97 )% 26  + 97)

        return ''.join(slist)
