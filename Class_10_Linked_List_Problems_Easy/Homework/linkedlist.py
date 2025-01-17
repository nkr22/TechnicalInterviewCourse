# A simple Python program to introduce a linked list

class Node:

	def __init__(self, data):
		self.data = data 
		self.next = None 


class LinkedList:

	def __init__(self):
		self.head = None


if __name__=='__main__':

	llist = LinkedList()

	llist.head = Node(1)
	second = Node(2)
	third = Node(3)

	llist.head.next = second; 

	second.next = third; 


###### what she did in class
class Node:

	def __init__(self, data):
		self.data = data 
		self.next = None 
		
class LinkedList:

	def __init__(self):
		self.head = None

	def insert(self, data):
		newNode=Node(data)
		if(self.head):
			current=self.head
			while(current.next):
				current=current.next
			current.next=newNode
		else:
			self.head=newNode

	def printLL(self):
		current=self.head
		while(current):
			print(current.data)
			current=current.next

LL= LinkedList()
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.printLL()