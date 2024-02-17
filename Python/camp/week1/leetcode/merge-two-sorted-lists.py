# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):

        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        if list1.val <= list2.val :
            temp= current=ListNode(list1.val)
            list1=list1.next
        else:
            temp= current=ListNode(list2.val)
            list2=list2.next

        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                current.next=ListNode(list1.val)
                list1=list1.next
                current = current.next
            elif list1.val > list2.val:
                current.next = ListNode(list2.val)
                list2 = list2.next
                current = current.next
    
        while list2 is not None:   
            current.next = ListNode(list2.val)
            list2 =list2.next
            current=current.next
        
        while list1 is not None:   
            current.next = ListNode(list1.val)
            list1 = list1.next
            current=current.next
        return temp