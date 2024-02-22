class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letters = defaultdict(int)
        for idx, char in enumerate(s):
            letters[char] = idx

        start = 0
        last = 0
        result = []
        for i, value in enumerate(s):
            start += 1
            last = max(last, letters[value])
            if i == last:
                result += [start]
                start = 0
                last = i + 1
                
        return result

