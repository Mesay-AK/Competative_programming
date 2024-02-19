class Solution:
    def longestPalindrome(self, s: str) -> int:
        check = Counter(s)
        odd = 0
        number = 0
        for key in check:
            val = check[key]
            if val%2:
                odd = 1
                number += val - 1

            else:
                number += val
        if odd == 0: return number
        return number + 1

        