
# Level order traversal of tree
from collections import deque

class Node:

	def __init__(self,key):
		self.data = key
		self.left = None
		self.right = None

def lot(root):

	if root is None:
		return

	d = deque()

	d.append(root)

	while(len(d)>0):

		l = len(d)

		while(l>0):
			temp = d.pop()
			print(temp.data,end=" ")
     	 	
			if(temp.left is not None):
				d.appendleft(temp.left)
			if(temp.right is not None):
				d.appendleft(temp.right)
			l = l-1;

		print()		


root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
  
print("Level Order Traversal of binary tree is -")
lot(root) 