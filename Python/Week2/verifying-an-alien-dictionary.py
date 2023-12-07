class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        the_order={char : index for index,char in enumerate(order)}
        for i in range(len(words)-1):
            word1, word2 = words[i],words[i+1]
            for j in range(len(word1)):
                if j ==len(word2):
                    return False
                if word1[j]!=word2[j]:
                    if the_order[word2[j]]< the_order[word1[j]]:
                        return False
                    break
        return True
