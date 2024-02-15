class Solution:
    def balancedString(self, s: str) -> int:
        charCount, left, requiredLen, res = Counter(s), 0, len(s) // 4, inf
        for right in range(len(s)):
            charCount[s[right]] -= 1
            while left < len(s) and charCount['W'] <= requiredLen and charCount['Q'] <= requiredLen and charCount['E'] <= requiredLen and charCount['R'] <= requiredLen:
                res = min(res, right - left + 1)
                charCount[s[left]] += 1
                left += 1
        return res
