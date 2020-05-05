class Node:
	def __init__(self, data=None):
		self.data = data
		self.left = None
		self.right = None


class BST:
	def __init__(self):
		self.root = None

	def insert(self, value):
		if self.root is None:
			self.root = Node(value)
		else:
			self._insert(value, self.root)

	def _insert(self, value, cur_node):
		if value < cur_node.data:
			if cur_node.left == None:
				cur_node.left = Node(value)
			else:
				self._insert(value, cur_node.left)

		elif value > cur_node.data:
			if cur_node.right == None:
				cur_node.right = Node(value)
			else:
				self._insert(value, cur_node.right)
		else:
			return - 1  # Data already exits

	# Left, Root, Right
	def inOrder(self):
		cur_node = self.root
		self._inOrder(cur_node)

	def _inOrder(self, cur_node):
		if cur_node == None:
			return -1
		else:
			self._inOrder(cur_node.left)
			print(cur_node.data, end=" ")
			self._inOrder(cur_node.right)

	# Root, Left, Right
	def preOrder(self):
		cur_node = self.root
		self._preOrder(cur_node)

	def _preOrder(self, cur_node):
		if cur_node == None:
			return -1
		else:
			print(cur_node.data, end=" ")
			self._preOrder(cur_node.left)
			self._preOrder(cur_node.right)

	# Left, Right, Root
	def postOrder(self):
		cur_node = self.root
		self._postOrder(cur_node)

	def _postOrder(self, cur_node):
		if cur_node == None:
			return -1
		else:
			self._postOrder(cur_node.left)
			self._postOrder(cur_node.right)
			print(cur_node.data, end=" ")

	# Iterative Approach for In-Order Traversal
	def IterativeInOrder(self):
		stack = []
		cur_node = self.root
		while True:
			while cur_node:  # cur_node is not None
				stack.append(cur_node)
				cur_node = cur_node.left
			if len(stack) == 0:  # if it is empty that means we have explored all nodes of bst tree
				break
			cur_node = stack.pop()
			print(cur_node.data, end=" ")
			cur_node = cur_node.right

	# Iterative Appproach for Pre-Order Traversal
	def IterativePreOrder(self):
		stack = []
		cur_node = self.root
		while True:
			while cur_node:
				print(cur_node.data, end=" ")
				stack.append(cur_node)
				cur_node = cur_node.left
			if len(stack) == 0:
				break
			cur_node = stack.pop()
			cur_node = cur_node.right

	# Iterative Approach for Post-Order Travsersal
	# def IterativePostOrder(self):
	# 	cur_node = self.root
	# 	stack = []
	# 	while True:
	# 		if cur_node:
	# 			stack.append(cur_node)
	# 			cur_node = cur_node.left
	# 		else:
	# 			if len(stack) == 0:
	# 				break
	# 			else:
	# 				top = stack[-1]
	# 				if top.right == None:
	# 					cur_node = stack.pop()
	# 					print(cur_node.data, end=" ")
	# 					if cur_node == top.right:
	# 						print(top.data)
	# 						if cur_node == top.right:
	# 							print(top.data)
	# 							stack.pop()
	# 				if len(stack) > 0:
	# 					cur_node = stack[-1].right
	# 				else:
	# 					cur_node = None


bst = BST()
data = [10, 8, 20, 3, 9, 15, 25]
for val in data:
	bst.insert(val)

print("IN-ORDER")
bst.inOrder()
print()

print("Iterative In-Order")
bst.IterativeInOrder()
print()

print("PRE-ORDER")
bst.preOrder()
print()

print("Iterative Pre-Order")
bst.IterativePreOrder()
print()

print("POST-ORDER")
bst.postOrder()
print()
#
# print("Iterative Post-Order")
# bst.IterativePostOrder()
# print()
