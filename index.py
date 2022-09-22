# create a Node to be inserted in Linked list. Each node will have info and link. If no link is provided then it will have None
class Node:
    # constructor
    def __init__(self, data):
        self.data = data
        self.next = None


a = Node(13)
b = Node(15)
a.next = b
print(a.data)
print(b.data)
print(a.next.data)
print(a)
print(a.next)
print(b)
print(b.next.data)

# creating a Linked list and inserting an element into it
# class LinkedList:
#     def __init__(self):
#         # initially head is pointing to None
#         self.head = None

#         # can add element either at the beginning or at the end of list
#         # insert the element at beginning with given input value, info
#         def insert_at_beginning(self, info):
#             # create a new node object using Node class
#             newNode = Node(info)


# LL = LinkedList()
# LL.insert_at_beginning(10)
