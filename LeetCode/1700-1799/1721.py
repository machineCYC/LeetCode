'''
1721. Swapping Nodes in a Linked List

2021.01.10 Sunday 16:07
'''
from LeetCode.tools.linkedlist import linkedlist2list, list2linkedlist, ListNode


class Solution:

    def swapNodes(self, head: ListNode, k: int) -> ListNode:

        vals = []
        node = head
        while node:
            vals.append(node.val)
            node = node.next

        vals[k-1], vals[-k] = vals[-k], vals[k-1]
        dummy = ListNode(vals[0])
        node = dummy
        for i, v in enumerate(vals):
            if i == 0:
                continue
            node.next = ListNode(v)
            node = node.next
        return dummy

if __name__ == "__main__":
    obj = Solution()
    assert linkedlist2list(obj.swapNodes(head = list2linkedlist([1,2,3,4,5]), k = 2))==[1,4,3,2,5]
    assert linkedlist2list(obj.swapNodes(head = list2linkedlist([7,9,6,6,7,8,3,0,9,5]), k = 5))==[7,9,6,6,8,7,3,0,9,5]
    assert linkedlist2list(obj.swapNodes(head = list2linkedlist([1]), k = 1))==[1]
    assert linkedlist2list(obj.swapNodes(head = list2linkedlist([1, 2]), k = 1))==[2, 1]
    assert linkedlist2list(obj.swapNodes(head = list2linkedlist([1,2,3]), k = 2))==[1,2,3]