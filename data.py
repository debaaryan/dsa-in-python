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
    def add_first(self, new_node):
        # connect rest of the nodes with the new node by assigning value inside head of linked list into the new node
        new_node.next = self.head
        # set the head of LinkedList equal to the new node we passed
        self.head = new_node

    # function to add a node at the end of LinkedList
    def add_last(self, new_node):
        # if head is None (as not None is true) i.e. empty Linkedlist means cannot traverse then set the head to the new node and stop method execution
        if not self.head:
            self.head = new_node
            return
        # trick : run a for loop over current LL object where a local variable will hold each node in each iteration. Loop will run even though there is no statement inside for loop. At the end local variable will hold the last node of linked list object
        for current_node in self:
            pass
        # local variable holds the last node of current LL, set it to hold address of newly passed node
        current_node.next = new_node

    # function to add a node between two existing node of LinkedList. Two ways : either after or before an existing node
    # function to add a node after an existing node
    def add_after(self, target_node_data, new_node):
        # check whether LL is empty. If head is pointing to None i.e. empty LL then raise exception
        if not self.head:
            raise Exception("List is empty")
        # iterate through current LL object, if given data matches with any node then assign value of its next instance variable to new node's next so that we can go from new node to rest of the nodes.
        # also make the node with target data as previous node of the new node. Stop the loop after finding target node
        # so node with target data < new node < node previously pointed by node with target data
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("That data wasn't found in the list :(")

    # function to add a node before an existing node
    def add_before(self, target_node_data, new_node):
        # check whether LL is empty, then raise exception
        if not self.head:
            raise Exception("List is empty")

        # also check whether the target data matches with first node, then there won't be any node before new node, new node will be the first node i.e. head will point to new node and new node will point to current first node which currently is stored in head then stop execution
        if self.head.data == target_node_data:
            new_node.next = self.head
            self.head = new_node
            return

        # if LL is not empty and first node also does not match with target data then make the first node as previous node because first node does not have target data as checked beforehand
        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                # if node with target data found then make the last checked node to point to the new node and new node point to the node with target data
                # so prev node < new node < node with target data
                prev_node.next = new_node
                new_node.next = node
                return
            # after each iteration make the node just checked as previous node
            prev_node = node

        raise Exception("That data wasn't found in the list :(")

    # removing a node : find the node with target data > link the node immediately before it to the node after target node. It's tricky in LL to go from target node to its previous node

    # make the linked list iterable so that we can go through its one by one node
    def __iter__(self):
        # set the current node to be equal to the head of linked list
        node = self.head
        while node is not None:
            # return the current node and set the current node to next one
            # yield is same as return but difference is after returning, yield does not stop currrent method execution
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
llist1 = LinkedList(strings)
# LinkedList object can now be printed
print(llist1)  # first -> second -> third -> None
# LinkedList object is now iterable
for node in llist1:
    print(node)  # first  second  third

llist1.add_first(Node("zeroth"))
print(llist1)  # zeroth -> first -> second -> third -> None

llist1.add_last(Node("fourth"))
print(llist1)  # zeroth -> first -> second -> third -> fourth -> None

llist2 = LinkedList()
# llist2.add_before("a", Node("a"))  # Exception: List is empty

llist3 = LinkedList(["b", "d"])
llist3.add_before("b", Node("a"))
print(llist3)  # a -> b -> d -> None
llist3.add_after("b", Node("c"))
print(llist3)  # a -> b -> c -> d -> None
