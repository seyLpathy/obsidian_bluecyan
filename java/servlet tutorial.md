>[!questions]
    - What is the web application and what is the difference between Get and Post request?
    - What information is received by the web server if we request for a Servlet?
    - How to run servlet in Eclipse, MyEclipse and Netbeans IDE?
    - What are the ways for servlet collaboration and what is the difference between RequestDispatcher and sendRedirect() method?
    - What is the difference between ServletConfig and ServletContext interface?
    - How many ways can we maintain the state of a user? Which approach is mostly used in web development?
    - How to count the total number of visitors and whole response time for a request using Filter?
    - How to run servlet with annotation?
    - How to create registration form using Servlet and Oracle database?
    - How can we upload and download the file from the server?
# definition
- Servlet is a technology which is used to create a web application.
- ervlet is an API that provides many interfaces and classes including documentation.
- Servlet is an interface that must be implemented for creating any Servlet.
- Servlet is a class that extends the capabilities of the servers and responds to the incoming requests . It can respond to any requests.
- Servlet is a web component that is deployed on the server to create a dynamic web page.
![[Pasted image 20231017210640.png]]
# advantage
- Better performance: because it creates a thread for each request, not process.
- Portability: because it uses Java language.
- Robust: JVM manages Servlets, so we don't need to worry about the memory leak, garbage collection, etc.
- Secure: because it uses java language.
# website
Website is a collection of related web pages that may contain text, images, audio and video. The first page of a website is called home page. Each website has specific internet address (URL) that you need to enter in your browser to access a website.
## static website
静态网页的内容固定
## dynamic website
- 从数据库或者内容管理系统(CMS)获取内容
- 客户端脚本基于用户输入生成内容及服务端脚本进行

|HTTP Request|Description|
|--|----|
|GET|Asks to get the resource at the requested URL.|
|POST|Asks the server to accept the body info attached. It is like GET request with extra info sent with the request.|
|HEAD|Asks for only the header part of whatever a GET would return. Just like GET but with no body.|
|TRACE|Asks for the loopback of the request message, for testing or troubleshooting.|
|PUT|Says to put the enclosed info (the body) at the requested URL.|
|DELETE|Says to delete the resource at the requested URL.|
|OPTIONS|Asks for a list of the HTTP methods to which the thing at the request URL can respond|
![[Pasted image 20231017212244.png]]
# Servlet Container
- Standalone: It is typical Java-based servers in which the servlet container and the web servers are the integral part of a single program. For example:- Tomcat running by itself
- In-process: It is separated from the web server, because a different program runs within the address space of the main server as a plug-in. For example:- Tomcat running inside the JBoss.
- Out-of-process: The web server and servlet container are different programs which are run in a different process. For performing the communications between them, web server uses the plug-in provided by the servlet contain
# 容器操作
- Life Cycle Management
- Multithreaded support
- Object Pooling
- Security etc.
# Server: Web vs. Application
1. web server 
![[Pasted image 20231017213114.png]]
3. Application server
![[Pasted image 20231017213150.png]]
# Servlet API
## javax.selvlet

|Class Name|Description|
|--|----|
|GenericServlet|To define a generic and protocol-independent servlet.|
|ServletContextAttributeEvent|To generate notifications about changes to the attributes of the servlet context of a web application.|
|ServletContextEvent|To generate notifications about changes to the servlet context of a web application.|
|ServletInputStream|This class provides an input stream to read binary data from a client request.|
|ServletOutputStream|This class provides an output stream for sending binary data to the client.|
|ServletRequestAttributeEvent|To generate notifications about changes to the attributes of the servlet request in an application.|
|ServletRequestEvent|To indicate lifecycle events for a ServletRequest.|
|ServletRequestWrapper|This class provides the implementation of the ServletRequest interface that can be subclassed by developers to adapt the request to a Servlet.|
|ServletResponseWrapper|This class provides the implementation of the ServletResponse interface that can be subclassed by developers to adapt the response from a Servlet.|
### interface
- **Servlet**
- **ServletRequest**
  
