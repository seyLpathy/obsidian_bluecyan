#data_structure
***具有某些排序的特性***
- solution1
    ~~创建一个列表存储所有元素，利用比较器进行排序并按照优先级获取特定元素
     内存消耗较大，Θ(N)
- solution2 （MinPQ)
      ==trace top prior P transactions for Q total transactions ==
bushy [[BST]] and Hash Table以及==有序数列==都不适合用有序查询的算法实现

## heaps

特性
1. 完整性：缺失的节点只能存在于最底层，所有节点优先左填充
2.  min-heap: 每个节点小于等于其俩子节点

implementation for heaps
1. getsmallest()  根节点
2. add(x)
优先左填充（从最底层开始填充），根据prior判断是否需要与父节点交换，不断循环该过程直到到达符合条件的位置

![[Pasted image 20230817124325.png]]
![[Pasted image 20230817124850.png]]
![[Pasted image 20230817125029.png]]
3. delete min()
>[!Summary]
● getSmallest() - return the item in the root node.
● add(x) - place the new employee in the last position, and promote as high as possible.
● removeSmallest() - assassinate the president (of the company), promote the rightmost person in the company to    president.Then demote repeatedly, always taking the ‘better’ successor.