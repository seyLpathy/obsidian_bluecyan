## definition
1. 节点的集合
2.  节点间相互连接，两个节点间只有一道通路
3.  除了根节点其他所有节点只有一个父节点
4. 父节点为节点到根结点通路上的第一个节点
## representation in java
1. creating mapping from node to children
```java
public class Tree1A<Key> {
Key k; // e.g. 0      //direct link by class level
Tree1A left;
Tree1A middle;
Tree1A right;
...
```

```java
public class Tree1B<Key> {
Key k;                           // using array to store children nodes 
Tree1B[] children;
```

```java
public class Tree1C<Key> {
Key k; // degenerate into linked list
Tree1C favoredChild;
Tree1C sibling;          
```
2. 对每一个节点而言，将所有节点的键值存储于数列，对应的父节点ID也存储于另一个数列（如果是bushy tree,则parent ID数列呈现特定的规律排列）
![[Pasted image 20230817131228.png]]
3. 将键值存储在数列中，不存储结构信息（假定：树结构完整，只适用于完整的树）
4. 基于方法3 进行优化，将数列第一位置空。所有节点偏移一个
    - leftChild(k) = k \* 2
    - rightChild(k) = k\*2 +１
    - parent(k) = k/2 
## tree traversal(树的遍历) 从上至下，从左至右
1. DFT（深度优先遍历）

|methods|orders|
|-----|------|
|preorder|x.key-->x.left-->x.right|
|inorder|x.left-->x.key-->x.right|
|postorder|x.left-->x.right-->x.key|

visual trick for postorder
![[Pasted image 20230817135129.png]]
#data_structure 


