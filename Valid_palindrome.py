class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        punc = string.punctuation + " "
        s = s.upper()
        new_s=[]
        for i in s:
            if i not in punc:
                new_s.append(i)
        index=0
        size=len(new_s)-1 
        while index<size:
            if new_s.pop() != new_s[index]:
                return False
            index += 1
            size -= 1
        return True
