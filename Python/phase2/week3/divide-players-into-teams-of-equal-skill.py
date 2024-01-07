class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
    # Using two pointers
        r=skill.sort()
        i=0
        j=len(skill)-1
        chemistry=0
        while i<j:
            now=skill[i]+skill[j]
            then=skill[i+1]+skill[j-1]
            chemistry=chemistry+skill[i]*skill[j]
            if now != then:
                return -1
            i+=1
            j-=1
        return chemistry