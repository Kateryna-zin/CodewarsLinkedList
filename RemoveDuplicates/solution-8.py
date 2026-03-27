class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    lst = []
    while head:
        if head.next == None or head.data != head.next.data:
            lst.append(head.data)
        head = head.next
    for el in reversed(lst):
        node = Node(el)
        node.next = head
        head = node
    return head
