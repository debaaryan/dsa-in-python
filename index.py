# create a Node with data which initially points to None
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# create a Singly Linked List which is initially empty
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # make the Linked List iterable, this fn gets called when we run for / while loop over object of this class
    def __iter__(self):
        node = self.head
        # if head is not empty then return the nodes one by one
        while node:
            yield node
            node = node.next

    # insertion in Linked List
    def insertSLL(self, data, locationIndex):
        # create a node
        newNode = Node(data)

        # if no node is there in SLL then make the head point to the newly created node
        if self.head is None:
            self.head = newNode

        # if SLL is not empty then 3 cases can happen : insertion at beginning, at end or at middle
        else:

            # insertion at beginning
            if locationIndex == 0:
                newNode.next = self.head
                self.head = newNode

            # insertion at end
            elif locationIndex == -1:
                temp = self.head
                # starting from first node, run until temp.next is None i.e. last node is reached, then temp will hold last node
                while temp.next:
                    temp = temp.next
                # make the new node to point None, and last node to point new node
                temp.next = newNode

            # insertion at middle
            else:
                prevNode = self.head
                index = 0
                # starting from first node, go to the previous node of desired location index
                while index < locationIndex - 1:
                    prevNode = prevNode.next
                    index += 1
                # make prev node to point to the new node and new node to point to the next node which prev node was pointing till now
                nextNode = prevNode.next
                prevNode.next = newNode
                newNode.next = nextNode

    # traversing singly linked list i.e. going through one after another node and printing their data
    def traverseSLL(self):
        if self.head is None:
            print("The Singly Linked List does not exist")
        else:
            node = self.head
            while node:
                print(node.data, end=" ")
                node = node.next

    # search for a node in singly linked list


# create a Singly Linked List object, create first node object of Linked List, add next nodes after that
sll = SinglyLinkedList()
sll.traverseSLL()  # The Singly Linked List does not exist
sll.insertSLL(20, 1)  # [20]
sll.insertSLL(40, 1)  # [20, 40]
sll.insertSLL(30, 1)  # [20, 30, 40]
sll.insertSLL(50, 3)  # [20, 30, 40, 50]
sll.insertSLL(60, -1)  # [20, 30, 40, 50, 60]
sll.insertSLL(10, 0)  # [10, 20, 30, 40, 50, 60]
print([node.data for node in sll])

# traverse linked list and print all data contained in its nodes
sll.traverseSLL()  # 10 20 30 40 50 60
