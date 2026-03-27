from preloaded import Node

def swap_pairs(head):
    if head == None or head.next == None:
        return head
    A = head
    B = head.next
    C = head.next.next
    B.next = A
    A.next = swap_pairs(C)
    return B
