class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    dictionary = {}
    for i in range(len(array)):
        dictionary[array[i]] = i
    for i in array:
        if i != target - i and target-i in dictionary.keys():
            return [dictionary[i], dictionary[target-i]]
    return []
