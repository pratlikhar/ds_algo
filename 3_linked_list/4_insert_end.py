class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

def printList(head: Node):
    curr = head
    while curr != None:
        print(curr.key, end='\n')
        curr = curr.next

def insertEnd(head: Node, key):

    if head == None:
        return Node(key)

    curr = head

    while curr.next != None:
        curr = curr.next

    curr.next = Node(key)
    return head

head = Node(10)
head.next = Node(20)
head.next.next = Node(15)
head.next.next.next = Node(30)

head = insertEnd(head, 10)
head = insertEnd(head, 20)
head = insertEnd(head, 30)
printList(head)
