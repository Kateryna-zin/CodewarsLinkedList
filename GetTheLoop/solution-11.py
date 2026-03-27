def loop_size(node):
    loop = []
    mini_node = node
    while mini_node not in loop:
        loop.append(mini_node)
        mini_node = mini_node.next
    return len(loop) - loop.index(mini_node)
