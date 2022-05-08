'''
2265. Count Nodes Equal to Average of Subtree

2022.05.08 Sunday 16:35
'''
from typing import Optional
from LeetCode.tools import tree
from LeetCode.tools.tree import TreeNode


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.count = 0

        def dfs(root):
            if root is None:
                return [0, 0]

            value = root.val
            left_val, left_cnt = dfs(root.left)
            right_val, right_cnt = dfs(root.right)

            value += left_val + right_val
            cnt = left_cnt + right_cnt + 1
            if (value // cnt) == root.val:
                self.count += 1
            return [value, cnt]

        dfs(root)
        return self.count

if __name__ == "__main__":
    obj = Solution()
    assert obj.averageOfSubtree(tree.string2tree("[4,8,5,0,1,null,6]")) == 5
    assert obj.averageOfSubtree(tree.string2tree("[1]")) == 1