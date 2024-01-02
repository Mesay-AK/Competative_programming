class Solution:
    def smallestNumber(self, num: int) -> int:
        num=str(num)
        num=(list(num))

        if num[0]=='-':
            temp=num[1:]
            temp.sort(reverse=True)
            num[1:]=temp
        else:
            num=sorted(num)
            i=0
            while num[0]=='0' and i<len(num):
                num[0], num[i] = num[i], num[0]   
                i+=1         
    
        num=''.join(num)
        return int(num)


        