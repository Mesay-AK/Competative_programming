class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits=map(str,digits)
        digits=int(''.join(digits))
        digits=digits+1
        digits=map(int,list(str(digits)))
        return digits