class Node:
     def __init__(self, data):
          self.data = data
          self.left = None
          self.right = None

def init_tree():
     global root
     new_node = Node("A")
     root = new_node

     new_node = Node("B")
     root.left = new_node

     new_node = Node("C")
     root.right = new_node

     new_node1 = Node("D")
     new_node2 = Node("E")
     node = root.left
     node.left = new_node1
     node.right = new_node2

     
     new_node1 = Node("F")
     new_node2 = Node("G")
     node = root.right
     node.left = new_node1
     node.right = new_node2

def preorder(node):
     if node == None: return
     print(node.data, end = '')
     preorder(node.left)
     preorder(node.right)

def inorder(node):
     if node == None: return
     inorder(node.left)
     print(node.data, end = '')
     inorder(node.right)

def postorder(node):
     if node == None: return
     postorder(node.left)
     postorder(node.right)
     print(node.data, end = '')

init_tree()
preorder(root)
print("\n")
inorder(root)
print("\n")
postorder(root)
