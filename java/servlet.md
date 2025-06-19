# application
- _**Read the explicit data sent by the clients (browsers).**_ This includes an HTML form on a Web page or it could also come from an applet or a custom HTTP client program.
- _**Read the implicit HTTP request data sent by the clients (browsers).**_ This includes cookies, media types and compression schemes the browser understands, and so forth.
- _**Process the data and generate the results. This process may require talking to a database, executing an RMI or CORBA call**_, invoking a Web service, or computing the response directly.
- _**Send the explicit data (i.e., the document) to the clients (browsers).**_ This document can be sent in a variety of formats, including text (HTML or XML), binary (GIF images), Excel, etc.
- _**Send the implicit HTTP response to the clients (browsers).**_ This includes telling the browsers or other clients what type of document is being returned (e.g., HTML), setting cookies and caching parameters, and other such tasks.
# architecture
![Alt text](JavaScript/image-4.png)
- First the HTTP requests coming to the server are delegated to the servlet container.

- The servlet container loads the servlet before invoking the service() method.

- Then the servlet container handles multiple requests by spawning multiple threads, each thread executing the service() method of a single instance of the servlet.
# Servlets Packages
 **javax.servlet and javax.servlet.http packages**
# life cycle
![Alt text](JavaScript/image-5.png)
## initialized by calling the init() method.
```java
// 服务器启动或者用户初次访问网址进行初始化
public void init() throws ServletException {
   // Initialization code...
}
```
## calls service() method to process a client's request.
```java
// 处理用户端的请求
// checks the HTTP request type (GET, POST, PUT, DELETE, etc.) and calls doGet, doPost, doPut, doDelete, etc.
public void service(ServletRequest request, ServletResponse response) 
   throws ServletException, IOException {
}

public void doGet(HttpServletRequest request, HttpServletResponse response)
   throws ServletException, IOException {
   // Servlet code
}

public void doPost(HttpServletRequest request, HttpServletResponse response)
   throws ServletException, IOException {
   // Servlet code
}
```
## terminated by calling the destroy() method.
```java
public void destroy() {
   // Finalization code...
}
```
## servlet is garbage collected by the garbage collector of the JVM.
# implementation of servlet
## creation
- implementing Servlet interface,
- inheriting GenericServlet class
- inheriting HttpServlet class