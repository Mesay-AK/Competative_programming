# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        curr = head
        length = 0
        number = 0

        while curr:
            length += 1
            curr = curr.next
            
        weight = 2 ** (length-1)
        curr = head

        for i in range(length):
            number += (curr.val * weight)
            curr = curr.next
            weight //= 2

        return number