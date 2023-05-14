"""
You are given the root of a binary search tree (BST), 
where the values of exactly two nodes of the tree were swapped by mistake.
Recover the tree without changing its structure.
"""
def inorder(self, root, nodes):
        if not root:
            return nodes # return [] 

        nodes = self.inorder(root.left, nodes) # we recurse the whole left tree based on the orde of Inorder traversal, keep going left, then check mid, then right

        prev,first,second = nodes # destructuring the list to make it more readable
        if prev and prev.val > root.val: # if prev exist, and is in ascend order, the previous node should have a smaller value than current node 
            if not nodes[1]: # first node is always fix, once we found it. 
                nodes[1] = nodes[0]                              
                            # the second node you probably have to keep going down to find the smallest value that's less than 
            nodes[2] = root # first, let's say the tree inorder is [3,2,1], the first value has to be 3, but then the second value 
                            # you find 2 as the second value first since 3 > 2, but then also 1 as well because 2 > 1  
        nodes[0] = root # just keep setting the current node to prev 
 
        nodes = self.inorder(root.right, nodes) # after looking at middle, search the right subree 

        return nodes

def recoverTree(self, root):
    """
    :type root: TreeNode
    :rtype: None Do not return anything, modify root in-place instead.

    Time: too long 
    Solve: No 
    Difficulty: Medium 
    Comments:
    I peronsally think question is hard bro, it makes sense for me that inorder traversal grants the ascending order of binary search tree, but 
    how to track these two nodes kinda stuck me, I was looking at iterative solution and I just don't understand(too hard to wrap around)
    However, I think the recursion implmentation make much more sense 
    """
    nodes = self.inorder(root, [None, None, None])
    nodes[1].val, nodes[2].val = nodes[2].val, nodes[1].val
    