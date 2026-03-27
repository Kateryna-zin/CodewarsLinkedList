class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    if not isinstance(node, Node):
        raise ValueError
    while index:
        if node.next is None:
            raise IndexError
        node = node.next
        index = index - 1
    return node
