class DoublyLinkedListNode:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.next = next
        self.prev = prev

def sortedInsert(head, data):
    new_node = DoublyLinkedListNode()
    new_node.data = data
    if head is None:
        head = new_node
    elif head.data >= data:
        new_node.next = head
        new_node.prev = head.prev
        head.prev = new_node
        head = new_node
    else:
        current = head
        while current.next is not None and current.next.data < data and current.next != head:
            current = current.next

        new_node.next = current.next
        if current.next is not None:
            new_node.next.prev = new_node
        current.next = new_node

        new_node.prev = current
    return head

head = None
A = [3, 1, 2, 3, 4, 10, 20, 15, 12, 11, 13]
for num in A:
    head = sortedInsert(head, num)
current = head
print(current.data)
current = current.next
while current != head and current is not None:
    print(current.data)
    current = current.next