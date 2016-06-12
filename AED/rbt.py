class Node():
    def __init__(self, key, color, data = None):
        self.key = key
        self.color = color
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

class RBT():
    def __init__(self):
        self.nil = Node(None, 'black')
        self.root = None
        self.nil.left = self.nil
        self.nil.right = self.nil
        self.nil.parent = self.nil

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
        if x.right != self.nil:
            return self.minimum(x.right)
        y = x.parent
        while y != self.nil and x == y.right:
            x = y
            y = y.parrent
        return y

    def predecessor(self, x):
        if x.left != self.nil:
            return self.maximum(x.left)
        y = x.parent
        while y != self.nil and x == y.left:
            x = y
            y = y.parent
        return y

    def isEmpty(self):
        return self.root is self.nil

    def emptyTree(self):
        self.root = self.nil

    def left_rotate(self, node_a):
        node_b = node_a.right #Define a subarvore direita de A
        node_a.right = node_b.left #Faz a subarvore esquerda de B a subarvore direita de A
        node_b.left.parent = node_a
        node_b.parent = node_a.parent #Modifica o pai de B para o pai de A
        if node_a.parent is self.nil:
            self.root = node_b
        elif node_a is node_a.parent.left:
            node_a.parent.left = node_b
        else:
            node_a.parent.right = node_b
        node_b.left = node_a #Coloca o A como subarvore esquerda de B
        node_a.parent = node_b

    def right_rotate(self, node_b):
        node_a = node_b.left #Define a subarvore esquerda de B
        node_b.left = node_a.right #Faz a subarvore direita de A a subarvore esquerda de B
        node_a.right.parent = node_b
        node_a.parent = node_b.parent #Modifica o pai de A para o pai de B
        if node_b.parent is self.nil:
            self.root = node_b
        elif node_b is node_b.parent.left:
            node_b.parent.left = node_a
        else:
            node_b.parent.right = node_a
        node_a.right = node_b #Coloca o B como subarvore direita de A
        node_b.parent = node_a

    def rb_insert(self, key, data = None):
        node = Node(key, 'red', data)
        a = self.nil #instancio a variavel de apoio
        b = self.root #instancio a raiz da arvore
        while b is not self.nil:
            a = b
            if node.key < b.key:
                b = b.left
            else:
                b = b.right
        node.parent = a #coloco a instancia da variavel a como pai do node
        if a is self.nil:  #atribuo a posicao correta do node na arvore (se sera raiz, subarvore esquerda ou direita)
            self.root = a
        elif node.key < a.key:
            a.left = node
        else:
            a.right = node
        node.left = self.nil
        node.right = self.nil
        self.rb_insert_fixup(node) #correcao da arvore para respeitar as propriedades

    def rb_insert_fixup(self, node):
        while node.parent.color is 'red':
            if node.parent is node.parent.parent.left:
                b = node.parent.parent.right
                if b.color is 'red':
                    node.parent.color = 'black'
                    b.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                elif node is node.parent.right:
                    node = node.parent
                    self.left_rotate(node)
                node.parent.color = 'black'
                node.parent.parent.color = 'red'
                self.right_rotate(node.parent.parent)
            else:
                if node.parent is node.parent.parent.right:
                    b = node.parent.parent.left
                    if b.color is 'red':
                        node.parent.color = 'black'
                        b.color = 'black'
                        node.parent.parent.color = 'red'
                        node = node.parent.parent
                    elif node is node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.left_rotate(node.parent.parent)
        self.root.color = 'black'

    def rb_delete(self, node):
        if node.left is self.nil or node.right is self.nil:
            b = node
        else:
            b = self.successor(node)
        if b.left is not self.nil:
            a = b.left
        else:
            a = b.right
        '''
        a.parent  = b.parent
        '''
        if a is not self.nil:
            a.parent = b.parent
        if b.parent is self.nil:
            self.root = a
        elif b is b.parent.left:
            b.parent.left = a
        else:
            b.parent.right = a
        if b is not node:
            node.key = b.key
        if b.color is 'black':
            self.rb_delete_fixup(a)
        return b

    def rb_delete_fixup(self, x):
        while x is not self.root and x.color is 'black':
            if x is x.parent.left:
                w = x.parent.right
                if w.color is 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color is 'black' and w.right.color is 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.right.color is 'black':
                        w.left.color = 'black'
                        w.color = 'red'
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.right.color = 'black'
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color is 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color is 'black' and w.left.color is 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.left.color is 'black':
                        w.right.color = 'black'
                        w.color = 'red'
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.left.color = 'black'
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 'black'