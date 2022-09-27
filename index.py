# create a node which initially points to None
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# create a singly linked list which is initially empty
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end=" ")
                temp = temp.next


# create a singly linked list object
sll = SinglyLinkedList()
# display the linked list
# sll.display()  # Linked list is empty
# create first node
n1 = Node(10)
# now head pointing to first created node
sll.head = n1
# sll.display()  # 10, data of first node
# create other nodes
n2 = Node(20)
n1.next = n2
n3 = Node(30)
n2.next = n3
sll.display()  # 10 --> 20 --> 30 -->
