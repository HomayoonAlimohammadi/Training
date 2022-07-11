from __future__ import annotations


class TreeNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self._left: TreeNode = None
        self._right: TreeNode = None
        self._parent: TreeNode = None
        self._is_locked = False

    @property
    def parent(self):
        return self._parent

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node: TreeNode):
        node._parent = self
        self._left = node

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node: TreeNode):
        node._parent = self
        self._right = node

    @property
    def is_locked(self) -> bool:
        return self._is_locked

    def get_ancestors(self) -> list[TreeNode]:
        ancestors = []
        current = self
        while current.parent:
            current = current.parent
            ancestors.append(current)
        return ancestors

    def get_decendants(self) -> list[TreeNode]:
        nodes = [self]
        decendants = []
        while nodes:
            node = nodes.pop()
            decendants.append(node)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)

        return decendants[1:]

    def toggle_lock(self) -> bool:
        ancestors = self.get_ancestors()
        decendants = self.get_decendants()

        decendants_locked, ancestors_locked = False, False
        for ancestor in ancestors:
            if ancestor.is_locked:
                ancestors_locked = True

        for decendant in decendants:
            if decendant.is_locked:
                decendants_locked = True

        if not decendants_locked or not ancestors_locked:
            self._is_locked = not self._is_locked
            return True

        return False

    def __repr__(self) -> str:
        lock_status = "x" if self.is_locked else "o"
        return f"({self.val}, {lock_status})"

    def __str__(self) -> str:
        return f"Node(val: {self.val}, is_locked: {self.is_locked}\n\tleft: {self.left}\n\tright: {self.right})"


class Tree:
    def __init__(self, root: TreeNode) -> None:
        self.root = root

    def get_ancestors(self, node: TreeNode) -> list[TreeNode]:
        def search(current: TreeNode, target: TreeNode, node_path: list[TreeNode]):
            if current is None:
                return False, []

            if current is target:
                return True, node_path

            node_path.append(current.left)
            is_left, left_path = search(current.left, target, node_path.copy())

            node_path.pop()
            node_path.append(current.right)
            is_right, right_path = search(current.right, target, node_path.copy())
            node_path.pop()

            if is_left:
                return True, left_path
            elif is_right:
                return True, right_path

            return False, []

        _, ancestors = search(self.root, node, [self.root])
        return ancestors

    def get_decendants(self, node: TreeNode) -> list[TreeNode]:
        nodes = [node]
        decendants = []
        while nodes:
            node = nodes.pop()
            decendants.append(node)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)

        return decendants[1:]

    @property
    def is_locked(self, node: TreeNode) -> bool:
        return node.is_locked


root = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_4 = TreeNode(4)
node_5 = TreeNode(5)
node_6 = TreeNode(6)
node_7 = TreeNode(7)

root.left = node_2
root.right = node_3
node_2.left = node_4
node_2.right = node_5
node_5.left = node_6
node_5.right = node_7

# tree = Tree(root)
# print(tree.get_ancestors(node_4))
# print(tree.get_decendants(node_2))

print(node_2.toggle_lock())
print(root.get_decendants())
print(node_5.toggle_lock())
print(root.get_decendants())
print(node_6.toggle_lock())
print(root.get_decendants())
print(node_5.toggle_lock())
print(root.get_decendants())
