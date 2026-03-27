from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    linked_list = None
    lst = [el.strip() for el in list_repr.split('->')][:-1][::-1]
    for el in lst:
        linked_list = Node(int(el), linked_list)
    return linked_list
