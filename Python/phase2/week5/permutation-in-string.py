class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        length = len (s1)
        ds1 = defaultdict(int)
        ds2 = defaultdict(int)

        for i in range(length):
            ds1[s1[i]] += 1 
            ds2[s2[i]] += 1 

        left, j = 0, length
        while j < len(s2):

            if ds1 == ds2:
                return True

            ds2[s2[left]] -= 1
            if ds2[s2[left]] == 0:
                del(ds2[s2[left]])

            ds2[s2[j]] += 1
            j += 1
            left += 1 

        if ds1 == ds2:
                return True

        return False


        