class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def reversing(i, n):
            if n <= i:
                return
            s[i],s[n] = s[n], s[i]
            
            return reversing(i+1, n-1)
        
        reversing(0, len(s)-1)

