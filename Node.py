class Node:

    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

    def getData(self):
        return self.data