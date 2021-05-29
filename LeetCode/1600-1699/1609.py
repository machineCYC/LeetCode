'''
1609. Even Odd Tree

2020.10.04 Sunday 17:05
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        queue = [root]
        level = 0
        while queue:
            newq = []
            prev = -float("inf") if level % 2 == 0 else float("inf")
            for node in queue:

                if level % 2 == 0 and (node.val % 2 == 0 or prev >= node.val): return False
                if level % 2 == 1 and (node.val % 2 == 1 or prev <= node.val): return False
                prev = node.val
                if node.left: newq.append(node.left)
                if node.right: newq.append(node.right)

            queue = newq
            level += 1
        return True


if __name__ == "__main__":
    from LeetCode.tools.tree import tree2string, string2tree

    obj = Solution()

    root = string2tree("[1,10,4,3,null,7,9,12,8,6,null,null,2]")
    assert obj.isEvenOddTree(root) == True
    root = string2tree("[5,4,2,3,3,7]")
    assert obj.isEvenOddTree(root) == False
    root = string2tree("[5,9,1,3,5,7]")
    assert obj.isEvenOddTree(root) == False
    root = string2tree("[1]")
    assert obj.isEvenOddTree(root) == True
    root = string2tree("[11,8,6,1,3,9,11,30,20,18,16,12,10,4,2,17]")
    assert obj.isEvenOddTree(root) == True
