class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        odd = n//2
        even = n - odd

        def power(x,n):
            if n == 0: return 1
            if n == 1:
                return x
            return (((power(x,n//2)%mod)**2)%mod * power(x,n%2))%mod
            
        return (power(4,odd) * power(5,even))%mod