'''
Created on 28 de abr de 2016

@author: Filipe Mei
'''
class SinlgyNode():
    
    def __init__(self, data):
        self.data = data
        self.nextNode = None
        
    def get_data(self):
        return self.data
    
    def set_data(self, data):
        self.data = data
    
    def get_nextNode(self):
        return self.nextNode
    
    def set_nextNode(self, node):
        self.nextNode = node
    
class SinglyLinkedList():
    
    def __init__(self):
        self.firstNode = None
        self.lastNode = None
        
    def __str__(self):
        if self.isEmpty():
            return "A lista esta vazia"
        string = "Lista: "
        currentNode = self.firstNode
        while currentNode is not None:
            string += str(currentNode.get_data()) + " "
            currentNode = currentNode.get_nextNode()
        return string
    
    def isEmpty(self):
        return self.firstNode is None
    
    def insertAtBegin(self, value):
        newNode = SinlgyNode(value)
        if self.isEmpty():
            self.firstNode = self.lastNode = newNode
        else:
            newNode.set_nextNode(self.firstNode)
            self.firstNode = newNode
            
    def insertAtEnd(self, value):
        newNode = SinlgyNode(value)
        if self.isEmpty():
            self.firstNode = self.lastNode = newNode
        else:
            self.lastNode.set_nextNode(newNode)
            self.lastNode = newNode
            
    def removeFromBegin(self):
        value = self.firstNode.get_data()
        if self.isEmpty():
            return None
        elif self.firstNode is self.lastNode:
            self.firstNode = self.lastNode = None
        else:
            self.firstNode = self.firstNode.get_nextNode()
        return value
            
    def removeFromEnd(self):
        value = self.lastNode.get_data()
        if self.isEmpty():
            return None
        elif self.firstNode is self.lastNode:
            self.firstNode = self.lastNode = None
        else:
            currentNode = self.firstNode
            while currentNode is not self.lastNode:
                prevNode = currentNode
                currentNode = currentNode.get_nextNode()
            prevNode.set_nextNode(None)
            self.lastNode = prevNode
        return value
    
    def removeNode(self, value):
        node = self.search(value)
        if node is None:
            return None
        if self.firstNode.get_data() is value:
            self.removeFromBegin()
        elif self.lastNode.get_data() is value:
            self.removeFromEnd()
        else:
            currentNode = self.firstNode
            while currentNode is not node:
                previous = currentNode
                currentNode = currentNode.get_nextNode()
            previous.set_nextNode(currentNode.get_nextNode())
            currentNode = None
            return value
                    
    def search(self, value):
        currentNode = self.firstNode
        while currentNode is not None:
            if currentNode.get_data() is value:
                break
            currentNode = currentNode.get_nextNode()
        return currentNode
    
class Stack(SinglyLinkedList):
    
    def push(self, value):
        self.insertAtBegin(value)
        
    def pop(self):
        self.removeFromBegin()