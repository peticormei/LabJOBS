'''
Created on 29 de abr de 2016

@author: Filipe Mei
'''
from doubly_linked_list import DoublyLinkedList, Stack

import sys

fileIn = open(sys.argv[1], mode = 'r')
fileOut = open(sys.argv[2], mode = 'w')

y = 0
undo = Stack()
text = Stack()
form = DoublyLinkedList()
while True:
    line = fileIn.readline().split()
    if len(line) == 0:
        break
    elif line[0].lower() == 'adicionar':
        undo.clean_out()
        for i in range(1, len(line)):
            text.push(line[i])
    elif line[0].lower() == 'italico' or line[0].lower() == 'negrito':
        if form.isEmpty() is True:
            form.insertAtEnd(line[0].lower())
        else:
            s = form.search(line[0].lower())
            if s is None:
                form.insertAtEnd(line[0].lower())
            else:
                form.removeNode(line[0].lower())
    elif line[0].lower() == 'apagar':
        y = int(line[1])
        for i in range(y):
            x = text.pop()
            undo.push(x)
    elif line[0].lower() == 'desfazer':
        x = undo.pop()
        while x is not None:
            text.push(x)
    elif line[0].lower() == 'refazer':
        for i in range(y):
            x = text.pop()
            undo.push(x)


# t = ''
# x = text.firstNode.get_data()
# while x is not None:
#     t += x + ' '
#     x = text.firstNode.get_nextNode().get_data()
# t += ' | '
# y = form.firstNode.get_data()
# while y is not None:
#     t += y + ' '
#     y = form.firstNode.get_nextNode().get_data()
# fileOut.write(t)

fileIn.close()
fileOut.close()