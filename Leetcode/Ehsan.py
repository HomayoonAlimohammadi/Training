class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):

        return f'''{self.value} 
    left: [{self.left}]
    right: [{self.right}]'''

    
class BST:

    def __init__(self, root_value):
        root = Node(root_value)
        self.root = root

    def addNode(self, value):

        new_node = Node(value)
        current_node = self.root

        while True:

            if new_node.value >= current_node.value:

                if current_node.right == None:
                    current_node.right = new_node
                    break

                current_node = current_node.right

            elif new_node.value < current_node.value:

                if current_node.left == None:
                    current_node.left = new_node
                    break

                current_node = current_node.left

    def calculateLeafValues(self):

        total = 0
        queue = []

        queue.append(self.root)

        while len(queue) != 0:
            
            node = queue[0]
            is_leaf = True

            if node.right != None:
                queue.append(node.right)
                is_leaf = False

            if node.left != None:
                queue.append(node.left)
                is_leaf = False

            if is_leaf:
                total += node.value

            queue = queue[1:]    

        return total


bst = BST(0)
nums = [-1]
for value in nums:
    bst.addNode(value)
    print(bst.calculateLeafValues() % (10**9 + 7))

print(bst.root)