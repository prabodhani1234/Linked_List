import DoublyLinkedList

linkedList=DoublyLinkedList.DoublyLinkedList()
linkedList.printForwardList()

print("\nDoubly Linked List is :")

linkedList.addNodeBeginning(4)
linkedList.addNodeBeginning(2)
linkedList.addNodeBeginning(1)
linkedList.addNodeEnd(5)
linkedList.addNodeBeginning(0)
linkedList.addNodeEnd(6)
linkedList.addNodeInPos(3,3)
linkedList.printForwardList()

print("\nDeleted First Node in Doubly Linked List :")
linkedList.deleteFirstNode()
linkedList.printForwardList()

print("\nDeleted given position Node in Doubly Linked List :")
linkedList.deleteNodeByPos(3)
linkedList.printForwardList()

print("\nDeleted Last Node in Doubly Linked List :")
linkedList.deleteLastNode()
linkedList.printForwardList()


print("\nDoubly Linked List Print Backward")
linkedList.printBackwardList()

print("\n\nDoubly Linked List Element Search")
linkedList.searchNodeByPos(2)


