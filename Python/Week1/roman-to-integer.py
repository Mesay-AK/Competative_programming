class Solution:
    def romanToInt(self, s: str) -> int:

        Roman={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        arabic= Roman[s[0]]

        for i in range(1,len(s)):
            before=Roman[s[i-1]]
            if before < Roman[s[i]]:
                arabic-=(2*before)

            arabic+=Roman[s[i]]
        return arabic

            