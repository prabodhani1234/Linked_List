import DoublyLinkedList

linkedList=DoublyLinkedList.DoublyLinkedList()
linkedList.printForwardList()

print("\nDoubly Linked List is :")

linkedList.addNodeBeginning(18)
linkedList.addNodeBeginning(17)
linkedList.addNodeBeginning(16)
linkedList.addNodeBeginning(15)
linkedList.addNodeBeginning(13)
linkedList.addNodeBeginning(12)
linkedList.addNodeBeginning(11)
linkedList.addNodeInPos(3,14)
linkedList.addNodeEnd(19)
linkedList.printForwardList()

print("\n\nDoubly Linked List Print Backward :")
linkedList.printBackwardList()

print("\n\nDeleted First Node :")
linkedList.deleteFirstNode()
linkedList.printForwardList()

print("\n\nDeleted given position Node :")
linkedList.deleteNodeByPos(3)
linkedList.printForwardList()

print("\n\nDeleted Last Node :")
linkedList.deleteLastNode()
linkedList.printForwardList()

print("\n\nDoubly Linked List Element Search")
linkedList.searchValue(17)


