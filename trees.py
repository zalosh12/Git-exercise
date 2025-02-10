from collections import deque
class BST:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


    def insert(self,data):
        if data == self.data:
            return # Binary tree can't have duplicate data
        if data < self.data:
            if self.left: # The node has a left subtree
                self.left.insert(data) # Recursively add data to the left subtree
            else:
                self.left = BST(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BST(data)








def sorted_arr_to_bst(elements):
    if not elements:
        return
    mid = len(elements) // 2
    root = BST(elements[mid])

    root.left = sorted_arr_to_bst(elements[:mid])
    root.right = sorted_arr_to_bst(elements[mid+1:])

    return root

if __name__ == "__main__":
    numbers = [6, 1, -1, -8, 5, 2, 28, 17, 12, 33]
    # The array must first be sorted
    numbers.sort()

    numbers_tree = sorted_arr_to_bst(numbers)
    def print_tree(root):
        queue = deque()
        print(root.data, end=" ")
        queue.append(root)

        while queue:
            root = queue.popleft()
            if root.left:
                print(root.left.data, end=" ")
                queue.append(root.left)

            if root.right:
                print(root.right.data, end=" ")
                queue.append(root.right)
    print_tree(numbers_tree)



