---
title: think in jjava
created: 2026-09-03 22:48
updated: 2026-09-03 22:48
tags:
  - 笔记
finished: false
type:
  - mindstorm
  - java
  - programming
author: bluecyan
---

## 摘要
>[!abstract]
>start from here ...
>

### class access 
1. 类不能用private或者protected修饰，如果需要限制访问，可以构建private constructor


### inner class/nested class
1. 用static修饰的内部类即为nested类，可以作为类单独使用，无需透过外部类进行连接使用

2. class也能nested于interface，如果你需要interface使用部分公用代码
3. nested class 可以直接访问enclosed class的成员或方法，不考虑嵌套层数
4. 使用inner class可以同时implements concrete class and abstract class
5. 
