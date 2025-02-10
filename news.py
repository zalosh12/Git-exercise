from collections import  deque
class TreeNode:
    def __init__(self,data):
        self.val = data
        self.right = None
        self.left = None

class BST:
    def __init__(self):
        self.root = None

    def add(self,val):
        new_node = TreeNode(val)
        if self.root is None:
            self.root = new_node

        current = self.root
        while True:
            if current.val == val:
                print("value already exist")
                return
            if current.val > val:
                if current.left:
                    current = current.left
                else:
                    current.left = new_node
                    return
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = new_node
                    return

    def delet(self,val):
        def search()


    def insert(self,val):
        new_node = TreeNode(val)
        if not self.root:
            self.root = new_node
            return

        def ins(root = self.root):
           if root is None:
                return new_node
           if val < root.val:
               root.left = ins(root.left)
           else:
               root.right = ins(root.right)
           return root
        ins()

    def inorder(self):
        def inord(root = self.root):
           if root is None:
               return
           inord(root.left)
           print(root.val)
           inord(root.right)
        inord()



    def print_tree(self):
        if self.root is None:
            return

        queue = deque()
        print(self.root.val, end=" ")
        queue.append(self.root)

        while queue:
            root = queue.popleft()
            if root.left:
                print(root.left.val, end=" ")
                queue.append(root.left)

            if root.right:
                print(root.right.val, end=" ")
                queue.append(root.right)


m = BST()
m.insert(4)
m.insert(8)
m.insert(3)
m.insert(5)
m.insert(33)
m.print_tree()
# m.inorder()
#
# f = BST()
# f.add(4)
# f.add(8)
# f.add(3)
# f.add(5)
# f.add(33)
# f.add(6)
# f.print_tree()
#
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

inorder(m.root)

def inorder_s(root):
    current = root
    while current.left:
        current = current.left
    return current

def delete_node(root,val):
    if root.val < val:
        root.right = delete_node(root.right,val)
    elif root.val > val:
        root.left = delete_node(root.left,val)
    else:
        if root.left is None and root.right is None:
            return
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        IS = inorder_s(root.right)
        root.val = IS.val
        root.right = delete_node(root.right,IS.val)
    return root
l = deque([9])

