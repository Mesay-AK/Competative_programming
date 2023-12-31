class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")

        ans = [""] * len(words)

        for word in words:
            index = int(word[-1]) - 1
            ans[index] = word[:-1]
        
        return " ".join(ans)

