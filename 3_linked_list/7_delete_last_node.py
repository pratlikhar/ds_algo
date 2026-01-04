class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

def printList(head: Node):
    curr = head
    while curr != None:
        print(curr.key, end='\n')
        curr = curr.next

def deleteLast(head: Node):
    if head == None or head.next == None:
        return None
    
    curr = head

    while curr.next.next != None:
        curr = curr.next

    curr.next = None
    return head

head = Node(10)
head.next = Node(20)
head.next.next = Node(15)
head.next.next.next = Node(30)

head = deleteLast(head)
printList(head)
head = deleteLast(head)
printList(head)
head = deleteLast(head)
printList(head)
head = deleteLast(head)
printList(head)
head = deleteLast(head)
printList(head)
head = deleteLast(head)
printList(head)

printList(head)
