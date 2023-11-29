class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        minim=len(strs[0])
        prefix=''
        for i in range(len(strs[0])):
            now=strs[0][i]
            for j in range(len(strs)):
                if now!=strs[j][i]:
                    return prefix
            prefix+=now
        return prefix

                        