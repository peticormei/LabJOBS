from singly_linked_list import SinglyLinkedList

x = SinglyLinkedList()
x.insertAtBegin(5)
x.insertAtBegin(10)
x.insertAtBegin(15)
x.insertAtBegin(None)
print(x.search(None))
print(x.__str__())