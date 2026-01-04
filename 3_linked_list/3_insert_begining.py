class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

def printList(head: Node):
    curr = head
    while curr != None:
        print(curr.key, end='\n')
        curr = curr.next

def insertBegin(head: Node, key):
    temp = Node(key)
    temp.next = head
    head = temp
    return head

head = Node(10)
head.next = Node(20)
head.next.next = Node(15)
head.next.next.next = Node(30)

head = insertBegin(head, 10)
head = insertBegin(head, 20)
head = insertBegin(head, 30)
printList(head)
