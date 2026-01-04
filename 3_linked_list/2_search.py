class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

def search(head: Node, x):
    pos = 1
    curr = head

    while curr != None:
        if x == curr.key:
            print(pos)

        pos += 1
        curr = curr.next

    return -1

head = Node(10)
head.next = Node(20)
head.next.next = Node(15)
head.next.next.next = Node(30)
head.next.next.next.next = Node(15)

search(head, 15)