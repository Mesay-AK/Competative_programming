# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        dictA = {}
        curr = headA
        while curr:
            dictA[curr]= curr
            curr = curr.next

        currB = headB 
        while currB:
            if currB in dictA:
                return currB
                    
            currB = currB.next

        return None