from typing import Optional


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return f'TreeNode{{val: {self.val}, left: {self.left}, right: {self.right}}}'


class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''Determine wheter a Tree structure is balanced or not.'''

        leafs = [root]
        while leafs:
            node = leafs[0]
            if node.left:
                leafs.append(node.left)
            if node.right:
                leafs.append(node.right)
            leafs.pop(0)

        return leafs


def create_tree(values):

    if values:
        val = values[0]
        values.pop(0)
    root = TreeNode(val)
    for val in values:
        curr = root
        while True:
            if val < curr.val:
                if curr.left is None:
                    node = TreeNode(val)
                    curr.left = node
                    break
                curr = curr.left
            else:
                if curr.right is None:
                    node = TreeNode(val)
                    curr.right = node
                    break
                curr = curr.right
    return root


values = [1,2,3,4]
root = create_tree(values)
print(root)
                
                