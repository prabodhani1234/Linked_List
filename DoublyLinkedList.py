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
    def printBackwardList(self):
        if self.head is None:  # checking head node is none
            print("Empty Doubly Linked List")
        else:
            newNode = self.head
            while newNode.getNext() is not None:  # running until next of new node is none
                newNode = newNode.getNext()  # making next of new node as new node
            while newNode is not None:  # if new node is not none
                print(newNode.data)  # print data of new node
                newNode = newNode.getPrev()  # making previous of new node as new node

    # add new node in the beginning
    def addNodeBeginning(self, data):
        newNode = Node(data)  # getting node expect data into new node
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

    def addNodeInPos(self, pos, data):
        if pos < self.length - 1 and pos < 0:
            return None
        elif pos == self.length - 1:
            self.addNodeEnd(data)
        elif pos == 0:
            self.addNodeBeginning(data)
        else:
            newNode = Node(data)
            current = self.head
            for i in range(0, pos - 1):
                current = current.getNext()

            newNode.setPrev(current)
            newNode.setNext(current.next)
            current.next.setPrev(newNode)
            current.setNext(newNode)

    # delete first node of the doubly linked list
    def deleteFirstNode(self):
        if self.head is None:
            print("Empty Doubly Linked List")
        else:
            self.head = self.head.getNext()  # equaling next of head node to head node
            self.head.setPrev(None)  # set previous of head as none
        self.length -= 1

    # delete last node of the doubly linked list
    def deleteLastNode(self):
        if self.head is None:
            print("Empty Doubly Linked List")
        else:
            current = self.head  # equaling head node to current
            previous = None # equaling previous node of current node to none
            while current.getNext() is not None: # running next of current node is none
                previous = current # equaling current node to previous node
                current = current.getNext() # equaling next of current node to current node
            previous.setNext(None) # set next of previous node as none
        self.length -= 1

    # delete given position node
    def deleteNodeByPos(self, Pos):
        if self.head is None:
            print("Empty Doubly Linked List")
            return None
        if self.length > Pos > -1: # checking length greater than position and one mines less than position
            if Pos == 0: # checking position is equal to zero
                self.deleteFirstNode() # running deleteFirstNode function
            elif Pos == self.length - 1: # checking position is equal to length mines one
                self.deleteLastNode() # running deleteLastNode function
            else:
                count = 0
                current = self.head
                while count != Pos - 1: # checking position mines one not equal to count
                    count += 1
                    current = current.getNext() # equaling next of current node as current
                # equaling next of next node in current node to next of current node
                current.setNext(current.next.getNext())
                # equaling current node to previous of next node in current node
                current.next.setPrev(current)
            self.length -= 1

    # search element of doubly linked list
    def searchNodeByPos(self, element):
        if self.head is None:
            print("Empty Doubly Linked List")
        else:
            current = self.head
            count = 0
            while current is not None: # checking current is not none
                if current.getData() == element: # checking search element equal to data of current node
                    print("This Element in Doubly Linked List :", count) # print count number

                    # printing next node and previous node of search element node
                    if current.getNext() is None: # checking next of current node is none
                        # equaling data of previous node of current node to currentPrev variable
                        currentPrev = current.prev.getData()
                        currentNext = "None" # equaling "None" to currentNext variable

                    elif current.getPrev() is None: # checking previous of current node is none
                        currentPrev = "None" # equaling "None" to currentPrev variable
                        # equaling data of next node of current node to currentNext variable
                        currentNext = current.next.getData()
                    else:
                        # equaling data of previous node of current node to currentPrev variable
                        currentPrev = current.prev.getData()
                        # equaling data of next node of current node to currentNext variable
                        currentNext = current.next.getData()
                    # print next and previous node
                    print('\nPrevious Node is :{} \nNext Node is :{}'.format(currentPrev, currentNext))
                current = current.getNext() # equaling next of current node to current
                count += 1