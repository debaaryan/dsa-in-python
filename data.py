class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    # make the node object to print as it's data
    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elm in nodes:
                node.next = Node(elm)
                node = node.next

    # function to add a node at the beginning of LinkedList
    def add_first(self, node):
        # connect rest of the nodes with the new node by assigning value inside head of linked list into the new node
        node.next = self.head
        # set the head of LinkedList equal to the new node we passed
        self.head = node

    # function to add a node at the end of LinkedList
    def add_last(self, node):
        # if head is None (as not None is true) i.e. empty Linkedlist means cannot traverse then set the head to the new node and stop method execution
        if not self.head:
            self.head = node
            return
        # trick : run a for loop over current LL object where a local variable will hold each node in each iteration. Loop will run even though there is no statement inside for loop. At the end local variable will hold the last node of linked list object
        for current_node in self:
            pass
        # local variable holds the last node of current LL, set it to hold address of newly passed node
        current_node.next = node

    # function to add a node between two existing node of LinkedList

    # make the linked list iterable so that we can go through its one by one node
    def __iter__(self):
        # set the current node to be equal to the head of linked list
        node = self.head
        while node is not None:
            # return the current node and set the current node to next one
            # yield is same as return but difference is after returning yield does not stop currrent method execution
            yield node
            node = node.next

    # make the linked list object to print as it's nodes joined via -> symbol
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


strings = ["first", "second", "third"]
llist = LinkedList(strings)
# LinkedList object can now be printed
print(llist)  # first -> second -> third -> None
# LinkedList object is now iterable
for node in llist:
    print(node)  # first  second  third

llist.add_first(Node("zeroth"))
print(llist)  # zeroth -> first -> second -> third -> None

llist.add_last(Node("fourth"))
print(llist)  # zeroth -> first -> second -> third -> fourth -> None


# llist = LinkedList()
# print(llist)
# first_node = Node("a")
# llist.head = first_node

# second_node = Node("b")
# third_node = Node("c")
# first_node.next = second_node
# second_node.next = third_node
# print(llist)
