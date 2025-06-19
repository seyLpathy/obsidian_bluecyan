# spring framework JDBC classes 
## JdbcTemplate
- 创建和关闭与数据库的连接
- 处理异常并提供通知性异常信息，相关包org.springframework.dao
  
|Method|Description|
|--|----|
|public int update(String query)|is used to insert, update and delete records.|
|public int update(String query,Object... args)|is used to insert, update and delete records using PreparedStatement using given arguments.|
|public void execute(String query)|is used to execute DDL query.|
|public T execute(String sql, PreparedStatementCallback action)|executes the query by using PreparedStatement callback.|
|public T query(String sql, ResultSetExtractor rse)|is used to fetch records using ResultSetExtractor.|
public List query(String sql, RowMapper rse)|is used to fetch records using RowMapper.|

```xml
<?xml version="1.0" encoding="UTF-8"?>  
<beans  
    xmlns="http://www.springframework.org/schema/beans"  
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  
    xmlns:p="http://www.springframework.org/schema/p"  
    xsi:schemaLocation="http://www.springframework.org/schema/beans   
http://www.springframework.org/schema/beans/spring-beans-3.0.xsd">  
  
<bean id="ds" class="org.springframework.jdbc.datasource.DriverManagerDataSource">  
<property name="driverClassName" value="oracle.jdbc.driver.OracleDriver" />  
<property name="url" value="jdbc:oracle:thin:@localhost:1521:xe" />  
<property name="username" value="system" />  
<property name="password" value="oracle" />  
</bean>  
  
<bean id="jdbcTemplate" class="org.springframework.jdbc.core.JdbcTemplate">  
<property name="dataSource" ref="ds"></property>  
</bean>  
  
<bean id="edao" class="com.javatpoint.EmployeeDao">  
<property name="jdbcTemplate" ref="jdbcTemplate"></property>  
</bean>  
  
</beans>  
```

```java
package com.javatpoint;  
import org.springframework.jdbc.core.JdbcTemplate;  
  
public class EmployeeDao {  
private JdbcTemplate jdbcTemplate;  
  
public void setJdbcTemplate(JdbcTemplate jdbcTemplate) {  
    this.jdbcTemplate = jdbcTemplate;  
}  
  
public int saveEmployee(Employee e){  
    String query="insert into employee values(  
    '"+e.getId()+"','"+e.getName()+"','"+e.getSalary()+"')";  
    return jdbcTemplate.update(query);  
}  
public int updateEmployee(Employee e){  
    String query="update employee set   
    name='"+e.getName()+"',salary='"+e.getSalary()+"' where id='"+e.getId()+"' ";  
    return jdbcTemplate.update(query);  
}  
public int deleteEmployee(Employee e){  
    String query="delete from employee where id='"+e.getId()+"' ";  
    return jdbcTemplate.update(query);  
}  
  
}  
```
### Example of PreparedStatement in Spring
```java
public T execute(String sql,PreparedStatementCallback<T>);
public T doInPreparedStatement(PreparedStatement ps)throws SQLException, DataAccessException   
```
example
```java
//employeeDao.java
package com.javatpoint;  
import java.sql.PreparedStatement;  
import java.sql.SQLException;  
import org.springframework.dao.DataAccessException;  
import org.springframework.jdbc.core.JdbcTemplate;  
import org.springframework.jdbc.core.PreparedStatementCallback;  
public class EmployeeDao {  
private JdbcTemplate jdbcTemplate;    
public void setJdbcTemplate(JdbcTemplate jdbcTemplate) {  
    this.jdbcTemplate = jdbcTemplate;  
}  
public Boolean saveEmployeeByPreparedStatement(final Employee e){  
    String query="insert into employee values(?,?,?)";  
    return jdbcTemplate.execute(query,new PreparedStatementCallback<Boolean>(){  
    @Override  
    public Boolean doInPreparedStatement(PreparedStatement ps)throws SQLException, DataAccessException {      
        ps.setInt(1,e.getId());  
        ps.setString(2,e.getName());  
        ps.setFloat(3,e.getSalary());     
        return ps.execute();         
    }  
    });  
}   
}  
```

