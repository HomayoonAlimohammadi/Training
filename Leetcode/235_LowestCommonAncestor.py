class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return f'TreeNode{{val: {self.val}, left: {self.left}, right: {self.right}}}'

    def __repr__(self):
        return f'TreeNode{{val: {self.val}}}'


class Solution:

    def lowestCommonAncestor(self, root: TreeNode, 
                            p: TreeNode, q: TreeNode) -> TreeNode:
        
        ancestors = {root.val}
        nodes_data = [(ancestors, root)]
        while nodes_data:
            ancestors, node = nodes_data[0]
            nodes_data.pop(0)

            if node.val == p.val:
                p_data = ((ancestors | {p.val}, node))
            if node.val == q.val:
                q_data = ((ancestors | {q.val}, node))

            if node.left:
                left_node_data = (ancestors | {node.val}, node.left)
                nodes_data.append(left_node_data)
            if node.right:
                right_node_data = (ancestors | {node.val}, node.right)
                nodes_data.append(right_node_data)

        # p_data = nodes_data

        # ancestors = {root.val}
        # nodes_data = [(ancestors, root)]
        # while nodes_data:
        #     ancestors, node = nodes_data[0]
        #     nodes_data.pop(0)
        #     if node.val == q.val:
        #         nodes_data = ((ancestors | {q.val}, node))
        #         break
        #     if node.left:
        #         left_node_data = (ancestors | {node.val}, node.left)
        #         nodes_data.append(left_node_data)
        #     if node.right:
        #         right_node_data = (ancestors | {node.val}, node.right)
        #         nodes_data.append(right_node_data)

        # q_data = nodes_data

        common_ancestors = list(p_data[0] & q_data[0])
        print(f'{p_data=}')
        print(f'{q_data=}')
        print(f'{common_ancestors=}')
        # return common_ancestors
        lca_value = min(common_ancestors)
        nodes = [root]
        while nodes:
            node = nodes[0]
            nodes.pop(0)
            if node.val == lca_value:
                return node

            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)

        return None


class Solution2:
    res = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q: return None
        
        def search(root, p, q):
            if not root: return False
            mid = left = right = False
            if root.val == p.val or root.val == q.val: 
                mid = True
            
            left = search(root.left, p, q)
            right = search(root.right, p, q)
            if mid:
                if left or right:
                    self.res = root
            elif left and right:
                self.res = root
            return mid or left or right
            
        search(root, p, q)
        return self.res



def build_tree(values):

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


values = [6,2,8,0,4,7,9,3,5]
p = TreeNode(2)
q = TreeNode(4)
root = build_tree(values)
print(Solution().lowestCommonAncestor(root, p, q))