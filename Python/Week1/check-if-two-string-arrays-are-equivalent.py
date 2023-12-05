class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # Join the list into a string and check if they have the same value
        if ''.join(word1)==''.join(word2): 
            return True
        return False
