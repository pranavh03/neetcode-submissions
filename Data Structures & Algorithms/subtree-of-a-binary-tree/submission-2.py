# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def has_tree(p,q):
            if not p and not q:
                return True
            if (not q) or (not p) or  p.val!=q.val:
                return False
            return has_tree(p.left,q.left) and has_tree(p.right,q.right)
        def has_subtree(root):
            if root is None:
                return False
            if has_tree(root,subRoot):
                return True  
            return has_subtree(root.left) or has_subtree(root.right)
        return has_subtree(root)    


        