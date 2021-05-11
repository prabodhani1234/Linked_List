class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getNext(self):
        return self.next

    def setNext(self, address1):
        self.next = address1

    def getPrev(self):
        return self.prev

    def setPrev(self, address2):
        self.prev = address2

    def hasNext(self):
        return self.next is not None

    def hasPrev(self):
        return self.prev is not None
