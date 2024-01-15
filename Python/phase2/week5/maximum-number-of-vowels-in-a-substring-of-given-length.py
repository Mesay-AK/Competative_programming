class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels={'a', 'e', 'i', 'o','u'}

        maxim=0
        count=0
        for i in range(k):
            if s[i] in vowels:
                count += 1
        left=0
        for j in range(k,len(s)):
            maxim = max(maxim, count)
            if s[left] in vowels:
                count -= 1
            if s[j] in vowels:
                count += 1
            left += 1
            
        maxim = max(maxim, count)

        return maxim
        