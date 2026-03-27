class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if head is None:
        raise ValueError
    if head.next is None:
        return Context(head, None)
    first = head
    second = head.next
    rest = head.next.next
    if rest:
        sub_context = alternating_split(rest)
        first.next = sub_context.first
        second.next = sub_context.second
    else:
        first.next = None
        second.next = None
    return Context(first, second)
