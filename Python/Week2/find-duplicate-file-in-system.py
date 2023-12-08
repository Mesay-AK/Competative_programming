class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        dic=defaultdict(lambda :[])
        for i in range(len(paths)):
            st=paths[i]
            lst=st.split(" ")
            for j in range(1,len(lst)):
                sp=lst[j].index("(")
                dic[lst[j][sp:]].append(lst[0]+"/"+lst[j][:sp])
        return [dic[i] for i in dic if len(dic[i])>1]