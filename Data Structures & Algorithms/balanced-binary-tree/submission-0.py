# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeInfo:
    def __init__(self, height, balanced):
        self.height = height
        self.balanced = balanced
class Solution:

    def helper(self, root):
        if root is None:
            return TreeInfo(0, True)
        
        left_child = self.helper(root.left)
        right_child = self.helper(root.right)

        my_height = max(left_child.height, right_child.height) + 1
        my_balanced = (left_child.balanced and right_child.balanced and abs(left_child.height - right_child.height) <= 1)

        return TreeInfo(my_height, my_balanced)


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root).balanced