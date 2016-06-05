import sys

class Node():
    
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

class BST():
    
    def __init__(self):
        self.root = None
        
    def inorder(self, l, x):
        if x != None:
            self.inorder(l, x.left)
            l.append(str(x.key))
            self.inorder(l, x.right)
            
    def preorder(self, l, x):
        if x != None:
            l.append(str(x.key))
            self.preorder(l, x.left)
            self.preorder(l, x.right)
            
    def postorder(self, l, x):
        if x != None:
            self.preorder(l, x.left)
            self.preorder(l, x.right)
            l.append(str(x.key))
    
    def search(self, k):
        x = self.root
        while x != None and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x
            
    def minimum(self, x):
        while x.left != None:
            x = x.left
        return x
    
    def maximum(self, x):
        while x.right != None:
            x = x.right
        return x
        
    def successor(self, x):
        if x == None:
            return None
        else:
            if x.right != None:
                return self.minimum(x.right)
            y = x.parent
            while y != None and x == y.right:
                x = y
                y = y.parent
            return y
        
    def predecessor(self, x):
        if x == None:
            return None
        else:
            if x.left != None:
                return self.maximum(x.left)
            y = x.parent
            while y != None and x == y.left:
                x = y
                y = y.parent
            return y
        
    def insert(self, z):
        z = Node(z)
        y = None
        x = self.root
        while x != None:
            y = x
            if z.key <= x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
            
    def transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != None:
            v.parent = u.parent
            
    def delete(self, z):
        z = self.search(z)
        if z.left == None:
            self.transplant(z, z.right)
        elif z.right == None:
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            
fileIn = open(sys.argv[1], mode = 'r')
fileOut = open(sys.argv[2], mode = 'w')

control = 0
case = 0
while control == 0:
    line = fileIn.readline()
    if line == '':
        control = 1
        break
    case += 1
    tree = BST()
    fileOut.write('Caso: '+str(case)+'\n')
    for i in range(int(line)):
        l = []
        seq = ''
        line = fileIn.readline().split()
        if line[0].upper() == 'A':
            tree.insert(int(line[1]))
        elif line[0].upper() == 'B':
            tree.delete(int(line[1]))
        elif line[0].upper() == 'C':
            value = tree.predecessor(tree.search(int(line[1])))
            if value:
                fileOut.write(str(value.key)+'\n')
            else:
                fileOut.write(str(0)+'\n')
        elif line[0].upper() == 'PRE':
            tree.preorder(l, tree.root)
            if l == []:
                fileOut.write(str(0)+'\n')
            else:
                for e in l:
                    seq += e+' '
                fileOut.write(seq+'\n')
        elif line[0].upper() == 'IN':
            tree.inorder(l, tree.root)
            if l == []:
                fileOut.write(str(0)+'\n')
            else:
                for e in l:
                    seq += e+' '
                fileOut.write(seq+'\n')
        elif line[0].upper() == 'POST':
            tree.postorder(l, tree.root)
            if l == []:
                fileOut.write(str(0)+'\n')
            else:
                for e in l:
                    seq += e+' '
                fileOut.write(seq+'\n')

fileIn.close()
fileOut.close()