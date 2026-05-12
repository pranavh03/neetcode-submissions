# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack=[[p,q]]
        while stack:
            Node1,Node2 =stack.pop()
            if not Node1 and not Node2:
                continue
            if not Node1 or not Node2 or Node1.val!=Node2.val:
                return False
            stack.append([Node1.left,Node2.left])
            stack.append([Node1.right,Node2.right])
        return True

        