import DoublyLinkedList

linkedList=DoublyLinkedList.DoublyLinkedList()
linkedList.printForwardList()

print("\nDoubly Linked List is :")

linkedList.addNodeBeginning(9)
linkedList.addNodeBeginning(8)
linkedList.addNodeBeginning(7)
linkedList.addNodeBeginning(3)
linkedList.addNodeBeginning(2)
linkedList.addNodeBeginning(1)
linkedList.addNodeBeginning(0)
linkedList.addNodeEnd(13)
linkedList.addNodeInPos(7,10)
linkedList.printForwardList()

print("\nDoubly Linked List Print Backward")
linkedList.printBackwardList()

print("\nDeleted First Node in Doubly Linked List :")
linkedList.deleteFirstNode()
linkedList.printForwardList()

print("\nDeleted given position Node in Doubly Linked List :")
linkedList.deleteNodeByPos(3)
linkedList.printForwardList()

print("\nDeleted Last Node in Doubly Linked List :")
linkedList.deleteLastNode()
linkedList.printForwardList()

print("\n\nDoubly Linked List Element Search")
linkedList.searchValue(2)


