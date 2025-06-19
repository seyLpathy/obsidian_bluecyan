all [[Tree]] are graph
## definition
1. 节点的集合
2.  零个或者多个连线用于连接连个节点间相互连接
simple graph（主要讨论内容）
1. 没有节点构成自循环
2. 两个节点不构成循环
![[Pasted image 20230817135843.png]]
## graph problems
● ==s-t Path. Is there a path between vertices s and t?==
● Connectivity. Is the graph connected, i.e. is there a path between all vertices?
● Biconnectivity. Is there a vertex whose removal disconnects the graph?
● Shortest s-t Path. What is the shortest path between vertices s and t?
● Cycle Detection. Does the graph contain any cycles?
● Euler Tour. Is there a cycle that uses every edge exactly once?
● Hamilton Tour. Is there a cycle that uses every vertex exactly once?
● Planarity. Can you draw the graph on paper with no crossing edges?
● Isomorphism. Are two graphs isomorphic (the same graph in disguise)?

### s-t Connectivity(该方法优先探索深度DFT)
● Mark s.
● Does s == t? If so, return true.
● Otherwise, if connected(v, t) for any unmarked neighbor v of s, return true.
● Return false

## tree traversal
Depthfirstpaths:寻找一条路径前往其他节点，每个节点最多访问一次
1 DFS preorder
- Mark v.
- For each unmarked adjacent vertex w:
    - set edgeTo\[w\] = v. ==（action before dfs）==
    - dfs(w)    ==(等价于preorder calls)==
2  DFS postorder
- mark s
- for each unmarked neighbor n of s,dfs(n)  ==(action after dfs)
- print(s)  ==(dfs 函数的返回顺序)==
3 bfs order
Action in order of distance from s （宽度优先查找）