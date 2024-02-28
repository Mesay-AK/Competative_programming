class Solution:
    def numberOfWays(self, s: str) -> int:
        Zprefix, Zsuffix, Oprefix, = 0, s.count('0'), 0
        Osuffix = len(s) - Zsuffix

        result = 0

        for num in s:
            if num == '1':
                result += (Zprefix * Zsuffix)
                Oprefix += 1
                Osuffix -= 1

            else:
                result += (Oprefix*Osuffix)
                Zprefix += 1
                Zsuffix -= 1

        return result