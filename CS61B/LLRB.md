#data_structure 
>[!issues about B-trees implementation]
1.Maintaining different node types.
2.Interconversion of nodes between 2-nodes and 3-nodes.
3.Walking up the tree to split nodes

> 优美的算法可能在实际应用中并不具有同样的效用

## tree rotation 

|direction|definition|tuitive abstraction|implementation|
|--------|-------------|---------------------|------------------------|
|right|rotateLeft(G): Let x be the right child of G. Make G the new left child of x.|以其右子树为轴心逆时针旋转成为后者的左子树|假定X为该节点的右子节点，先将X与当前节点合并，然后将该节点转为X的左子节点|
|left|rotateRight(P): Let x be the left child of P. Make P the new right child of x.|以其左子树为轴心顺时针旋转成为后者的右子树|假定X为该节点的左子节点，先将X与当前节点合并，然后将该节点转为X的右子节点

>[!summary]
>tree rotation能够保证树的平衡，但实现难度过大
***但目前没有算法能够实现tree rotation这一算法***

## red black trees
结构上继承[[B-tree(2-3 tree)|B tree]] balanced 特性的BST
case1 节点只有一个元素
- 则与基础BST毫无差别
case2  节点有两个元素
- solution1 : ~~~~创造一个空节点（dummy node) wasted link,ugly code 
- solution2 : ==在两元素间创造"glue" link,红线标注，较小者作为较大者的左子节点==
LLRB height = H(black) + H+1(red)
>[!important property]
>- No node has two red links 
>- Every path from root to a null has same number of black links because 2-3 trees have the same number of links to every leaf. LLRBs are therefore balanced.
    

### construction of LLRB
- insert as usual into a BST(==new values are always added to a leaf node==)
- use zero or more rotations to maintain the 1-1 mapping (==how to implement by algorithm==)
basic rules
- ====When inserting: Use a red link.
- ====If there is a right leaning “3-node”, we have a Left Leaning Violation.Rotate left the appropriate node to fix
- ====If there are two consecutive left links, we have an Incorrect 4 Node ViolationRotate right the appropriate node to fix
- =====If there are any nodes with two red children, we have a Temporary 4 Node
- ====Color flip the node to emulate the split operation

## extension 
other self balanced trees: **AVL trees, splay trees, treaps**
Other linked structures:**Skip lists are linked lists with express lanes**

LLRB = [[BST]] + [[B-tree(2-3 tree)]]


