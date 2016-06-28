from avl import AVL 

l = []

tree = AVL()
tree.insert(100)
tree.insert(90)
tree.insert(80)
tree.insert(6)
tree.delete(100)
tree.inorder(l, tree.root)
print(l)