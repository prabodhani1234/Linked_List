from Node import Node  # import Node class in Node python file


class DoublyLinkedList:
    def __init__(self):  # define variable
        self.head = None  # initially first node is none
        self.tail = None  # initially last node is none
        self.length = 0  # initially doubly linked list length is zero

    def doublyListLength(self):  # define length function
        current = self.head  # creating variable as current and head node assign it
        count = 0  # creating count is zero
        while current is not None:  # running until the current is None
            count += 1  # adding one
            current = current.getNext()  # equaling current next node to current
        print("Doubly Linked List Length is :",count) # print count

