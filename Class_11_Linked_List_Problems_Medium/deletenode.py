# A complete working Python3 program to
# demonstrate deletion in singly
# linked list with class

# Node class
class Node:

	# Constructor to initialize the node object
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	# Function to insert a new node at the beginning
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

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


	# Utility function to print the linked LinkedList
	def printList(self):
		temp = self.head
		while(temp):
			print (" %d" %(temp.data)),
			temp = temp.next


# Driver program
llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)

print ("Created Linked List: ")
llist.printList()
llist.deleteNode(1)
print ("\nLinked List after Deletion of 1:")
llist.printList()

# This code is contributed by Nikhil Kumar Singh (nickzuck_007)
