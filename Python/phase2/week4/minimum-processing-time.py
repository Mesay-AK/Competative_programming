class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse=True)
        tasks.sort()

        minim=0
        j,bdry = 0,4
        print(processorTime, tasks)
        for i in range(len(processorTime)):
            while j<bdry:
                curr = processorTime[i]+tasks[j]
                j+=1
                minim=max(curr,minim)

            bdry+=4
        return minim