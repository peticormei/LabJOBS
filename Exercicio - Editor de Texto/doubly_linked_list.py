'''
Created on 29 de abr de 2016

@author: Filipe Mei
'''
class DoublyNode():
    
    def __init__(self, data):
        self.data = data
        self.nextNode = None
        self.prevNode = None
        
    def get_data(self):
        return self.data
    
    def set_data(self, data):
        self.data = data
        
    def get_prevNode(self):
        return self.prevNode
    
    def set_prevNode(self, node):
        self.prevNode = node
    
    def get_nextNode(self):
        return self.nextNode
    
    def set_nextNode(self, node):
        self.nextNode = node
        
class DoublyLinkedList():
    
    def __str__(self):
        "Override do Estatuto STRING"
        if self.isEmpty():
            return "A lista esta vazia!"
        currentNode = self.firstNode
        string = "A lista eh:"
        while currentNode is not None:
            string += str(currentNode.get_data()) + " "
            currentNode = currentNode.get_nextNode()
        return string
    
    def __init__(self):
        self.firstNode = None
        self.lastNode = None
        
    def isEmpty(self):
        return self.firstNode is None
    
    def insertAtBegin(self, value):
        newNode = DoublyNode(value)
        if self.firstNode is None:
            self.firstNode = self.lastNode = newNode
        else:
            newNode.set_nextNode(self.firstNode)
            self.firstNode = newNode
            print(self.firstNode.get_nextNode().get_data())
            print(self.firstNode.get_prevNode().get_data())
    
    def insertAtEnd(self, value):
        newNode = DoublyNode(value)
        if self.lastNode is None:
            self.firstNode = self.lastNode = newNode
        else:
            newNode.set_prevNode(self.lastNode)
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
            previousNode = self.lastNode.get_prevNode()
            previousNode.set_nextNode(None)
            self.lastNode.set_prevNode(None)
            self.lastNode = previousNode
        return value
    
    def removeNode(self, value):
        node = self.search(value)
        if node is None:
            return None
        currentNode = self.firstNode
        while currentNode is not node:
            currentNode = currentNode.get_nextNode()
        previousNode = currentNode.get_prevNode()
        nextNode = currentNode.get_nextNode()
        if currentNode is self.firstNode:
            nextNode.set_prevNode(previousNode)
        elif currentNode is self.lastNode:
            previousNode.set_nextNode(nextNode)
        else:
            previousNode.set_nextNode(nextNode)
            nextNode.set_prevNode(previousNode)
        currentNode = None
        return value
        
    def search(self, value):
        currentNode = self.firstNode
        while currentNode.get_data() is not value:
            currentNode = currentNode.get_nextNode()
        if currentNode.get_data() == value:
            return currentNode
        return None
    
    def clean_out(self):
        self.firstNode = self.lastNode = None
    
class Stack(DoublyLinkedList):
    
    def push(self, value):
        self.insertAtBegin(value)
        
    def pop(self):
        self.removeFromBegin()
    