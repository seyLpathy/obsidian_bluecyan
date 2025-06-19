# adavantage
## extension of servlet
JSP technology is the extension to Servlet technology. We can use all the features of the Servlet in JSP. In addition [[#JSP Implicit Objects(内置对象)|内置对象]], predefined tags, expression language and Custom tags== in JSP, that makes JSP development easy.
## Easy to maintain
 separate our business logic with presentation logic. In Servlet technology
## Fast Development: No need to recompile and redeploy
If JSP page is modified, we don't need to recompile and redeploy the project. The Servlet code needs to be updated and recompiled if we have to change the look and feel of the application.
## Less code than Servlet
# The Lifecycle of a JSP Page
- Translation of JSP Page
- Compilation of JSP Page
- Classloading (the classloader loads class file)
- Instantiation (Object of the Generated Servlet is created).
- Initialization ( the container invokes jspInit() method).
- Request processing ( the container invokes jspService() method).
- Destroy ( the container invokes jspDestroy() method).
![[Pasted image 20231017182249.png]]
## The Directory structure of JSP
![[Pasted image 20231017182740.png]]
# JSP API
## javax.servlet.jsp package
###  interface
1. JspPage
 **public void jspInit():** It is invoked only once during the life cycle of the JSP when JSP page is requested firstly. It is used to perform initialization. It is same as the init() method of Servlet interface.
**public void jspDestroy():** It is invoked only once during the life cycle of the JSP before the JSP page is destroyed. It can be used to perform some clean up operation.
3. HttpJspPage
4. ![[Pasted image 20231017183429.png]]
public void \_jspService(): It is invoked each time when request for the JSP page comes to the container. It is used to process the request. cannot override this method.
### classes
- JspWriter
- PageContext
- JspFactory
- JspEngineInfo
- JspException
- JspError
# JSP Scriptlet tag(java code)
##  JSP scriptlet tag
<%  java source code %>
## JSP expression tag
1. <%=  statement %>
```html
<html>  
<body>  
<form action="welcome.jsp">  
<input type="text" name="uname"><br/>  
<input type="submit" value="go">  
</form>  
</body>  
</html>
```

``` html
<html>  
<body>  
<%= "Welcome "+request.getParameter("uname") %>  
</body>  
</html>
```
## JSP declaration Tag
The **JSP declaration tag** is used _to declare fields and methods_.placed outside the service() method of auto generated servlet.
<%!  field or method declaration %>
```html
<html>  
<body>  
<%!   
int cube(int n){  
return n*n*n*;  
}  
%>  
<%= "Cube of 3 is:"+cube(3) %>  
</body>  
</html>
```
# JSP Implicit Objects(内置对象)
|Object|Type|definition|
|---|---|------|
|out|JspWriter|输出到HTML|
|request|HttpServletRequest|获取用户信息|
|response|HttpServletResponse|响应客户端请求|
|config|ServletConfig|这是一个 Servlet 配置对象，用于 Servlet 和页面的初始化参数|
|application|ServletContext|所有用户共享信息|
|session|HttpSession|用来保存用户信息|
|pageContext|jsp.PageContext|JSP 的页面容器，用于访问 page、request、application 和 session 的属性|
|page|jsp.HttpJspPage|类似于 Java 类的 this 关键字，表示当前 JSP 页面|
|exception|Throwable|异常|
- 由 JSP 规范提供，不用编写者实例化；
- 通过 Web 容器实现和管理；
- 所有 JSP 页面均可使用；
- 只有在脚本元素的表达式或代码段中才能使用。
### out example
```html
<html>  
<body>  
<% out.print("Today is:"+java.util.Calendar.getInstance().getTime()); %>  
</body>  
</html>
```
### request example
```html
<form action="welcome.jsp">  
<input type="text" name="uname">  
<input type="submit" value="go"><br/>  
</form>  

welcome.jsp

<%   
String name=request.getParameter("uname");  
out.print("welcome "+name);  
%>
```
### response example
```html
**index.html**

<form action="welcome.jsp">  
<input type="text" name="uname">  
<input type="submit" value="go"><br/>  
</form>  

**welcome.jsp**
<%   
response.sendRedirect("http://www.google.com");  
%>
```
### config example 
```html

index.html
<form action="welcome">  
<input type="text" name="uname">  
<input type="submit" value="go"><br/>  
</form>  

web.xml file
<web-app>  

<servlet>  
<servlet-name>sonoojaiswal</servlet-name>  
<jsp-file>/welcome.jsp</jsp-file>  
<init-param>  
<param-name>dname</param-name>  
<param-value>sun.jdbc.odbc.JdbcOdbcDriver</param-value>  
</init-param>  
</servlet>  
  
<servlet-mapping>  
<servlet-name>sonoojaiswal</servlet-name>  
<url-pattern>/welcome</url-pattern>  
</servlet-mapping>  
</web-app>  

welcome.jsp
<%   
out.print("Welcome "+request.getParameter("uname"));  
String driver=config.getInitParameter("dname");  
out.print("driver name is="+driver);  
%>  
```
### JSP application implicit object
作用与config有点类似，但只在部署的时候执行一次
### # session implicit object
```html

index.html
<html>  
<body>  
<form action="welcome.jsp">  
<input type="text" name="uname">  
<input type="submit" value="go"><br/>  
</form>  
</body>  
</html>  

welcome.jsp

<html>  
<body>  
<%   
String name=request.getParameter("uname");  
out.print("Welcome "+name);  
session.setAttribute("user",name);  
<a href="second.jsp">second jsp page</a>  
%>  
</body>  
</html>  
second.jsp

<html>  
<body>  
<%   
String name=(String)session.getAttribute("user");  
out.print("Hello "+name);  
%>  
</body>  
</html>  
```

### pageContext implicit object
```html
The pageContext object can be used to set,get or remove attribute from one of the following scopes:
- page
- request
- session
- application

index.html
<html>  
<body>  
<form action="welcome.jsp">  
<input type="text" name="uname">  
<input type="submit" value="go"><br/>  
</form>  
</body>  
</html>  

welcome.jsp

<html>  
<body>  
<%   
String name=request.getParameter("uname");  
out.print("Welcome "+name);  
pageContext.setAttribute("user",name,PageContext.SESSION_SCOPE);  
<a href="second.jsp">second jsp page</a>  
%>  
</body>  
</html>  

second.jsp

<html>  
<body>  
<%   
String name=(String)pageContext.getAttribute("user",PageContext.SESSION_SCOPE);  
out.print("Hello "+name);  
%>  
</body>  
</html>  
```
### page implicit object
Object page=this;
For using this object it must be cast to Servlet type.For example:
<% (HttpServlet)page.log("message"); %>
Since, it is of type Object it is less used because you can use this object directly in jsp.For example:
<% this.log("message"); %>
### exception implicit object
In JSP, exception is an implicit object of type java.lang.Throwable class. This object can be used to print the exception.
# JSP指令
## page directive
\<%@ page attribute="value" %> 表明属性应用于全体页面
### Attributes of JSP page directive
- import(引入模块)
- contentType(defines the MIME(Multipurpose Internet Mail Extension) type of the HTTP response)
- extends(继承)
- info -sets the information of the JSP page which is retrieved by using getServletInfo()
- buffer -(buffer size in kilobytes to handle output)
- language (specifies the scripting language used in the JSP page)
- isELIgnored (统一表达式语言)
- isThreadSafe(是否支持多线程)
- autoFlush
- session
- pageEncoding（编码）
- errorPage（错误页面）
- isErrorPage（错误页面申明）
### include directive
\<%@ include file="resourceName" %> 包含其他文件
### taglib directive(定义tag)
\<%@ taglib uri="uriofthetaglibrary" prefix="prefixoftaglibrary" %>
# JSP异常处理
- By **errorPage** and **isErrorPage** attributes of page directive
- By **<error-page>** element in web.xml file

# JSP action tags
|JSP Action Tags|Description|
|---|---|
|jsp:forward|forwards the request and response to another resource.|
|jsp:include|includes another resource.|
|jsp:useBean|creates or locates bean object.|
|jsp:setProperty|sets the value of property in bean object.|
|jsp:getProperty|prints the value of property of the bean.|
|jsp:plugin|embeds another components such as applet.|
|jsp:param|sets the parameter value. It is used in forward and include mostly.|
|jsp:fallback|can be used to print the message if plugin is working. It is used in jsp:plugin.|
1. ##　forward:将请求引导至其他的资源，过程中可附带参数设置　##
```html
ndex.jsp
<html>  
<body>  
<h2>this is index page</h2>  
<jsp:forward page="printdate.jsp" >  
<jsp:param name="name" value="javatpoint.com" />  
</jsp:forward>  
</body>  
</html>  

printdate.jsp
<html>  
<body>  
<% out.print("Today is:"+java.util.Calendar.getInstance().getTime()); %>  
<%= request.getParameter("name") %>  
</body>  
</html>  
```
2. ## include：仅在请求时包含特定其他资源，一般用于动态网页　##

|JSP include directive|JSP include action|
|---|---|
|includes resource at translation time.|includes resource at request time.|
|better for static pages.|better for dynamic pages.|
includes the original content in the generated servlet.|calls the include method.|

```html
index.jsp
<h2>this is index page</h2>  
<jsp:include page="printdate.jsp" />  
<h2>end section of index page</h2>  

printdate.jsp
<% out.print("Today is:"+java.util.Calendar.getInstance().getTime()); %>  
```

3. ## useBean action tag ##
id: bean的识别号
scope: 指定应用域page/request/session/application，默认应用域page.
class: 初始化特定的类，该类不能是抽象类同时必须拥有无参构造器
type: 指定bean的类型
beanName: java.beans.Beans.instantiate() 指定类名
```html
Calculator.java 
package com.javatpoint;  
public class Calculator{  
public int cube(int n){return n*n*n;}  
}  

index.jsp file
<jsp:useBean id="obj" class="com.javatpoint.Calculator"/>  
<%  
int m=obj.cube(5);  
out.print("cube of 5 is "+m);  
%>  
```
4. ## setProperty action tags/getProperty action tags##
```html
index.html
<form action="process.jsp" method="post">  
Name:<input type="text" name="name"><br>  
Password:<input type="password" name="password"><br>  
Email:<input type="text" name="email"><br>  
<input type="submit" value="register">  
</form>  

process.jsp
<jsp:useBean id="u" class="org.sssit.User"></jsp:useBean>  
<jsp:setProperty property="*" name="u"/>  
Record:<br>  
<jsp:getProperty property="name" name="u"/><br>  
<jsp:getProperty property="password" name="u"/><br>  
<jsp:getProperty property="email" name="u" /><br>  

User.java
package org.sssit;  
public class User {  
private String name,password,email;  
//setters and getters  
}  
```
5. ## plugin action tag ##
将applet或者bean镶嵌至jsp中
# EL in jsp
|pageScope|it maps the given attribute name with the value set in the page scope|
|--|-----|
|requestScope|it maps the given attribute name with the value set in the request scope|
|sessionScope|it maps the given attribute name with the value set in the session scope|
|applicationScope|it maps the given attribute name with the value set in the application scope|
|param|it maps the request parameter to the single value|
|paramValues|it maps the request parameter to an array of values|
|header|it maps the request header name to the single value|
|headerValues|it maps the request header name to an array of values|
|cookie|it maps the given cookie name to the cookie value|
|initParam|it maps the initialization parameter|
|pageContext|it provides access to many objects request, session etc.|
# MVC IN jsp
- model:bean
- controller:servlet
- view:JSP 




