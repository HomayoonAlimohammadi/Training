from typing import Optional
from random import sample


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return f'TreeNode{{val: {self.val}, left: {self.left}, right: {self.right}}}'

    def __repr__(self):
        return f'{self.val}'


class Solution:

    def isBalanced_search(self, root: Optional[TreeNode]) -> bool:
        '''Determine wheter a Tree structure is balanced or not.'''

        nodes = [(1, root)]
        leafs = []
        all_depth = []
        while nodes:
            node = nodes[0][1]
            depth = nodes[0][0]
            has_left, has_right = False, False
            if node.left:
                nodes.append((depth+1, node.left))
                has_left = True
            if node.right:
                nodes.append((depth+1, node.right))
                has_right = True
            print(node.val, has_left, has_right)
            if not has_left or not has_right:
                if hasattr(node, 'val'):
                    leafs.append(node.val)
                    all_depth.append(depth)
                else:
                    leafs.append(None)
                
                if all_depth and all_depth[-1] - all_depth[0] > 1:
                    print(all_depth)
                    print(leafs)
                    return False
            nodes.pop(0)

        print(all_depth)
        return True 

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''Determine wheter a Tree structure is balanced or not.'''

        if root is None:
            return True

        def process(node):
            
            left, right = {
                'ans': True,
                'depth': 0
            }, {
                'ans': True,
                'depth': 0
            }
            if node.left:
                left = process(node.left)
            if node.right:
                right = process(node.right)

            print(node.val)
            print('left:', left)
            print('right:', right)
            print()
            
            if (not left['ans'] or not right['ans']) or \
                (abs(left['depth'] - right['depth']) > 1):
                return {
                    'ans': False,
                    'depth': None
                }
            
            depth = max(left['depth'], right['depth'])
            return {
                'ans': True,
                'depth': depth + 1
            }

        result = process(root)
        return result['ans']


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

def create_arbitrary_tree(values):

    root = TreeNode(values[0])
    nodes = [root]
    values.pop(0)
    while nodes:
        
        node = nodes[0]
        nodes.pop(0)

        if not values:
            break

        left_val = values[0]
        values.pop(0)
        if left_val:
            left_node = TreeNode(left_val)
            nodes.append(left_node)
            node.left = left_node

        if not values:
            break

        right_val = values[0]
        values.pop(0)
        if right_val:
            right_node = TreeNode(right_val)
            nodes.append(right_node)
            node.right = right_node

    return root


values = [3]
# values = sample(range(1, 200), 100)
root = create_arbitrary_tree(values)
print(root)
print(Solution().isBalanced(root))
                
                