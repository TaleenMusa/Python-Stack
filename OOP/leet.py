class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    class MyLinkedList:
        def __init__(self):
            self.head = None

        def addAtHead(self, val):
            new_node = Node (new_data)
            new_node.next = self.head
            self.head = new_node
            
            

        def addAtTail(self, val):
            if self.head==None
                self.head=Node(val)
            else :
                current=self.head
                while current.next is not None:
                    current=current.next
                current.next=Node(val)
            