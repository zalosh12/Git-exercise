import binary
from binary import TreeNode
from collections import deque


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        new_node = TreeNode(value)
        if self.root is None:
            self.root = new_node
            return
        queue = deque([self.root])
        while queue:
            current = queue.popleft()
            if current.left is None:
                current.left = new_node
                return
            queue.append(current.left)
            if current.right is None:
                current.right = new_node
                return
            queue.append(current.right)

    def print_tree(self):
        if self.root is None:
            return

        queue = deque()
        print(self.root.val,end=" ")
        queue.append(self.root)

        while queue:
            root = queue.popleft()
            if root.left:
                print(root.left.val,end=" ")
                queue.append(root.left)

            if root.right:
                print(root.right.val,end=" ")
                queue.append(root.right)





m = BinaryTree()
m.insert(7)
m.insert(9)
m.insert(3)
m.insert(2)
m.insert(1)
m.insert(4)
m.insert(1)
m.print_tree()




