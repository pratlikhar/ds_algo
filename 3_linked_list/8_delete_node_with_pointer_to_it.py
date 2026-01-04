class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

def printList(head: Node):
    curr = head
    while curr != None:
        print(curr.key, end='\n')
        curr = curr.next

def deletePointer(ptr: Node):
    temp = ptr.next
    ptr.key = temp.key
    ptr.next = temp.next

head = Node(10)
head.next = Node(20)
head.next.next = Node(15)
head.next.next.next = Node(30)

deletePointer(head.next.next)
printList(head)
