class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return f'TreeNode{{val: {self.val}, left: {self.left}, right: {self.right}}}'


class Solution:

    def lowestCommonAncestor(self, root: TreeNode, 
                            p: TreeNode, q: TreeNode) -> TreeNode:
        
        pass


def build_tree(values):

    root = TreeNode(values[0])
    for val in values[1:]:
        curr = root
        while curr:
            if val <= curr.val:
                if curr.left:
                    curr = curr.left
            else:
                curr = curr.right

        curr = TreeNode(val)

    return root


values = [6,2,8,0,4,7,9,3,5]
root = build_tree(values)
print(root)