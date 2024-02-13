class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = Node()
    
    def getNode(self, index):

        curr = self.head
        while curr and 0 <=index :
            curr = curr.next
            index -= 1
        return curr
        
    def get(self, index: int) -> int:
        
        curr = self.getNode(index)
        return curr.val if curr else -1
        

    def addAtHead(self, val: int) -> None:

        new = Node(val)
        temp = self.head.next
        self.head.next = new
        new.next = temp
        

    def addAtTail(self, val: int) -> None:

        new = Node(val)
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new
        new.next = None
        

    def addAtIndex(self, index: int, val: int) -> None:

        new = Node(val)
        curr = self.getNode(index-1)
        if not curr:
            return  
        temp = curr.next
        curr.next = new
        new.next = temp        

    def deleteAtIndex(self, index: int) -> None:

        curr = self.getNode(index-1)
        if not curr or not curr.next:
           return 
        curr.next = curr.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)