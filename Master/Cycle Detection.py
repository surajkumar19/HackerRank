"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    a=head
    b=head
    while((a.next!=None) and (b.next.next!=None)):
        a=a.next
        b=b.next
        if(a==b):
            return True
    return False