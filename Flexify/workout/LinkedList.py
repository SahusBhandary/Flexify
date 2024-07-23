class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        newNode = Node(data)
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = newNode