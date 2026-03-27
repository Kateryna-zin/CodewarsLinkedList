class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    node = Node(data)
    node.next = head
    return node

def build_one_two_three():
    resolt = None
    resolt = push(resolt, 3)
    resolt = push(resolt, 2)
    resolt = push(resolt, 1)
    return resolt
