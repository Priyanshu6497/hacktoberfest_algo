class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Sample binary tree
#        1
#       / \
#      2   3
#     / \
#    4   5

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.value, end=' ')
        in_order_traversal(node.right)

print("In-order traversal:")
in_order_traversal(root)  # Output: 4 2 5 1 3

def pre_order_traversal(node):
    if node:
        print(node.value, end=' ')
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

print("\nPre-order traversal:")
pre_order_traversal(root)  # Output: 1 2 4 5 3

def post_order_traversal(node):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.value, end=' ')

print("\nPost-order traversal:")
post_order_traversal(root)  # Output: 4 5 2 3 1
