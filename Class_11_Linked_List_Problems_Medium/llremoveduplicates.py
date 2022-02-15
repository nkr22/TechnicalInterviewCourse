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
    
    	def deleteNode(self, key):
		
		# Store head node
		temp = self.head


		if (temp is not None):
			if (temp.data == key):
				self.head = temp.next
				temp = None
				return

		while(temp is not None):
			if temp.data == key:
				break
			prev = temp
			temp = temp.next

		if(temp == None):
			return

		# Unlink the node from linked list
		prev.next = temp.next

		temp = None

	def reverse(self):
		previous=None
		current=self.head
		while(current is not None):
			next=current.next
			current.next=previous
			previous=current
			current=next
		self.head=previous

        def remdup(self):
            current=self.head
            while (current is not None):
                if current==current.next:
                    self.deleteNode(current.next.data)
                else:
                    current.next=current




LL= LinkedList()
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.printLL()
LL.reverse()
LL.printLL()
LL.remdup()