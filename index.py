class Node:
    # constructor
    def __init__(self, info, link=None):
        self.info = info
        self.link = link


# creating a single Node with value 10
first = Node(10)
print(first.info)

# inserting an element into linked list


class LinkedList:
    def __init__(self):
        self.head = None


LL = LinkedList()
