# IOC container
## functions
- instantiate the application class
- configure the object
- assemble the dependencies between the objects
## types
### beanfactory
```java
Resource resource=new ClassPathResource("applicationContext.xml");  
BeanFactory factory=new XmlBeanFactory(resource); 
```
### ApplicationContext
```java
ApplicationContext context =   
    new ClassPathXmlApplicationContext("applicationContext.xml"); 
```
# Dependency Injection 
## 实现方法
### constructor 单一对象
\<constructor-arg value="x" type="datatype>\<constructor-arg>,默认type为string
```java
package com.javatpoint;  
  
public class Employee {  
private int id;  
private String name;  
  
public Employee() {System.out.println("def cons");}  
  
public Employee(int id) {this.id = id;}  
  
public Employee(String name) {  this.name = name;}  
  
public Employee(int id, String name) {  
    this.id = id;  
    this.name = name;  
}  
  
void show(){  
    System.out.println(id+" "+name);  
}  
  
}  
```
```xml
<?xml version="1.0" encoding="UTF-8"?>  
<beans  
    xmlns="http://www.springframework.org/schema/beans"  
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  
    xmlns:p="http://www.springframework.org/schema/p"  
    xsi:schemaLocation="http://www.springframework.org/schema/beans  
                http://www.springframework.org/schema/beans/spring-beans-3.0.xsd">  
  
<bean id="e" class="com.javatpoint.Employee">  
<constructor-arg value="10" type="int"></constructor-arg>  
</bean>  
  
</beans>  
```
```java
  //test.java
package com.javatpoint;  
  
import org.springframework.beans.factory.BeanFactory;  
import org.springframework.beans.factory.xml.XmlBeanFactory;  
import org.springframework.core.io.*;  
  
public class Test {  
    public static void main(String[] args) {  
          
        Resource r=new ClassPathResource("applicationContext.xml");  
        BeanFactory factory=new XmlBeanFactory(r);  
          
        Employee s=(Employee)factory.getBean("e");  
        s.show();  
          
    }  
}  
```
- 注入依赖对象时采用\<ref bean="beanID">可以将对象作为参数输入
- 集合参数注入list,map,
```xml
<constructor-arg>  
<list>  
<value>Java is a programming language</value>  
<value>Java is a Platform</value>  
<value>Java is an Island of Indonasia</value>  
</list>  
</constructor-arg>  
```

```xml
<map>  
<entry key-ref="answer1" value-ref="user1"></entry>  
<entry key-ref="answer2" value-ref="user2"></entry>  
</map> 
```
- bean的继承
```java
//employee.java
package com.javatpoint;  
  
public class Employee {  
private int id;  
private String name;  
private Address address;  
public Employee() {}  
  
public Employee(int id, String name) {  
    super();  
    this.id = id;  
    this.name = name;  
}  
public Employee(int id, String name, Address address) {  
    super();  
    this.id = id;  
    this.name = name;  
    this.address = address;  
}  
  
void show(){  
    System.out.println(id+" "+name);  
    System.out.println(address);  
}  
  
}  
```

```java
//address.java
package com.javatpoint;  
  
public class Address {  
private String addressLine1,city,state,country;  
  
public Address(String addressLine1, String city, String state, String country) {  
    super();  
    this.addressLine1 = addressLine1;  
    this.city = city;  
    this.state = state;  
    this.country = country;  
}  
public String toString(){  
    return addressLine1+" "+city+" "+state+" "+country;  
}  
  
}  
```

```xml
applicationcontext.xml
<?xml version="1.0" encoding="UTF-8"?>  
<beans  
    xmlns="http://www.springframework.org/schema/beans"  
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  
    xmlns:p="http://www.springframework.org/schema/p"  
    xsi:schemaLocation="http://www.springframework.org/schema/beans   
http://www.springframework.org/schema/beans/spring-beans-3.0.xsd">  
  
<bean id="e1" class="com.javatpoint.Employee">  
<constructor-arg value="101"></constructor-arg>  
<constructor-arg  value="Sachin"></constructor-arg>  
</bean>  
  
<bean id="address1" class="com.javatpoint.Address">  
<constructor-arg value="21,Lohianagar"></constructor-arg>  
<constructor-arg value="Ghaziabad"></constructor-arg>  
<constructor-arg value="UP"></constructor-arg>  
<constructor-arg value="USA"></constructor-arg>  
</bean>  
  
<bean id="e2" class="com.javatpoint.Employee" parent="e1">  
<constructor-arg ref="address1"></constructor-arg>  
</bean>  
  
</beans>  
```
- getBean()的返回值需要进行强制转换
  ![Alt text](JavaScript/image-2.png)
### setter method
- 赋值(property name="" value)
```xml
<?xml version="1.0" encoding="UTF-8"?>  
<beans  
    xmlns="http://www.springframework.org/schema/beans"  
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  
    xmlns:p="http://www.springframework.org/schema/p"  
    xsi:schemaLocation="http://www.springframework.org/schema/beans  
                http://www.springframework.org/schema/beans/spring-beans-3.0.xsd">  
  
<bean id="obj" class="com.javatpoint.Employee">  
<property name="id">  
<value>20</value>  
</property>  
<property name="name">  
<value>Arun</value>  
</property>  
<property name="city">  
<value>ghaziabad</value>  
</property>  
  
</bean>  
  
</beans> 
```
- 依赖对象
```xml
<property name="address" ref="address1"></property> 
```
- 集合

```xml
<property name="answers">  
<list>  
<value>Java is a programming language</value>  
<value>Java is a platform</value>  
<value>Java is an Island</value>  
</list>  
</property> 
```
- 对象集合
```xml
<list>  
<ref bean="answer1"/>  
<ref bean="answer2"/>  
</list>  
```
- 纯文本集合
```xml
<map>  
<entry key="Java is a programming language"  value="Sonoo Jaiswal"></entry>  
<entry key="Java is a Platform" value="Sachin Yadav"></entry>  
</map>
```
- 对象集合
```xml
<map>  
<entry key-ref="answer1" value-ref="user1"></entry>  
<entry key-ref="answer2" value-ref="user2"></entry>  
</map>  
```
### 差异
- 部分依赖
- setter override constructor
- setter injection can change values easily
### autowiring(自动装配)
仅用于对象索引，不可用于赋值
|Mode|Description|
|--|----|
|no|It is the default autowiring mode. It means no autowiring bydefault.|
|byName|bean ID与指向名相同|
|byType|class类型一致，但只能创造一个|
|constructor|优先调用参数最多的构造函数进行配置|
### 工厂方法

