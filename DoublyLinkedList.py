from Node import Node


class DoublyLinkedList:
    def __init__(self):  # define variable
        self.head = None  # initially first node is none
        self.tail = None  # initially last node is none
        self.length = 0  # initially doubly linked list length is zero

    # Doubly Linked List length size
    def doublyListLength(self):
        current = self.head  # creating variable as current and head node assign it
        count = 0  # creating count is zero
        while current is not None:  # running until the current is None
            count += 1
            current = current.getNext()  # making next of current node as current
        return count

    # this function print contend of all doubly linked
    def printForwardList(self):
        if self.head is None:  # checking head node is none
            print("Empty Doubly Linked List")
        else:
            current = self.head  # making head node as current
            while current is not None:  # running until the current is none
                print(current.getData())  # print data of current node
                current = current.getNext()  # making next of current node as current

    # this function reverse all linked
    def printBackward(self):
        if self.head is None:  # checking head node is none
            print("Empty Doubly Linked List")
        else:
            newNode = self.head
            while newNode.getNext() is not None:# running until next of new node is none
                newNode = newNode.getNext()  # making next of new node as new node
            while newNode is not None:  # if new node is not none
                print(newNode.data)  # print data of new node
                newNode = newNode.getPrev()  # making previous of new node as new node

    # add new node in the beginning
    def addNodeBeginning(self, data):
        newNode = Node(data) # getting node expect data into new node
        newNode.setData(data)
        if self.head is None:  # checking head Node is Node
            self.head = newNode  # making new node as head node
        else:
            newNode.setNext(self.head)  # making head node as next of new node
            self.head.setPrev(newNode)  # making newNode as previous of head node
            newNode.setPrev(None)  # making none as previous of next node
            self.head = newNode
        self.length += 1  # adding one to length

    # add new node in the end of the doubly linked list
    def addNodeEnd(self, data):
        newNode = Node(data)
        newNode.setData(data)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head  # equaling head node to current variable
            while current.getNext() is not None:  # if next of current is not none
                current = current.getNext()  # equaling get next of current node to current
            current.setNext(newNode)  # making new node as next of current
            newNode.setPrev(current)  # making current as previous of new node
        self.length += 1



