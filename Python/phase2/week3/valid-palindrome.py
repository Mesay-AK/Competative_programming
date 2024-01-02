class Solution(object):
    import string
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        punct=string. punctuation + " "
        nL=[]
        s=s.upper()
        for i in s:
            if i not in punct:
                nL.append(i)
        for i in range(len(nL)//2):
            if nL[0]!=nL[-1]:
                return False
            else:
                nL.pop(-1)
                nL.pop(0)
                
        return True

