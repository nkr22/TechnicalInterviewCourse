class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
    
    def remove(self, data):
        if data == self.head.data:
            self.head = self.head.next
        else:
            current = self.head.next
            prev = self.head
            while(current):
                if current.data == data:
                    prev.next = current.next 
                    break
                prev = current
                current = current.next

    def removeDups(self):
        current = self.head.next
        prev = self.head
        while(current):
            if current.data == prev.data:
                prev.next = current.next
                current = current.next
            else:
                prev = current
                current = current.next

    # def removeDupsunorder(self):
    #     ### use a hash table
    #     ### brute force nested for loops
    #     ### merge sort and then do it
    #     hash={}
    #     current=self.head
    #     previous=None

    #     if(hash[current.data]) 

    ##write a program to delete N nodes after M nodes of a linked list
    def deleteNM(self, M, N):
        current=self.head
        while (current):
            for i in range(1, M):
                if current is None:
                    return
                current=current.next
            if current is None:
                return
            
            temp=current.next

            for j in range(0, N):
                




                    

    
def printHead(head):
    current = head
    while(current):
        print(current.data)
        current = current.next
    
def reverse(node):
    if (node == None):
        return node
    if (node.next == None):
        return node
    
    tempnode = reverse(node.next)
    node.next.next = node
    node.next = None
    return tempnode


LL = LinkedList()
LL.insert(3)
LL.insert(3)
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.insert(5)
LL.insert(6)
printHead(LL.head)
print()
LL.removeDups()
printHead(LL.head)
print()
head = reverse(LL.head)
printHead(head)