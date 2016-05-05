from doubly_linked_list import DoublyLinkedList

x = DoublyLinkedList()
x.insertAtBegin(5)
x.insertAtBegin(10)
x.insertAtBegin(15)
x.clean_out()
print(x.__str__())