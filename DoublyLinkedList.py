from Node import Node


class DoublyLinkedList:
    def __init__(self):  # defining variable
        self.head = None  # initially first node is none
        self.tail = None  # initially last node is none
        self.length = 0  # initially doubly linked list length is zero

    # Doubly Linked List length size
    def doublyListLength(self):
        current = self.head  # create current variable as head node
        count = 0  # creating count as zero
        while current is not None:  # checking current node is not none
            count += 1
            current = current.getNext()  # change current as next of current node
        return count

    # this function print contend of all doubly linked
    def printForwardList(self):
        if self.head is None:  # checking head node is none
            print("Empty Doubly Linked List")
        else:
            current = self.head
            while current is not None:  # checking current node is not none
                print(current.getData())  # print data of current node
                current = current.getNext()  # change current as next of current node

    # this function reverse all linked
    def printBackwardList(self):
        if self.head is None:  # checking head node is none
            print("Empty Doubly Linked List")
        else:
            newNode = self.head
            while newNode.getNext() is not None:  # traversing to last node in the list
                newNode = newNode.getNext()  # change next of new node as new node
            while newNode is not None:  # traversing until first node in the list
                print(newNode.data)  # print data of new node
                newNode = newNode.getPrev()  # change previous of new node as new node

    # add new node in the beginning
    def addNodeBeginning(self, data):
        newNode = Node(data)
        newNode.setData(data)
        if self.head is None:  # checking head Node is Node
            self.head = newNode  # create new node as head node
        else:
            newNode.setNext(self.head)  # create next of new node as head node
            self.head.setPrev(newNode)  # create previous of head node as newNode
            newNode.setPrev(None)  # create previous of new node as none
            self.head = newNode  # change new node as head node
        self.length += 1  # adding one to length

    # add new node in the end of the doubly linked list
    def addNodeEnd(self, data):
        newNode = Node(data)
        newNode.setData(data)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.getNext() is not None:  # traversing until the last node in the list
                current = current.getNext()  # change next of current as current
            current.setNext(newNode)  # create next of current as new node
            newNode.setPrev(current)  # create previous of new node as current
        self.length += 1

    # add new node in given position of the doubly linked list
    def addNodeInPos(self, pos, data):
        # checking position is greater than length mines one or position is less than zero
        if pos > self.length - 1 or pos < 0:
            return None
        elif pos == self.length - 1:  # checking position is equal to length mines one
            self.addNodeEnd(data)  # running addNodeEnd function
        elif pos == 0:  # checking position is equal to zero
            self.addNodeBeginning(data)  # running addNodeBeginning
        else:
            newNode = Node(data)
            current = self.head
            for i in range(0, pos - 1):  # traversing until the previous node before the position
                current = current.getNext()  # change next of current as current

            newNode.setPrev(current)  # create previous of new node as current
            newNode.setNext(current.next)  # create next of new node as next of current
            current.next.setPrev(newNode)  # create previous of next in current as new node
            current.setNext(newNode)  # create next of current as new node

    # delete first node of the doubly linked list
    def deleteFirstNode(self):
        if self.head is None:
            print("Empty Doubly Linked List")
        else:
            self.head = self.head.getNext()  # change next of head as head
            self.head.setPrev(None)  # create previous of head as none
        self.length -= 1

    # delete last node of the doubly linked list
    def deleteLastNode(self):
        if self.head is None:
            print("Empty Doubly Linked List")
        else:
            current = self.head
            previous = None  # create previous node as none
            while current.getNext() is not None:  # traversing until the last node in the list
                previous = current  # change current as previous
                current = current.getNext()  # change next of current as current
            previous.setNext(None)  # create next of precious as none
        self.length -= 1

    # delete given position node
    def deleteNodeByPos(self, Pos):
        if self.head is None:
            print("Empty Doubly Linked List")
            return None
        if self.length > Pos > -1:  # checking length greater than position and one mines less than position
            if Pos == 0:  # checking position is equal to zero
                self.deleteFirstNode()  # running deleteFirstNode function
            elif Pos == self.length - 1:  # checking position is equal to length mines one
                self.deleteLastNode()  # running deleteLastNode function
            else:
                count = 0
                current = self.head
                while count != Pos - 1:  #
                    count += 1
                    current = current.getNext()  # change next of current as current
                # create next of current as next of next in current
                current.setNext(current.next.getNext())
                # create previous of next in current as current
                current.next.setPrev(current)
            self.length -= 1

    # search element of doubly linked list
    def searchNodeByPos(self, element):
        if self.head is None:
            print("Empty Doubly Linked List")
        else:
            current = self.head
            count = 0
            while current is not None:  # traversing until current node is none
                if current.getData() == element:  # checking search element equal to data of current node
                    print("This Element in Doubly Linked List :", count)  # print count number

                    # printing next node and previous node of search element node
                    if current.getNext() is None:  # checking next of current node is none
                        # assign data of previous in current node to currentPrev variable
                        currentPrev = current.prev.getData()
                        currentNext = "None"  # assign "None" string to currentNext variable

                    elif current.getPrev() is None:  # checking previous of current node is none
                        currentPrev = "None"  # assign "None" string to currentPrev variable
                        # assign data of next in current node to currentNext variable
                        currentNext = current.next.getData()
                    else:
                        # assign data of previous in current node to currentPrev variable
                        currentPrev = current.prev.getData()
                        # assign data of next in current node to currentNext variable
                        currentNext = current.next.getData()
                    # print next and previous node
                    print('\nPrevious Node is :{} \nNext Node is :{}'.format(currentPrev, currentNext))
                current = current.getNext()  # change next of current as current
                count += 1
