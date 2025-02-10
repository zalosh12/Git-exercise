# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head) :
        if not head:
            return self.root
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        self.root = TreeNode(slow.val)
        prev = slow.next
        slow.next = None

        self.root.left = self.sortedListToBST(head)
        self.root.right = self.sortedListToBST(prev)





