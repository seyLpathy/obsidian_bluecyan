>[!feature]Spring Boot is a Spring module that provides the RAD (Rapid Application Development) feature to the Spring framework.
![Alt text](图片/image-10.png)
# sister projects
- Spring Data: It simplifies data access from the relational and NoSQL databases.
- Spring Batch: It provides powerful batch processing.
- Spring Security: It is a security framework that provides robust security to applications.
- Spring Social: It supports integration with social networking like LinkedIn.
- Spring Integration: It is an implementation of Enterprise Integration Patterns. It facilitates integration with other enterprise applications using lightweight messaging and declarative adapters.
# Goals of Spring Boot
1. Provides Opinionated Development approach
2. Avoids defining more Annotation Configuration
3. Avoids writing lots of import statements
4. Avoids XML Configuration.
# structures and classes
## SpringApplication
```java
public static void main(String[] args)  
{    
SpringApplication.run(ClassName.class, args);    
}  
```
## Application Events and Listeners
1. uses events to handle the variety of tasks
2. Always create factories file in META-INF folder like META-INF/spring.factories.
## Admin Support
>[!job]It is used to access and manage applications remotely. We can enable it in the Spring Boot application by using spring.application.admin.enabled property.
## Externalized Configuration
The application uses YAML files to externalize configuration
## Properties Files
Spring Boot provides a rich set of Application Properties.The properties file is used to set properties like server-port =8082 and many others. It helps to organize application properties.
## YAML Support
It provides a convenient way of specifying the hierarchical configuration. It is a superset of JSON. The SpringApplication class automatically supports YAML. It is an alternative of properties file.
## Type-safe Configuration
The strong type-safe configuration is provided to govern and validate the configuration of the application. Application configuration is always a crucial task which should be type-safe. We can also use annotation provided by this library.
## Logging
Spring Boot uses Common logging for all internal logging. Logging dependencies are managed by default. We should not change logging dependencies if no customization is needed.
## Security
Spring Boot applications are spring bases web applications. So, it is secure by default with basic authentication on all HTTP endpoints. A rich set of Endpoints is available to develop a secure Spring Boot application.
# Architecture
![Alt text](图片/image-11.png)
- **Presentation Layer:** The presentation layer handles the HTTP requests, translates the JSON parameter to object, and authenticates the request and transfer it to the business layer. In short, it consists of views i.e., frontend part
- **Business Layer**: The business layer handles all the business logic. It consists of service classes and uses services provided by data access layers. It also performs authorization and validation.

- **Persistence Layer**: The persistence layer contains all the storage logic and translates business objects from and to database rows.

- **Database Layer**: In the database layer, CRUD (create, retrieve, update, delete) operations are performed.
![Alt text](图片/image-13.png)
# Spring Boot Annotations
## Core Spring Framework Annotations
- **@Required: It applies to the bean setter method.**
```java
@Required  
public void setCost(Integer cost)   
{this.cost = cost;}  
```
- **@Autowired: Spring provides annotation-based auto-wiring**
```java
@Autowired  
public Customer(Person person)   
{this.person=person;}  
```
- @Configuration class annotated with @Configuration used by Spring Containers as a source of bean definitions
```java
@ComponentScan(basePackages = "com.javatpoint") 
@Configuration  
public class Vehicle{  
@BeanVehicle engine(){  
return new Vehicle();  }  
} 
```
- **@Bean It tells the method to produce a bean to be managed by Spring Container.**
```java
@Bean  
public BeanExample beanExample(){
	return new BeanExample();}  
```
- **@component It is used to mark a Java class as a bean.**
```java
@Component  
public class Student{}  
```
- **@Service: It is also used at class level. It tells the Spring that class contains the business logic**
```java
package com.javatpoint;  
@Service  
public class TestService{  
	public void service1(){ }  
}  
```
- **@Repository: It is a class-level annotation. The repository is a DAOs that access the database directly. The repository does all the operations related to the database.**
```java
package com.javatpoint;  
@Repository   
public class TestRepository{  
	public void delete(){ }  
}  
```
@