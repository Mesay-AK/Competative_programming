class Solution:
    def isPalindrome(self, x: int) -> bool:
        the_string=str(x)
        j=len(the_string)-1
        for i in range(len(the_string)//2):
            if the_string[i]!=the_string[j]:
                return False
            j-=1
        
        return   True

        