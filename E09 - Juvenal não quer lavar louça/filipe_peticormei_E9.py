import sys

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

    def getFirstNode(self):
        return self.firstNode

fileIn = open(sys.argv[1], mode = 'r')
fileOut = open(sys.argv[2], mode = 'w')

party = int(fileIn.readline())
if party > 0 and party <= 10 ** 5:
    for i in range(1, party + 1):

        k = 0
        list_palyers = []
        deck_list = SinglyLinkedList()

        deck = fileIn.readline().split()
        for c in deck:
            deck_list.insertAtEnd(c)
        while True:
            player = fileIn.readline().split()
            plays_list = SinglyLinkedList()
            if player[0] == '-1':
                break
            for c in player:
                plays_list.insertAtEnd(c)
            list_palyers.append(plays_list)
        for i in range(1000):
            piece = deck_list.getFirstNode().get_data()
            for p in list_palyers:
                if piece == p.getFirstNode().get_data():
                    p.removeFromBegin()
                else:
                    value = p.getFirstNode().get_data()
                    p.insertAtEnd(value)
                    p.removeFromBegin()
            value = deck_list.getFirstNode().get_data()
            deck_list.insertAtEnd(value)
            deck_list.removeFromBegin()
            for p in list_palyers:
                if p.isEmpty() is True:
                    k = list_palyers.index(p) + 1
                    break
            if k > 0:
                break
        if k > 0:
            fileOut.write(str(k)+'\n')
        else:
            fileOut.write(str(k)+'\n')
else:
    fileOut.write('Valor de F nao respeita a restricao\n')

fileIn.close()
fileOut.close()
