class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target=defaultdict(int)
        curr=defaultdict(int)

        if len(p)>len(s):
            return []
        for i in range(len(p)):
            target[p[i]]+=1
            curr[s[i]]+=1

        result=[]
        i=0
        for j in range(len(p),len(s)):
            if curr==target:
                result.append(i)
            curr[s[i]]-=1
            if curr[s[i]]==0:
                del(curr[s[i]])
            curr[s[j]]+=1
            i+=1
        if curr==target:
            result.append(i)


        return result