### ResultSetExtractor Example
```java
public T query(String sql,ResultSetExtractor<T> rse)
public T extractData(ResultSet rs)throws SQLException,DataAccessException  

// dao.java
package com.javatpoint;  
import java.sql.ResultSet;  
import java.sql.SQLException;  
import java.util.ArrayList;  
import java.util.List;  
import org.springframework.dao.DataAccessException;  
import org.springframework.jdbc.core.JdbcTemplate;  
import org.springframework.jdbc.core.ResultSetExtractor;  
public class EmployeeDao {  
private JdbcTemplate template;  
public void setTemplate(JdbcTemplate template) {  
    this.template = template;  
}  
public List<Employee> getAllEmployees(){  
 return template.query("select * from employee",new ResultSetExtractor<List<Employee>>(){  
    @Override  
     public List<Employee> extractData(ResultSet rs) throws SQLException,  
            DataAccessException {  
        List<Employee> list=new ArrayList<Employee>();  
        while(rs.next()){  
        Employee e=new Employee();  
        e.setId(rs.getInt(1));  
        e.setName(rs.getString(2));  
        e.setSalary(rs.getInt(3));  
        list.add(e);  
        }  
        return list;  
        }  
    });  
  }  
}  
```
### RowMapper Example
```java
public T query(String sql,RowMapper<T> rm)  
public T mapRow(ResultSet rs, int rowNumber)throws SQLException  

//dao.java
package com.javatpoint;  
import java.sql.ResultSet;  
import java.sql.SQLException;  
import java.util.ArrayList;  
import java.util.List;  
import org.springframework.dao.DataAccessException;  
import org.springframework.jdbc.core.JdbcTemplate;  
import org.springframework.jdbc.core.ResultSetExtractor;  
import org.springframework.jdbc.core.RowMapper;  
public class EmployeeDao {  
private JdbcTemplate template;  
public void setTemplate(JdbcTemplate template) {  
    this.template = template;  
}  
public List<Employee> getAllEmployeesRowMapper(){  
 return template.query("select * from employee",new RowMapper<Employee>(){  
    @Override  
    public Employee mapRow(ResultSet rs, int rownumber) throws SQLException {  
        Employee e=new Employee();  
        e.setId(rs.getInt(1));  
        e.setName(rs.getString(2));  
        e.setSalary(rs.getInt(3));  
        return e;  
    }  
    });  
}  
}  
```
## NamedParameterJdbcTemplate
```java
insert into employee values (:id,:name,:salary)  
pubic T execute(String sql,Map map,PreparedStatementCallback psc)  
// dao.java
package com.javatpoint;  
import java.sql.PreparedStatement;  
import java.sql.SQLException;  
import org.springframework.dao.DataAccessException;  
import org.springframework.jdbc.core.PreparedStatementCallback;  
import org.springframework.jdbc.core.namedparam.NamedParameterJdbcTemplate;  
import java.util.*;  
public class EmpDao {  
NamedParameterJdbcTemplate template;   
public EmpDao(NamedParameterJdbcTemplate template) {  
        this.template = template;  
}  
public  void save (Emp e){  
String query="insert into employee values (:id,:name,:salary)";  
Map<String,Object> map=new HashMap<String,Object>();  
map.put("id",e.getId());  
map.put("name",e.getName());  
map.put("salary",e.getSalary());  
template.execute(query,map,new PreparedStatementCallback() {  
    @Override  
    public Object doInPreparedStatement(PreparedStatement ps)  
            throws SQLException, DataAccessException {  
        return ps.executeUpdate();  
    }  
});  
}  
}  
```


## SimpleJdbcTemplate
```java
package com.javatpoint;  
import org.springframework.jdbc.core.simple.SimpleJdbcTemplate;  
public class EmpDao {  
SimpleJdbcTemplate template;  
public EmpDao(SimpleJdbcTemplate template) {  
        this.template = template;  
}  
public int update (Emp e){  
String query="update employee set name=? where id=?";  
return template.update(query,e.getName(),e.getId());  
}   
} 
```
 
- SimpleJdbcInsert and SimpleJdbcCall 
# Dao class
![Alt text](JavaScript/image-3.png)