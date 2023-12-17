class Solution:
    def minimizedStringLength(self, s: str) -> int:
        to_minimize={char:1 for char in s}
        return len(to_minimize)