import sys, math

class Node():
	def __init__(self, data):
		self.data = data
		self.nextNode = None

	def getData(self):
		return self.data

	def getNextNode(self):
		return self.nextNode

	def setNextNode(self, nextNode):
		self.nextNode = nextNode

class Stack():
	def __init__(self):
		self.fristNode = None

	def isEmpty(self):
		if self.fristNode is None:
			return True
		return False

	def push(self, data):
		newNode = Node(data)
		if self.isEmpty is True:
			self.fristNode = newNode
		else:
			newNode.setNextNode(self.fristNode)
			self.fristNode = newNode

	def pop(self):
		currentNode = self.fristNode
		self.fristNode = currentNode.getNextNode()
		currentNode.setNextNode(None)
		return currentNode.getData()

fileIn = open(sys.argv[1], mode = 'r')
fileOut = open(sys.argv[2], mode = 'w')

def add(op1, op2):
	return op1 + op2

def sub(op1, op2):
	return op1 - op2

def mult(op1, op2):
	return op1 * op2

def div(op1, op2):
	a = op1 / op2
	if a > 0:
		return math.floor(a)
	return math.ceil(a)

for line in fileIn:
	stack = Stack()
	line = line.split()
	line.reverse()
	cases = {
			'+':add,
			'-':sub,
			'*':mult,
			'/':div
			}
	for e in line:
		if e.isdigit():
			stack.push(int(e))
		else:
			op1 = stack.pop()
			op2 = stack.pop()
			stack.push(cases[e](op1, op2))
	fileOut.write(str(stack.pop())+'\n')

fileIn.close()
fileOut.close()
