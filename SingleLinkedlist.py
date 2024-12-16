# single linked list witha all operations
class node():
    def __init__(self,data):
        self.data=data
        self.next=None
class SingleLinkedlist():
    def __init__(self):
        self.head=None
    def travel(self):
        if self.head==None:
            print("The list is empty")
        else:
            a=self.head
            while a is not None:
                print(a.data,end=" ")
                a=a.next
# ..........................................
    def insert_in_first(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node
    def insert_in_last(self,data):
        new_node=node(data)
        a=self.head
        while a.next is not None:
            a=a.next
        a.next=new_node
    def insert_in_mid(self,data,position):
        new_node=node(data)
        a=self.head
        for i in range(position-1):
            a=a.next
        new_node.next=a.next
        a.next = new_node
    def delete_in_first(self):
        a=self.head
        self.head=a.next
        a.next=None
    def delete_in_last(self):
        prev=self.head
        a=self.head.next
        while a.next is not None:
            a=a.next
            prev=prev.next
        prev.next=None
    def delete_in_mid(self,position):
        prev=self.head
        a=self.head.next
        for i in range(1,position-1):
            a=a.next
            prev=prev.next
        prev.next=a.next
        a.next=None
n1=node(10)
sll=SingleLinkedlist()
sll.head=n1
n2=node(20)
n1.next=n2
n3=node(30)
n2.next=n3
n4=node(40)
n3.next=n4
sll.insert_in_first(9)
sll.insert_in_last(44)
sll.insert_in_mid(15,2)
sll.delete_in_first()
sll.delete_in_last()
sll.delete_in_mid(1)
sll.travel()

m1=node(2)
linkedlist=SingleLinkedlist()
linkedlist.head=m1
m2=node(4)
m1.next=m2
m3=node(6)
m2.next=m3
m4=node(8)
m3.next=m4
print()
linkedlist.travel()
