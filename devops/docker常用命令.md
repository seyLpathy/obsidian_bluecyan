![[Pasted image 20250927203422.png]]
## docker 网络基础
```sh
docker network ls  //查询docker 网络信息
docker network create xx 创建默认为bridge类型的网络
docker network connect/disconnect xx containername 将容器与指定网络相连/断开
docker run/create --network <network identifier>

```

### 网络类型
1. bridge 默认网络驱动，多个容器间通讯
2. host 完全独立，只依赖于主机系统
3. macvlan 关联mac地址与容器绑定

![[Pasted image 20251207173350.png]]