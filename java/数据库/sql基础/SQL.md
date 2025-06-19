# 基本语句
## 关键字
`select where between and or delete update like regexp order by desc `
# 语句优化
# 事务及隔离级别
![[Pasted image 20230921152625.png]]
## 事务（transaction）
>[!definition]
>事务是任务集合构成的执行单元，只存在两种结果（成功或失败）
>具有ACID特性

```sql
begin transaction transaction_name; #开启事务
set TRANSACTION [ READ WRITE | READ ONLY ]; #设定事务的隔离级别和访问模式
SAVEPOINT SAVEPOINT_NAME;　＃创建保存点
commit;
rollback; #回滚至最近的一个commited transaction的状态
rollback to savepoint_name; #回滚至特定保存点
RELEASE SAVEPOINT SAVEPOINT_NAME;#释放保存点
```

## 隔离级别
1. 可传行化(serializable )
    等级最高，要求在选定对象上的读锁和写锁直到事务结束后才能释放
1. 可重复读(repeatable read)
    重复读，就是在开始读取数据（事务开启）时，不再允许修改操作，但允许插入操作
1. 提交读 (read commited)
    需要对选定对象的写锁一直保持到事务结束，但是读锁在SELECT操作完成后马上释放
1. 未提交读（read uncommited)
    是最低的隔离级别。允许“脏读”（dirty reads），事务可以看到其他事务“尚未提交”的修改
    
|隔离级别|写操作|读操作|范围操作 (...where...)|
|---|---|---|---|
|未提交读|S|S|S|
|提交读|C|S|S|
|可重复读|C|C|S|
|可序列化|C|C|C|
# 索引
## 分类
1. 聚集索引（指向具体对应的数据模组）
2. 非聚集索引（指向下一个索引模块）
- Data retrieval is speed up by the usage of indexes.
- They function as a database row’s table of contents.
- Enhance query speed, however, inserts and updates might take longer.
- Bitmap, Hash, and B-tree indexes are examples of typical types.
- Indexes must be carefully selected and kept up-to-date in order for database operations to go smoothly
# 锁
数据库实现锁功能的数据结构成为[[锁表]]
# 数据库的底层数据结构
- Btree
- B+tree(B-tree的一种变体，数据存储在叶节点，然后叶节点间用双向链表连接)
![[Pasted image 20230922130920.png]]
- hash
## 常用数据库引擎
- MyISAM
- MEMORY
- INNODB
