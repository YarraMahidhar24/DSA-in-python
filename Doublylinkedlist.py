# Doubly Linked List >>>>>>>>>>>>>>>>>>>>>>>>>>
class node():
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class dll():
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
    def Reverse_travel(self):
        if self.head==None:
            print("The list is empty")
        else:
            a=self.head
            while a.next is not None:
                a=a.next
            while a is not None:
                print(a.data,end=" ")
                a=a.prev
# ..........................................
    def insert_in_first(self,data):
        new_node=node(data)
        a=self.head
        new_node.next=a
        a.prev=new_node
        self.head=new_node
    def insert_in_last(self,data):
        new_node = node(data)
        a=self.head
        while a.next is not None:
            a=a.next
        new_node.prev=a
        a.next=new_node
    def insert_in_mid(self,data,position):
        new_node = node(data)
        a=self.head
        b=self.head.next
        for i in range(position-1):
            a=a.next
            b=b.next
        a.next=new_node
        b.prev=new_node
        new_node.next=b
        new_node.prev=a
        pass
    def delete_in_first(self):
        a=self.head
        b=a.next
        self.head=b
        b.prev=None
    def delete_in_last(self):
        a=self.head
        while a.next is not None:
            a=a.next
        b=a.prev
        b.next=None
    def delete_in_mid(self,position):
        p=self.head
        a=p.next
        n=a.next
        for i in range(position-1):
            a=a.next
            p=p.next
            n=n.next
        p.next=n
        n.prev=p
n1=node(5)
dll=dll()
dll.head=n1
n2=node(10)
n1.next=n2
n2.prev=n1
n3=node(15)
n2.next=n3
n3.prev=n2
n4=node(20)
n3.next=n4
n4.prev=n3
dll.insert_in_first(1)
dll.delete_in_first()
dll.insert_in_last(25)
dll.delete_in_last()
dll.insert_in_mid(99,2)
dll.delete_in_mid(2)
dll.travel()
print()
dll.Reverse_travel()
