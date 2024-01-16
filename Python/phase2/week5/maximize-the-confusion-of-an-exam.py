class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        confuse =  0
        tomax = {'T' : 0, 'F' : 0}

        left, j = 0, 0
        while j < len(answerKey):
            tomax[answerKey[j]] +=1
            minim = min(tomax["T"], tomax["F"])
            if minim > k:
                tomax[answerKey[left]] -= 1
                left += 1
            confuse = max(confuse, j - left+1)

            j += 1

        return confuse