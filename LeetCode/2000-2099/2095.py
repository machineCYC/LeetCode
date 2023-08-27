'''
2095. Delete the Middle Node of a Linked List

2021.12.05 Sunday 14:30
'''
from LeetCode.tools.linkedlist import ListNode, linkedlist2list, list2linkedlist
from typing import Optional


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head.next == None:
            return None

        pre_node = ListNode(None)
        cur_node = head
        fut_node = head

        while fut_node and fut_node.next:
            pre_node = cur_node
            cur_node = cur_node.next
            fut_node = fut_node.next.next
        pre_node.next = cur_node.next
        return head

if __name__ == "__main__":
    obj = Solution()
    assert linkedlist2list(obj.deleteMiddle(head=list2linkedlist([1,3,4,7,1,2,6]))) == [1,3,4,1,2,6]
    assert linkedlist2list(obj.deleteMiddle(head=list2linkedlist([1,2,3,4]))) == [1,2,4]
    assert linkedlist2list(obj.deleteMiddle(head=list2linkedlist([2,1]))) == [2]
    assert linkedlist2list(obj.deleteMiddle(head=list2linkedlist([1, 2, 3]))) == [1, 3]
    assert linkedlist2list(obj.deleteMiddle(head=list2linkedlist([1]))) == []
