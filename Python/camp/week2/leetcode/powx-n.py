class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if x == 0:
               return 0
            elif n == 0:
               return 1

            result = helper(x, n//2)
            result = result*result

            return x*result if n%2 else result

        res = helper(x, abs(n))
        return res if n >= 0 else 1/res 