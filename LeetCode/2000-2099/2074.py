'''
5926. Time Needed to Buy Tickets

2021.11.14 Sunday 14:14
'''
from LeetCode.tools.linkedlist import ListNode, linkedlist2list, list2linkedlist
from typing import Optional


class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        node = head
        while node:
            a.append(node.val)
            node = node.next

        i = 0
        n = len(a)
        d = 1
        while i < n:
            if min(d, n-i) % 2 == 0:
                a[i:i+d] = a[i:i+d][::-1]
            i += d
            d += 1

        node = head
        for x in a:
            node.val = x
            node = node.next
        return head


if __name__ == "__main__":
    obj = Solution()
    assert linkedlist2list(obj.reverseEvenLengthGroups(head=list2linkedlist([5,2,6,3,9,1,7,3,8,4]))) == [5,6,2,3,9,1,4,8,3,7]
    assert linkedlist2list(obj.reverseEvenLengthGroups(head=list2linkedlist([1,1,0,6]))) == [1,0,1,6]
    assert linkedlist2list(obj.reverseEvenLengthGroups(head=list2linkedlist([2,1]))) == [2,1]
    assert linkedlist2list(obj.reverseEvenLengthGroups(head=list2linkedlist([8]))) == [8]