|Method|Description|
|--|----|
|public String getParameter(String name)|is used to obtain the value of a parameter by name.|
|public String[] getParameterValues(String name)|returns an array of String containing all values of given parameter name.It is mainly used to obtain values of a Multi select list box.|
|java.util.Enumeration|getParameterNames()	returns an enumeration of all of the request parameter names.|
|public int getContentLength()|Returns the size of the request entity data, or -1 if not known.|
|public String getCharacterEncoding()|Returns the character set encoding for the input of this request.|
|public String getContentType()|Returns the Internet Media Type of the request entity data, or null if not known.|
|public ServletInputStream getInputStream() throws IOException|	Returns an input stream for reading binary data in the request body.|
|public abstract String getServerName()|Returns the host name of the server that received the request.|
|public int getServerPort()|Returns the port number on which this request was received.|
- ServletResponse
- RequestDispatcher
- ServletConfig
- ServletContext
- SingleThreadModel
- Filter
- FilterConfig
- FilterChain
- ServletRequestListener
- ServletRequestAttributeListener
- ServletContextListener
- ServletContextAttributeListener
### classes
- **GenericServlet**
```java
public abstract class GenericServlet 
extends java.lang.Object 
implements Servlet, ServletConfig, java.io.Serializable

public void init(ServletConfig config) //is used to initialize the servlet.

public abstract void service(ServletRequest request, ServletResponse response) //provides service for the incoming request. It is invoked at each time when user requests for a servlet.

public void destroy() //is invoked only once throughout the life cycle and indicates that servlet is being destroyed.

public ServletConfig getServletConfig() //returns the object of ServletConfig.

public String getServletInfo() //returns information about servlet such as writer, copyright, version etc.

public void init() //it is a convenient method for the servlet programmers, now there is no need to call super.init(config)

public ServletContext getServletContext() //returns the object of ServletContext.

public String getInitParameter(String name) //returns the parameter value for the given parameter name.

public Enumeration getInitParameterNames() //returns all the parameters defined in the web.xml file.

public String getServletName() //returns the name of the servlet object.

public void log(String msg) //writes the given message in the servlet log file.

public void log(String msg,Throwable t) //writes the explanatory message in the servlet log file and a stack trace.
```
- ServletInputStream
- ServletOutputStream
- ServletRequestWrapper
- ServletResponseWrapper
- ServletRequestEvent
- ServletContextEvent
- ServletRequestAttributeEvent
- ServletContextAttributeEvent
- ServletException
- UnavailableException
## javax.servlet.http
### interface
- HttpServletRequest
- HttpServletResponse
- HttpSession
- HttpSessionListener
- HttpSessionAttributeListener
- HttpSessionBindingListener
- HttpSessionActivationListener
### classes
- **HttpServlet**
```java
public abstract class HttpServlet 
extends GenericServlet 
implements java.io.Serializable

public void service(ServletRequest req,ServletResponse res) //dispatches the request to the protected service method by converting the request and response object into http type.

protected void service(HttpServletRequest req, HttpServletResponse res) //receives the request from the service method, and dispatches the request to the doXXX() method depending on the incoming http request type.

protected void doGet(HttpServletRequest req, HttpServletResponse res) //handles the GET request. It is invoked by the web container.

protected void doPost(HttpServletRequest req, HttpServletResponse res) //handles the POST request. It is invoked by the web container.

protected void doHead(HttpServletRequest req, HttpServletResponse res) //handles the HEAD request. It is invoked by the web container.

protected void doOptions(HttpServletRequest req, HttpServletResponse res) //handles the OPTIONS request. It is invoked by the web container.

protected void doPut(HttpServletRequest req, HttpServletResponse res) //handles the PUT request. It is invoked by the web container.

protected void doTrace(HttpServletRequest req, HttpServletResponse res) //handles the TRACE request. It is invoked by the web container.

protected void doDelete(HttpServletRequest req, HttpServletResponse res) //handles the DELETE request. It is invoked by the web container.

protected long getLastModified(HttpServletRequest req) //returns the time when HttpServletRequest was last modified since midnight January 1, 1970 GMT.
```
- Cookie
- HttpServletRequestWrapper
- HttpServletResponseWrapper
- HttpSessionEvent
- HttpSessionBindingEvent
![[Pasted image 20231018150306.png]]
# servlet的生命周期
## 加载servlet类
## 创建servlet实例
## 触发init()
```java
public void init(ServletConfig config) throws ServletException  
```
## 触发service()
```java
public void service(ServletRequest request, ServletResponse response)   
  throws ServletException, IOException  
```
## 触发destroy()
```java
public void destroy()  
```
# create a serlet for tomcat
1. **create directory structure**
2. **create a servlet**
   1. extends httpservlet class
   2. implements servlet interface
   3. extends abstract genericservlet class
```java
import javax.servlet.http.*;  
import javax.servlet.*;  
import java.io.*;  
public class DemoServlet extends HttpServlet{  
public void doGet(HttpServletRequest req,HttpServletResponse res)  
throws ServletException,IOException  
{  
res.setContentType("text/html");//setting the content type  
PrintWriter pw=res.getWriter();//get the stream to write the data  
  
//writing html in the stream  
pw.println("<html><body>");  
pw.println("Welcome to servlet");  
pw.println("</body></html>");  
  
pw.close();//closing the stream  
}}  
```
3. **compile servlet**

|Jar file|Server|
|--|---|
|servlet-api.jar|Apache Tomcat|
|weblogic.jar|Weblogic|
|javaee.jar|Glassfish|
|javaee.jar|JBoss|
4. **create web.xml**
```xml
<web-app>  
  
<servlet>  
<servlet-name>sonoojaiswal</servlet-name>  
<servlet-class>DemoServlet</servlet-class>  
</servlet>  
  
<servlet-mapping>  
<servlet-name>sonoojaiswal</servlet-name>  
<url-pattern>/welcome</url-pattern>  
</servlet-mapping>  
  
</web-app>  
```
5. 启动服务器并进行部署
6. 访问servlet页面
# war包
jar -cvf name.war *  -压缩
# welcome-file-list in web.xml
![[Pasted image 20231018153820.png]]
```xml
<web-app>  
 ....  
  
  <welcome-file-list>  
   <welcome-file>home.html</welcome-file>  
   <welcome-file>default.html</welcome-file>  
  </welcome-file-list>  
</web-app>  
```

