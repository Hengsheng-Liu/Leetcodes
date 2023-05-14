"""
Given an undirected tree consisting of n vertices numbered from 0 to n-1, which has some apples in their vertices. You spend 1 second to walk over one edge of the tree. Return the minimum time in seconds you have to spend to collect all apples in the tree, starting at vertex 0 and coming back to this vertex.

The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi. Additionally, there is a boolean array hasApple, where hasApple[i] = true means that vertex i has an apple; otherwise, it does not have any apple.
"""
def minTime(n, edges, hasApple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        Time:Noone
        Solve: No
        Difficulty: Medium 
        Comments:
        First I thought use BFS, then the shit is so complicated using BFS, because you need to calculate the level is at 
        and then do like 2*level because each level you go down and up is 2 operation. SO MANY EDGE CASES. After, I check the solution,
        Lmfao. The DFS solution is much sense and easy to implement. Keep going down to the leaf node and then if there is an apple then plus 2
        any node is being visited in that path also + 2 but the DFS already help us on it. I guess because the structure of this question is a 
        graph not a tree, thus you need to create a bi-direction graph. I try to create single direction graph, but it doesn't work on a test case
        """
        def dfs(curr, par, adj_list):
            total = 0
            for child in adj_list[curr]:
                if child != par:
                    child_time = dfs(child, curr, adj_list)
                    if child_time > 0 or hasApple[child]:
                        total += child_time + 2
            return total

        adj_list = {i: [] for i in range(n)}
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        total_time = dfs(0, -1, adj_list)
        return total_time  

