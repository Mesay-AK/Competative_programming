class Solution:
    def reverseWords(self, s: str) -> str:
        the_list=s.split()
        the_reversed=the_list[::-1]
        return ' '.join(the_reversed)
        