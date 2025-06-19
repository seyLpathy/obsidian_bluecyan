# 总览
属于ORM中的一种，实现SQL数据库和java中的对象的映射。
将应用逻辑和数据库语句解耦合
# advantages
![Alt text](image%201.png)
# 配置 config.xml
```xml
<configuration>
   <typeAliases>
      <typeAlias alias = "class_alias_Name" type = "absolute_clas_Name"/>
   </typeAliases>
   <objectFactory type="org.mybatis.example.ExampleObjectFactory">
  <property name="someProperty" value="100"/>
</objectFactory>
<!-- 对象工厂 -->
   <environments default = "default_environment _name">
      <environment id = "environment_id">
         <transactionManager type = "JDBC/MANAGED"/>  
		 <!-- 事务管理属性 -->
		 <!-- JDBC 事务管理操作
		 MANAGED数据库连接周期 -->
            <dataSource type = "UNPOOLED/POOLED/JNDI">
			<!-- 线程池控制 -->
               <property name = "driver" value = "database_driver_class_name"/>
               <property name = "url" value = "database_url"/>
               <property name = "username" value = "database_user_name"/>
               <property name = "password" value = "database_password"/>
            </dataSource>        
				
      </environment>
   </environments>
	
   <mappers>
      <mapper resource = "path of the configuration XML file"/>
	  <!-- 指定映射文件位置 -->
	  <mapper url="file:///var/mappers/AuthorMapper.xml"/>
	  <!-- 使用完全限定资源定位符（URL） -->
	  <mapper class="org.mybatis.builder.AuthorMapper"/>
	  <!-- 使用映射器接口实现类的完全限定类名 -->
	  <package name="org.mybatis.builder"/>
	  <!-- 将包内的映射器接口全部注册为映射器 -->
   </mappers>
   
</configuration>
```

```xml
<?xml version = "1.0" encoding = "UTF-8"?>
<!DOCTYPE configuration PUBLIC "-//mybatis.org//DTD Config 3.0//EN" "http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>		
   <environments default = "development">
      <environment id = "development">
         <transactionManager type = "JDBC"/> 			
         <dataSource type = "POOLED">
            <property name = "driver" value = "com.mysql.jdbc.Driver"/>
            <property name = "url" value = "jdbc:mysql://localhost:3306/details"/>
            <property name = "username" value = "root"/>
            <property name = "password" value = "password"/>
         </dataSource>          
      </environment>
   </environments>
   <mappers>
      <mapper resource = "mybatis/Student.xml"/>
   </mappers>
</configuration>
```
# mapping.xml
## 顶级元素
```xml
<!-- cache – 该命名空间的缓存配置。 -->
cache-ref – 引用其它命名空间的缓存配置。
<!-- resultMap – 描述如何从数据库结果集中加载对象，是最复杂也是最强大的元素。 -->
<resultMap id = "result" type = "Student">
   <result property = "id" column = "ID"/>
   <result property = "name" column = "NAME"/>
   <result property = "branch" column = "BRANCH"/>
   <result property = "percentage" column = "PERCENTAGE"/>
   <result property = "phone" column = "PHONE"/>
   <result property = "email" column = "EMAIL"/>
</resultMap>

<select id = "getAll" resultMap = "result">
   SELECT * FROM STUDENT; 
</select>

<select id = "getById" parameterType = "int" resultMap = "result">
   SELECT * FROM STUDENT WHERE ID = #{id};
</select>
<!-- insert – 映射插入语句。 -->
<insert id="insertAuthor">
  insert into Author (id,username,password,email,bio)
  values (#{id},#{username},#{password},#{email},#{bio})
</insert>
<!-- update – 映射更新语句 -->
<update id="updateAuthor">
  update Author set
    username = #{username},
    password = #{password},
    email = #{email},
    bio = #{bio}
  where id = #{id}
</update>
<!-- delete – 映射删除语句-->
<delete id = "deleteById" parameterType = "int">
   DELETE from STUDENT WHERE ID = #{id};
</delete>
<!-- select – 映射查询语句 -->
<select id="selectPerson" parameterType="int" resultType="hashmap">
  SELECT * FROM PERSON WHERE ID = #{id}
</select>
```
## Annotations
```java
import java.util.List;

import org.apache.ibatis.annotations.*;

public interface Student_mapper {
	
   final String getAll = "SELECT * FROM STUDENT"; 
   final String getById = "SELECT * FROM STUDENT WHERE ID = #{id}";
   final String deleteById = "DELETE from STUDENT WHERE ID = #{id}";
   final String insert = "INSERT INTO STUDENT (NAME, BRANCH, PERCENTAGE, PHONE, EMAIL ) VALUES (#{name}, #{branch}, #{percentage}, #{phone}, #{email})";
   final String update = "UPDATE STUDENT SET EMAIL = #{email}, NAME = #{name}, BRANCH = #{branch}, PERCENTAGE = #{percentage}, PHONE = #{phone} WHERE ID = #{id}";
   
   @Select(getAll)
   @Results(value = {
      @Result(property = "id", column = "ID"),
      @Result(property = "name", column = "NAME"),
      @Result(property = "branch", column = "BRANCH"),
      @Result(property = "percentage", column = "PERCENTAGE"),       
      @Result(property = "phone", column = "PHONE"),
      @Result(property = "email", column = "EMAIL")
   })
   List getAll();

   @Select(getById)
   @Results(value = {
      @Result(property = "id", column = "ID"),
      @Result(property = "name", column = "NAME"),
      @Result(property = "branch", column = "BRANCH"),
      @Result(property = "percentage", column = "PERCENTAGE"),       
      @Result(property = "phone", column = "PHONE"),
      @Result(property = "email", column = "EMAIL")
   })
   Student getById(int id);

   @Update(update)
   void update(Student student);

   @Delete(deleteById)
   void delete(int id);

   @Insert(insert)
   @Options(useGeneratedKeys = true, keyProperty = "id")
   void insert(Student student);
}
```
## dynamic SQL
```xml
<!-- if 条件 -->
<select id = "getRecByName" parameterType = "Student" resultType = "Student">

   SELECT * FROM STUDENT		 
   <if test = "name != null">
      WHERE name LIKE #{name}
   </if> 
</select>

<!-- switch语句 -->
<select id = "getRecByName_Id_phone" parameterType = "Student" resultType = "Student">
   SELECT * FROM Student WHERE id != 0
	
   <choose>
      <when test = "name != null">
         AND name LIKE #{name}
      </when> 

      <when test = "phone != null">
         AND phone LIKE #{phone}
      </when>
   </choose>
</select>

<!-- 处理动态异常 -->
<select id = "getName_Id_phone" parameterType = "Student" resultType = "Student">
   SELECT * FROM STUDENT
   <where>
      <if test = "id != null">
         id = #{id}
      </if>
      <if test = "name != null">
         AND name LIKE #{name}
      </if>
   </where>
</select>

<!-- for each  -->
<select id = "selectPostIn" resultType = "domain.blog.Post">
   SELECT *
   FROM POST P
   WHERE ID in
   <foreach item = "item" index = "index" collection = "list"
      open = "(" separator = "," close = ")">
      #{item}
   </foreach>
</select>
```



