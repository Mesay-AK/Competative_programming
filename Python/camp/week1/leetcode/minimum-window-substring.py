class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = Counter(t)
        c = len(window)
        i = start = 0
        n = len(s)
        result = n + 1
        for j in range(n):
            if s[j] in window:
                window[s[j]] -= 1
                if window[s[j]] == 0:
                    c -= 1            
            while c == 0:
                if result > j-i+1:
                    result = j-i+1
                    start = i
                if s[i] in window:
                    window[s[i]] += 1
                    if window[s[i]] > 0:
                        c += 1
                i += 1
        if result > n:
            return ""
        return s[start : start + result]