class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    head_list = []
    while head:
        head_list.append(head.data)
        head = head.next
    head = None
    for el in head_list:
        node = Node(el)
        node.next = head
        head = node
    return head
