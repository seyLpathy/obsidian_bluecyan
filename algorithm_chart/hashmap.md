# indexing

![[Drawing 2024-06-28 18.51.27.excalidraw]]

可以理解为用空间换时间，target-value的值和当前遍历数组的index作为键值组存到record中，这样可以在一边遍历的情况下判断出结果

# count
统计每个hashmap中元素的个数统计，遍历过程中对对应的值进行变化,源字符够成原始hashmap,遍历测试字符时设置逻辑并对应更改hashmap值
![[Drawing 2024-06-28 19.26.35.excalidraw]]
# demtermine the loop
记录循环过程中以计算的值并存入hashmap或者set,判断loop是否会结束
# ranking and continue
本质是实现滑动窗口，既维持特定长度利用hashmap的存取性能进行遍历
![[Drawing 2024-06-29 18.39.54.excalidraw]]
# the consecutive sequeue
遍历数组的同时，统计最长的连续的序列同时剔除以遍历的序列
![[Drawing 2024-06-29 18.56.00.excalidraw]]
