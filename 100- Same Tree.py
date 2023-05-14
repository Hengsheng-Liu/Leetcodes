"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""
def isSameTree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    Time:15mins 14sec
    Solve: yes
    Difficulty: Easy 
    Comments:
    I think this question is not hard and I first thought Inorder traversal solves which I also need 2N space to store both tree,
    which is not an efficient solution. After look at solution I realized that is easy if you just pass in both tree into the recursion which 
    I got stuck like how do we traverse two tree at the same time 
    """
    def inorder(self,root):
        if root == None:
            return None 
        else:
            return  [self.inorder(root.left)]+ [root.val]+ [self.inorder(root.right)]
    tree1 = inorder(p)
    tree2 = inorder(q)
    return tree1 == tree2 
    """
        Comments: 
            The offical solution is actually pretty easy if you know double recursion on the two sub-tree
        def isSameTree(self, p, q):
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        elif p.val != q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
    """