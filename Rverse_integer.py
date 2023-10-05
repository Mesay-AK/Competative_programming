class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            x=abs(x)
            y=-1
        else:
            y=1
        xs=str(x)
        xs=xs[::-1]
        i=0
        while xs[i]=='0':
            if len(xs)==1:
                break
            xs=xs[1:]
        x=int(xs)
        if (2**31-1)>=x:
            if y<0:
                return -(x)
            else:
                return x
        else:
            return 0
