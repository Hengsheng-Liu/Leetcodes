"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.
"""
def preorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]

    Time:10mins 14sec
    Solve: yes
    Difficulty: Easy 
    Comments
    I believe that any way of traversal(pre,in,post) all have to use stack because is all DFS, 
    you have to all the way down in to the left tree then to the right tree. This problem is not hard but 
    I forgot to check empty tree in which keep give me None type error. 
    """
    if root is None:
        return [] 
    stack = []
    stack.append(root)
    preorder = []
    while(stack):
        node = stack.pop()
        preorder.append(node.val)
        if node.right is not None: 
            stack.append(node.right)
        if node.left is not None: 
            stack.append(node.left)  
    return preorder
    """
    Comments: 
        Didn't realize that recursion is one liner 
    def preorderTraversal(self, root):
        :type root: TreeNode
        :rtype: List[int]

        if(root == None):
            return []
        else:
            return [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right)    
    """
    