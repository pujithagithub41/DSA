class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def iae(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp
    def backtraverse(self):
        print("value for transversinf backward...")
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
    dll.iae(val)
dll.display()
dll.backtraverse()
        
