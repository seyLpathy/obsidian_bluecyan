>[!definition]
Object Relational Mapping (ORM) is a functionality which is used to develop and maintain a relationship between an object and relational database by mapping an object state to database column
![Alt text](图片/image-6.png)
# trait
## direction
- Unidirectional relationship
- Bidirectional relationship
## type
- One-to-one This association is represented by @OneToOne annotation. instance of each entity is related to a single instance of another entity.
- One-to-many - This association is represented by @OneToMany annotation. In this relationship, an instance of one entity can be related to more than one instance of another entity.
- Many-to-one This mapping is defined by @ManyToOne annotation. In this relationship, multiple instances of an entity can be related to single instance of another entity.
- Many-to-many This association is represented by @ManyToMany annotation. Here, multiple instances of an entity can be related to multiple instances of another entity. In this mapping, any side can be the owing side.
# JPA entity
## Entity Properties
- 持久性 (对象存储在数据库可随时访问)
- 永久标识 (java对象标识)
- 事务性（维持数据库的事务操作的原子性）
## metadata(元数据)
- annotation
- XML file
# 创建JPA实体
## java对象的要求
- 无参构造器
- 注解
```java
import javax.persistence.*;  
@Entity  // JPA实体
@Table(name="student")  
public class Student {  
    @Id  //主键 永久标识
    private int id;  
    private String name;  
    private long fees;  
    public Student() {}  
    public Student(int id)   
     {  
        this.id = id;  
         }  
    public int getId()   
     {  
        return id;  
         }  
    public void setId(int id)   
     {  
        this.id = id;  
         }  
    public String getName()  
     {  
        return name;   
         }  
    public void setName(String name)   
     {  
        this.name = name;  
         }  
    public long getFees()  
     {  
        return fees;  
         }  
    public void setFees (long fees)  
     {  
        this.fees = fees;  
     }   
}  
```
# JPA实体管理器
## functions
- 用单一接口封装entity
- 读取/构造/删除 entity
- 管理entity
## 构建
```java
// Creating an entity manager factory object
EntityManagerFactory emf = PersistencecreateEntityManagerFactory("Student_details"); 
// Obtaining an entity manager from factory.
EntityManager em=emf.createEntityManager(); 
// Intializing an entity manager.
em.getTransaction().begin();  
// Persisting a data into relational database.
em.persist(s1); 
// Closing the transaction
em.getTransaction().commit();  
//Releasing the factory resources.
emf.close();  
em.close();  
```
# insert/find/update/delete
```xml
// persistence.xml
<persistence>  
<persistence-unit name="Student_details">      
    <class>com.javatpoint.jpa.student.StudentEntity</class>  
<properties>  
<property name="javax.persistence.jdbc.driver" value="com.mysql.jdbc.Driver"/>  
<property name="javax.persistence.jdbc.url" value="jdbc:mysql://localhost:3306/studentdata"/>  
<property name="javax.persistence.jdbc.user" value="root"/>  
<property name="javax.persistence.jdbc.password" value=""/>  
<property name="eclipselink.logging.level" value="SEVERE"/>  
<property name="eclipselink.ddl-generation" value="create-or-extend-tables"/>  
</properties>  
    </persistence-unit>  
</persistence>  
```

```java
// operation/entity manager
package com.javatpoint.jpa.find;  
  
import javax.persistence.*;  
  
import com.javatpoint.jpa.student.*;  
  
public class FindStudent {  
    public static void main(String args[])  
    {  
        EntityManagerFactory emf=Persistence.createEntityManagerFactory("Student_details");  
        EntityManager em=emf.createEntityManager();           
		em.getTransaction().begin();  
		// insert a entity 
		StudentEntity s2=new StudentEntity();  
        s2.setS_id(102);  
        s2.setS_name("Ronit");  
        s2.setS_age(22);   
		// select a entity   
        StudentEntity s=em.find(StudentEntity.class,101);   
		// update a entity
		StudentEntity s=em.find(StudentEntity.class,102);  
		s.setS_age(30);  
		// remove an entity
		StudentEntity s=em.find(StudentEntity class,102);  
		em.remove(s);  
    }  
}  
```
## collection mapping
@ElementCollection
```java
@ElementCollection  //标注内部镶嵌类
private List<Address> address=new ArrayList<Address>(); 
```

```java 
// 镶嵌对象
@Embeddable  
public class Address { }
```

