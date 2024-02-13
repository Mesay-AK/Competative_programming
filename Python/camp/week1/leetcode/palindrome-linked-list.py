# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        forward = head
        newHead = self.createNew(head)
        backward = self.reverse(newHead)
        
        while forward:
            if forward.val != backward.val:
                return False
            forward = forward.next
            backward = backward.next

        return True
    def createNew(self,head):
        newHead = ListNode(val = head.val)
        curr = head.next
        curr2 = newHead

        while curr:
            curr2.next = ListNode(val= curr.val)
            curr = curr.next
            curr2 = curr2.next
        
        return newHead
    def reverse(self, head):
        if not head:
            return None
        elif not head.next:
            return head

        previous = None
        current = head
       

        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
            
        return previous
    