class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def iab(self,data):
        newnode=Node(data)
        newnode.next=self.head
        if self.head:
            self.head.prev=newnode
        self.head=newnode
        
       
    def backtraverse(self):
        print("value for transversing backward...")
        temp=self.head
        if not temp:
            print("empty list")
            return 
        while temp.next:
             temp=temp.next
        while temp:
            print(temp.data,end='<-->')
            temp=temp.prev
        print("None")
    def display(self):
        temp=self.head
        print("Doubly Li'nked List")
        while temp:
            print(temp.data,end="<-->")
            temp=temp.next
        print("None")
       
dll=DoublyLinkedList()
n=int(input("enter the number of elements to insert at end:"))
for i in range(n):
    val=int(input(f"enter element {i+1}:"))
    dll.iab(val)
dll.display()
dll.backtraverse()
        
