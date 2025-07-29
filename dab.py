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
        if self.head is None:
            self.head=newnode
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp
    def dab(self):
        if not self.head:
            print("cant perform delete opration in any empty list")
        print(f"deleted :{self.head.data}")
        self.head=self.head.next
        if self.head:
            self.head.prev=None
            
        

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
d=int(input("\n how many times do you want to perform delete operation "))
for _ in range(d):
    dll.dab()
    dll.display()
    
        
