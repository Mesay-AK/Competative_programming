class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maximum=''
        for i in range(len(num)-2):
            if num[i]==num[i+1]==num[i+2]:
                maximum=max(maximum,num[i:i+3])
        return maximum


       