```java
//entity operation
Address a1=new Address();  
a1.setE_pincode(201301);  
a1.setE_city("Noida");  
a1.setE_state("Uttar Pradesh");
Employee e1=new Employee();  
e1.setE_id(1);  
e1.setE_name("Vijay");  
e1.getAddress().add(a1); 
em.persist(e1);   
```
- 实体间映射关系
```java
@Entity  
public class Library {  
    @Id  
    @GeneratedValue(strategy=GenerationType.AUTO)  
private int b_id;  
private String b_name;  
@OneToOne  
private Student stud;
}
public class Student {  
@Id  
@GeneratedValue(strategy=GenerationType.AUTO)  
private int s_id;  
private String s_name;  
@OneToMany(targetEntity=Library.class)  
private List books_issued;  
}
@ManyToOne  
private Library lib;  
@ManyToMany(targetEntity=Student.class)  
private List stud;  
```
## cascade operations(关联操作)
|Cascade Operations|Description|
|--|-----|
|PERSIST|In this cascade operation, if the parent entity is persisted then all its related entity will also be persisted.|
|MERGE|In this cascade operation, if the parent entity is merged then all its related entity will also be merged.|
|DETACH|In this cascade operation, if the parent entity is detached then all its related entity will also be detached.|
|REFRESH|In this cascade operation, if the parent entity is refreshed then all its related entity will also be refreshed.|
|REMOVE|In this cascade operation, if the parent entity is removed then all its related entity will also be removed.|
|ALL|In this case, all the above cascade operations can be applied to the entities related to parent entity.|
1. @OneToOne(cascade=CascadeType.PERSIST) (父实体插入)
2. @OneToOne(cascade=CascadeType.REMOVE)  (父实体移除)

# JPA JPQL Introduction
>[!definition]the role of JPA is to transform JPQL into SQL. Thus, it provides an easy platform for developers to handle SQL tasks.
## JPQL Features
1. It is a platform-independent query language.
2. It is simple and robust.
3. It can be used with any type of database such as MySQL, Oracle.
4. JPQL queries can be declared statically into metadata or can also be dynamically built in code.
## Creating Queries in JPQL
```java
Query query = em.createQuery("Select s.s_name from StudentEntity s"); 
createNamedQuery(name = "find name" , query = "Select s from StudentEntity s")  
```
## basic operation
### **fetch single column**
```java
Query query = em.createQuery("Select s.s_name from StudentEntity s");  
@SuppressWarnings("unchecked")  
List<String> list =query.getResultList();  
System.out.println("Student Name :");  
for(String s:list) {  
    System.out.println(s);  
}  
```
### fetch all columns
```java
Query query = em.createQuery( "Select s from StudentEntity s ");  
@SuppressWarnings("unchecked")  
List<StudentEntity> list=(List<StudentEntity>)query.getResultList( );      
    System.out.print("s_id");  
    System.out.print("\t s_name");  
    System.out.println("\t s_age");   
    for( StudentEntity s:list ){  
        System.out.print( s.getS_id( ));  
        System.out.print("\t" +  s.getS_name( ));  
        System.out.print("\t" + s.getS_age( ));  
        System.out.println();  
    }  
```
### update records
```java
Query query = em.createQuery( "update StudentEntity SET s_age=25 where s_id>103");  
query.executeUpdate();  
```
### delete records
```java
Query query = em.createQuery( "delete from StudentEntity where s_id=102");  
query.executeUpdate();  
```
# JPA criteria API
```java
EntityManager em = emf.createEntityManager();  
CriteriaBuilder cb=em.getCriteriaBuilder();  
CriteriaQuery<StudentEntity> cq=cb.createQuery(StudentEntity.class);  
Root<StudentEntity> stud=cq.from(StudentEntity.class);
CriteriaQuery<StudentEntity> select = cq.select(stud);  
Query q = em.createQuery(select);  
List<StudentEntity> list = q.getResultList();
```

|Clause|Criteria API Interface|Methods|
|--|--|--|
SELECT|CriteriaQuery|select()|
FROM|AbstractQuery|from()|
WHERE|AbstractQuery|where()|
ORDER BY|CriteriaQuery|orderBy()|
GROUP BY|AbstractQuery|groupBy()|
HAVING|AbstractQuery|having()|
# JPA Inheritence
@Inheritence - This annotation is applied on the root entity class to define the inheritance strategy. 
@MappedSuperclass - This annotation is applied to the classes that are inherited by their subclasses. 
@DiscriminatorColumn - The discriminator attribute differentiates one entity from another. Thus, this annotation is used to provide the name of discriminator column. It is required to specify this annotation on the root entity class only.
@DiscriminatorValue - This annotation is used to specify the type of value that represents the particular entity. It is required to specify this annotation on the sub-entity classes.
## Hibernate and Spring Integration
## HibernateTemplate class

# [[mybatis]]