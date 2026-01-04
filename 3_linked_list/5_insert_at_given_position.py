class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

def printList(head: Node):
    curr = head
    while curr != None:
        print(curr.key, end='\n')
        curr = curr.next

def insertPos(head: Node, key, pos):
    temp = Node(key)
    if pos == 1:
        temp.next = head
        return temp
    
    curr = head

    for i in range(pos-2): # if we want to insert at 4th pos, we need to run the loop 2 times to reach the 3rd pos
        curr = curr.next
        if curr == None: # if reached at the end of ll, the pos provided is out of bound, don't modify the ll
            return head
        
    temp.next = curr.next
    curr.next = temp

    return head

head = Node(10)
head.next = Node(20)
head.next.next = Node(15)
head.next.next.next = Node(30)

head = insertPos(head, 40, 3)
printList(head)
