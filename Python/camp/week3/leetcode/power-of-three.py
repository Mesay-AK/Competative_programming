class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1:
            return True
        elif n%3!=0 or n==0:
            return False
        return self.isPowerOfThree(n/3)
        # if n==1:
        #     return True
        # if n<1:
        #     return False
        # return self.isPowerOfThree(n/3)