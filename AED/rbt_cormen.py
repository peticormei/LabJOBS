class Node():
    def __init__(self, key, color, data = None):
        self.key = key
        self.color = color
        self.data = data
        self.p = None
        self.left = None
        self.right = None

class RBT():
    def __init__(self):
        self.nil = Node(None, 'black')
        self.root = self.nil
        self.nil.left = self.nil
        self.nil.right = self.nil
        self.nil.p = self.nil
        
    def inorder_tree_walk(self, x):
        if x != self.nil:
            self.inorder_tree_walk(x.left)
            print(x.key)
            self.inorder_tree_walk(x.right)
            
    def preorder_tree_walk(self, x):
        if x != self.nil:
            print(x.key)
            self.preorder_tree_walk(x.left)
            self.preorder_tree_walk(x.right)
            
    def postorder_tree_walk(self, x):
        if x != self.nil:
            self.preorder_tree_walk(x.left)
            self.preorder_tree_walk(x.right)
            print(x.key)
        
    def search(self, k):
        x = self.root
        while x != self.nil and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x
            
    def minimum(self, x):
        while x.left != self.nil:
            x = x.left
        return x
    
    def maximum(self, x):
        while x.right != self.nil:
            x = x.right
        return x
        
    def successor(self, value):
        x = self.search(value)
        if x == self.nil:
            return self.nil.key
        else:
            if x.right != self.nil:
                return self.minimum(x.right).key
            y = x.p
            while y != self.nil and x == y.right:
                x = y
                y = y.p
            return y.key
        
    def predecessor(self, value):
        x = self.search(value)
        if x == self.nil:
            return self.nil.key
        else:
            if x.left != self.nil:
                return self.maximum(x.left).key
            y = x.p
            while y != self.nil and x == y.left:
                x = y
                y = y.p
            return y.key
        
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.p = x
        y.p = x.p
        if x.p == self.nil:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y
        
    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.nil:
            x.right.p = y
        x.p = y.p
        if y.p == self.nil:
            self.root = x
        elif y == y.p.right:
            y.p.right = x
        else:
            y.p.left = x
        x.right = y
        y.p = x
        
    def rb_insert(self, value, data = None):
        z = Node(value, 'red', data)
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        self.rb_insert_fixup(z)
        
    def rb_insert_fixup(self, z):
        while z.p.color == 'red':
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.color == 'red':
                    z.p.color = 'black'
                    y.color = 'black'
                    z.p.p.color = 'red'
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p
                        self.left_rotate(z)
                    z.p.color = 'black'
                    z.p.p.color = 'red'
                    self.right_rotate(z.p.p)
            else:
                if z.p == z.p.p.right:
                    y = z.p.p.left
                    if y.color == 'red':
                        z.p.color = 'black'
                        y.color = 'black'
                        z.p.p.color = 'red'
                        z = z.p.p
                    else:
                        if z == z.p.left:
                            z = z.p
                            self.right_rotate(z)
                        z.p.color = 'black'
                        z.p.p.color = 'red'
                        self.left_rotate(z.p.p)
        self.root.color = 'black'
            
    def rb_transplant(self, u, v):
        if u.p == self.nil:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p
            
    def rb_delete(self, value):
        z = self.search(value)
        y = z
        y_original_color = y.color
        if z.left == self.nil:
            x = z.right
            self.rb_transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.p == z:
                x.p = y
            else:
                self.rb_transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.rb_transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
        if y_original_color == 'black':
            self.rb_delete_fixup(x)
    
    def rb_delete_fixup(self, x):
        while x != self.root and x.color == 'black':
            if x == x.p.left:
                w = x.p.right
                if w.color == 'red':
                    w.color = 'black'
                    x.p.color = 'red'
                    self.left_rotate(x.p)
                    w = x.p.right
                if w.left.color == 'black' and w.right.color == 'black':
                    w.color == 'red'
                    x = x.p
                else:
                    if w.right.color == 'black':
                        w.left.color = 'black'
                        w.color = 'red'
                        self.right_rotate(w)
                        w = x.p.right
                    w.color = x.p.color
                    x.p.color = 'black'
                    w.right.color = 'black'
                    self.left_rotate(x.p)
                    x = self.root
            else:
                w = x.p.left
                if w.color == 'red':
                    w.color = 'black'
                    x.p.color = 'red'
                    self.right_rotate(x.p)
                    w = x.p.left
                if w.right.color == 'black' and w.left.color == 'black':
                    w.color == 'red'
                    x = x.p
                else:
                    if w.left.color == 'black':
                        w.right.color = 'black'
                        w.color = 'red'
                        self.left_rotate(w)
                        w = x.p.left
                    w.color = x.p.color
                    x.p.color = 'black'
                    w.left.color = 'black'
                    self.right_rotate(x.p)
                    x = self.root
        x.color = 'black'
        
    def isEmpty(self):
        return self.root == self.nil
    
    def emptyTree(self):
        self.root = self.nil