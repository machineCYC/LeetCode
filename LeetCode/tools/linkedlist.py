# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def linkedlist2list(linkedlist):
    vals = []
    node = linkedlist
    while node:
        vals.append(node.val)
        node = node.next
    return vals


def list2linkedlist(array):
    dummy = ListNode()
    node = dummy
    for v in array:
        node.next = ListNode(v)
        node = node.next
    return dummy.next
