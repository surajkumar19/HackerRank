"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(first_node):
    if first_node is None:
        return False
    x = first_node
    if first_node.next is None:
        return False
    y = first_node.next.next

    while y.next.next is not None and x.next is not None:
        x = x.next
        y = y.next.next
        if x == y:
            return True


    return False
    pass