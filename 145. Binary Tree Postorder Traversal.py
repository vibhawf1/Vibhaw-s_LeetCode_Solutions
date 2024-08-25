# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def traverse(node):
            if node:
                # Visit left subtree
                traverse(node.left)
                # Visit right subtree
                traverse(node.right)
                # Visit node itself
                result.append(node.val)
        
        traverse(root)
        return result
        
