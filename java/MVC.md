# functions
A Spring MVC provides an elegant solution to use MVC in spring framework by the help of DispatcherServlet. Here, **DispatcherServlet** is a class that receives the incoming request and maps it to the right resource such as controllers, models, and views.
![Alt text](图片/image-7.png)
# components
- Model - A model contains the data of the application. A data can be a single object or a collection of objects.
- Controller - A controller contains the business logic of an application. Here, the @Controller annotation is used to mark the class as the controller.
- View - A view represents the provided information in a particular format. Generally, JSP+JSTL is used to create a view page. Although spring also supports other view technologies such as Apache Velocity, Thymeleaf and FreeMarker.
- Front Controller - In Spring Web MVC, the DispatcherServlet class works as the front controller. It is responsible to manage the flow of the Spring MVC application.
![Alt text](图片/image-8.png)
# advantages
1. Separate roles - The Spring MVC separates each role, where the model object, controller, command object, view resolver, DispatcherServlet, validator, etc. can be fulfilled by a specialized object.
2. Light-weight - It uses light-weight servlet container to develop and deploy your application.
3. Powerful Configuration - It provides a robust configuration for both framework and application classes that includes easy referencing across contexts, such as from web controllers to business objects and validators.
4. Rapid development - The Spring MVC facilitates fast and parallel development.
5. Reusable business code - Instead of creating new objects, it allows us to use the existing business objects.
6. Easy to test - In Spring, generally we create JavaBeans classes that enable you to inject test data using the setter methods.
7. Flexible Mapping - It provides the specific annotations that easily redirect the page.
MVC example
![Alt text](图片/image-9.png)
# model interface
|Method|Description|
|--|------|
|Model addAllAttributes(Collection<?> arg)|It adds all the attributes in the provided Collection into this Map.|
|Model addAllAttributes(Map<String,?> arg)|It adds all the attributes in the provided Map into this Map.|
|Model addAllAttribute(Object arg)|It adds the provided attribute to this Map using a generated name.|
|Model addAllAttribute(String arg0, Object arg1)|It binds the attribute with the provided name.|
|Map<String, Object> asMap()|It return the current set of model attributes as a Map.|
|Model mergeAttributes(Map< String,?> arg)|It adds all attributes in the provided Map into this Map, with existing objects of the same name taking precedence.|
|boolean containsAttribute(String arg)|It indicates whether this model contains an attribute of the given name|
# RequestParam Annotation
>[!function]read the form data and bind it automatically to the parameter present in the provided method
```java
@Controller  
public class HelloController {  
@RequestMapping("/hello")  
    //read the provided form data  
    public String display(@RequestParam("name") String name,@RequestParam("pass") String pass,Model m){  
        if(pass.equals("admin")){  
            String msg="Hello "+ name;  
            //add a message to the model  
            m.addAttribute("message", msg);  
            return "viewpage";  
        }  
        else  
        {  
            String msg="Sorry "+ name+". You entered an incorrect password";  
            m.addAttribute("message", msg);  
            return "errorpage";  
        }     
    }  
}  
```
# Form Tag Library(标注库)
```xml
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%> 
```

|Form Tag|Description|
|--|----|
|form:form|It is a container tag that contains all other form tags.|
|form:input|This tag is used to generate the text field.|
|form:radiobutton|This tag is used to generate the radio buttons.|
|form:checkbox|This tag is used to generate the checkboxes.|
|form:password|This tag is used to generate the password input field.|
|form:select|This tag is used to generate the drop-down list.|
|form:textarea|This tag is used to generate the multi-line text field.|
|form:hidden|This tag is used to generate the hidden input field.|
## input
```xml
<form:input type=?email? path="email" />  
<form:input type=?date? path="date" /> 
``` 
## radiobutton
```xml
<body>  
    <form:form action="submitForm" modelAttribute="reservation">  
        First name: <form:input path="firstName" />         
        <br><br>  
        Last name: <form:input path="lastName" />  
        <br><br>  
        Gender:   
        Male <form:radiobutton path="Gender" value="Male"/>  
        Female <form:radiobutton path="Gender" value="Female"/>  
        <br><br>  
        <input type="submit" value="Submit" />  
    </form:form>  
</body>
```
## checkbox
```xml
  Meals:  
        BreakFast<form:checkbox path="Food" value="BreakFast"/>  
        Lunch<form:checkbox path="Food" value="Lunch"/>  
        Dinner<form:checkbox path="Food" value="Dinner"/>
```
## drop down list
```xml
<body>  
    <form:form action="submitForm" modelAttribute="reservation">  
        Leaving from: <form:select path="cityFrom">  
        <form:option value="Ghaziabad" label="Ghaziabad"/>  
        <form:option value="Modinagar" label="Modinagar"/>  
        <form:option value="Meerut" label="Meerut"/>  
        <form:option value="Amristar" label="Amristar"/>  
        </form:select>  
        <br><br>  
        Going to: <form:select path="cityTo">  
        <form:option value="Ghaziabad" label="Ghaziabad"/>  
        <form:option value="Modinagar" label="Modinagar"/>  
        <form:option value="Meerut" label="Meerut"/>  
        <form:option value="Amristar" label="Amristar"/>  
        </form:select>  
        <br><br>  
        <input type="submit" value="Submit" />  
    </form:form>  
</body>  
```
# Spring MVC CRUD Example
