#AOP
>[!DEFINITION]AOP breaks the program logic into distinct parts (called concerns). It is used to increase modularity by cross-cutting concerns.
## 概念及术语
### **Join point**
节点 (spring中仅包含方法执行时)
### **Advice(建言)**
	切面在特定节点进行的操作

|type|description|
|--|----|
|Before Advice| it executes before a join point.
After Returning Advice|it executes after a joint point completes normally.|
|After Throwing Advice|it executes if method exits by throwing an exception.|
|After (finally) Advice|it executes after a join point regardless of join point exit whether normally or exceptional return.|
|Around Advice|It executes before and after a join point.|

### **Pointcut**
统一表达式语言中对应节点
### **Introduction**
引入额外的方法和特定类型的域，能够为建言对象引入新的接口
### **Target Object(目标对象)**
被切面建言的对象，也可以称为代理对象，spring中采用实时代理
### **Aspect**
包含建言和节点的类
### **Interceptor**
只包含一种建言的切面aspect
### **AOP Proxy**
 JDK dynamic proxy or CGLIB proxy，实现切面合同
### **Weaving**
连接切面和其他类以构成建言目标对象
## Spring AOP AspectJ Annotation Example
@pointcut(标注节点)
@Apsect(标注切面)
@before(建言类型)
```java
//Operation.java
package com.javatpoint;  
public  class Operation{  
    public void msg(){System.out.println("msg method invoked");}  
    public int m(){System.out.println("m method invoked");return 2;}  
    public int k(){System.out.println("k method invoked");return 3;}  
}  
```

```java
//TrackOperation.java
package com.javatpoint;  
  
import org.aspectj.lang.JoinPoint;  
import org.aspectj.lang.annotation.Aspect;  
import org.aspectj.lang.annotation.Before;  
import org.aspectj.lang.annotation.Pointcut;  
  
@Aspect  
public class TrackOperation{  
    @Pointcut("execution(* Operation.*(..))")  
    public void k(){}//pointcut name  
      
    @Before("k()")//applying pointcut on before advice  
    public void myadvice(JoinPoint jp)//it is advice (before advice)  
    {  
        System.out.println("additional concern");  
        //System.out.println("Method Signature: "  + jp.getSignature());  
    }  
}  
```

```xml
<?xml version="1.0" encoding="UTF-8"?>  
<beans xmlns="http://www.springframework.org/schema/beans"  
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  
    xmlns:aop="http://www.springframework.org/schema/aop"   
       xsi:schemaLocation="http://www.springframework.org/schema/beans   
       http://www.springframework.org/schema/beans/spring-beans.xsd   
       http://www.springframework.org/schema/aop   
       http://www.springframework.org/schema/aop/spring-aop.xsd">  
  
  
    <bean id="opBean" class="com.javatpoint.Operation">   </bean>  
    <bean id="trackMyBean" class="com.javatpoint.TrackOperation"></bean>  
      
    <bean class="org.springframework.aop.aspectj.annotation.AnnotationAwareAspectJAutoProxyCreator"></bean>  
          
</beans> 
```
- **around advice**
```java
// around advice
@Aspect  
public class TrackOperation  
{  
    @Pointcut("execution(* Operation.*(..))")  
    public void abcPointcut(){}  
      
    @Around("abcPointcut()")  
    public Object myadvice(ProceedingJoinPoint pjp) throws Throwable   
    {  
        System.out.println("Additional Concern Before calling actual method");  
        Object obj=pjp.proceed();  
        System.out.println("Additional Concern After calling actual method");  
        return obj;  
    }  
} 
```
- AfterReturning
```java
@Aspect  
public class TrackOperation{  
    @AfterReturning(  
              pointcut = "execution(* Operation.*(..))",  
              returning= "result")  
                
    public void myadvice(JoinPoint jp,Object result)//it is advice (after returning advice)  
    {  
        System.out.println("additional concern");  
        System.out.println("Method Signature: "  + jp.getSignature());  
        System.out.println("Result in advice: "+result);  
        System.out.println("end of after returning advice...");  
    }  
} 
```
- **After**
```java
@Aspect  
public class TrackOperation{  
    @Pointcut("execution(* Operation.*(..))")  
    public void k(){}//pointcut name  
      
    @After("k()")//applying pointcut on after advice  
    public void myadvice(JoinPoint jp)//it is advice (after advice)  
    {  
        System.out.println("additional concern");  
        //System.out.println("Method Signature: "  + jp.getSignature());  
    }  
}  
```

- AfterThrowing
```java
@Aspect  
public class TrackOperation{  
    @AfterThrowing(  
              pointcut = "execution(* Operation.*(..))",  
              throwing= "error")  
                
    public void myadvice(JoinPoint jp,Throwable error)//it is advice  
    {  
        System.out.println("additional concern");  
        System.out.println("Method Signature: "  + jp.getSignature());  
        System.out.println("Exception is: "+error);  
        System.out.println("end of after throwing advice...");  
    }  
}  
```
## Spring AOP AspectJ Xml Configuration Example
```xml
// applicationcontext.xml
<?xml version="1.0" encoding="UTF-8"?>  
<beans xmlns="http://www.springframework.org/schema/beans"  
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"   
    xmlns:aop="http://www.springframework.org/schema/aop"  
    xsi:schemaLocation="http://www.springframework.org/schema/beans  
    http://www.springframework.org/schema/beans/spring-beans-3.0.xsd   
    http://www.springframework.org/schema/aop   
    http://www.springframework.org/schema/aop/spring-aop-3.0.xsd ">    
<aop:aspectj-autoproxy />  
<bean id="opBean" class="com.javatpoint.Operation">   </bean>  
<bean id="trackAspect" class="com.javatpoint.TrackOperation"></bean>          
<aop:config>  
  <aop:aspect id="myaspect" ref="trackAspect" >  
     <!-- @Before -->  
     <aop:pointcut id="pointCutBefore"   expression="execution(* com.javatpoint.Operation.*(..))" />  
     <aop:before method="myadvice" pointcut-ref="pointCutBefore" />  
  </aop:aspect>  
</aop:config>  
      
</beans>  
```