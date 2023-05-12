"""
Given the root of a binary tree, return the sum of all left leaves.
A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.
"""
def sumOfLeftLeaves(root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
        Time:12mins 18sec
        Solve: yes
        Difficulty: Easy 
        Comments: This is a classic tree search question that stutter me in the beginning because I was trying to implement it in recursion,
        but I couldn't think about it(IMO: I'm just bad at recursion), I think iteration is easier because you just need a stack or Queue
        and everytime at a node just check whether it has a left node or not, then check whether this node is a leaf or not . 

        """
        stack = []
        stack.append(root)
        count = 0 
        while(stack):
            node = stack.pop()
            if(node.left != None and node.left.left == None and node.left.right == None):
                count+= node.left.val
            if(node.left != None):
                stack.append(node.left)
            if(node.right != None):
                stack.append(node.right)
        return count 

        """
        I guess once implement the iteration way, the recursion way is not that diffcult

        Recursion implementation: 

        def sumOfLeftLeaves(self, root)
            if(root == None):
                return 0 
            else:
                left = self.sumOfLeftLeaves(root.left)
                right = self.sumOfLeftLeaves(root.right)
                if(root.left != None and root.left.left == None and root.left.right == None):
                    return root.left.val+left+right
                return left + right
        """
