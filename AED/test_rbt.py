from rbt import RBT

l=[]
tree = RBT()
tree.rb_insert(5)
tree.rb_insert(4)
tree.rb_insert(8)
tree.rb_insert(6)
print(tree.inorder(l))