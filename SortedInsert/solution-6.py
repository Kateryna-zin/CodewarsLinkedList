class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    if head is None or data < head.data:
        new_node = Node(data)
        new_node.next = head
        return new_node
    front_list = []
    current = head
    while current is not None and current.data < data:
        front_list.append(current.data)
        current = current.next
    new_node = Node(data)
    new_node.next = current
    for el in reversed(front_list):
        node = Node(el)
        node.next = new_node
        new_node = node
    return new_node
