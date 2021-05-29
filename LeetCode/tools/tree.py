# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def string2tree(strList):
    strList = strList.strip()
    strList = strList.replace("[", "").replace("]", "")
    strList = strList.split(",")

    tree = TreeNode(int(strList[0]))
    value_index = 0
    node_index = 0
    is_left_right = True
    queue = [tree]
    while value_index < len(strList):
        node = queue[node_index]
        node_index += 1

        value_index += 1
        if value_index < len(strList):
            left_value = strList[value_index]
            if left_value != "null":
                node.left  = TreeNode(int(left_value))
                queue.append(node.left)
            else:
                node.left = None # TreeNode(None)

        value_index += 1
        if value_index < len(strList):
            right_value = strList[value_index]
            if right_value != "null":
                node.right  = TreeNode(int(right_value))
                queue.append(node.right)
            else:
                node.right = None # TreeNode(None)

    return tree

# FIXME: will return more null in the last
def tree2string(root):
    stringList = []

    node_index = 0
    queue = [root]
    while node_index < len(queue):
        node = queue[node_index]
        node_index += 1

        if node is None:
            stringList.append("null")
        else:
            value = node.val
            stringList.append(value)

            if node.left is not None:
                queue.append(node.left)
            else:
                queue.append(None)

            if node.right is not None:
                queue.append(node.right)
            else:
                queue.append(None)

    return str(stringList)

if __name__ == "__main__":
    tree = string2tree("[1,10,4,3,null,7,9,12,8,6,null,null,2]")
    stringList = tree2string(tree)
