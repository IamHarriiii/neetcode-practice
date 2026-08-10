# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeInfo:
    def __init__(self, height, diameter):
        self.height = height
        self.diameter = diameter


class Solution:

    def helper(self, root):

        if root is None:
            return TreeInfo(0, 0)

        left = self.helper(root.left)
        right = self.helper(root.right)

        my_height = max(left.height, right.height) + 1

        diam1 = left.height + right.height
        diam2 = left.diameter
        diam3 = right.diameter

        my_diameter = max(diam1, diam2, diam3)

        return TreeInfo(my_height, my_diameter)

    def diameterOfBinaryTree(self, root):
        return self.helper(root).diameter