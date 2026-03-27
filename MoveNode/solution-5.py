class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    data = source.data
    source = source.next
    dest1 = Node(data)
    dest1.next = dest
    return Context(source, dest1)
