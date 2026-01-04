class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

def printList(head: Node):
    curr = head
    while curr != None:
        print(curr.key, end='\n')
        curr = curr.next

def deleteFirst(head: Node):
    if head == None or head.next == None:
        return None
    
    head = head.next

    return head

def conciseDeleteFirst(head: Node):
    if head == None:
        return None
    else:
        return head.next

head = Node(10)
head.next = Node(20)
head.next.next = Node(15)
head.next.next.next = Node(30)

head = deleteFirst(head)
printList(head)
head = deleteFirst(head)
printList(head)
head = deleteFirst(head)
printList(head)
head = deleteFirst(head)
printList(head)
head = deleteFirst(head)
printList(head)
head = deleteFirst(head)
printList(head)

printList(head)
