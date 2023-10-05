class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l=[]
        multiplier=1
        i=-1
        j=-1
        while i>=len(num1)*(-1):
            product=int(num1[i])*int(num2[j])*multiplier
            l.append(product)
            if j==len(num2)*(-1):
                multiplier=10**(-1*(i+1))
                j=-1
                i-=1
            else:
                j-=1
            multiplier*=10
        result=0
        for i in l:
            result+=i
        return str(result)
