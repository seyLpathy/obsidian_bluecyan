# feature
1. 授权及确认用户身份
2. 对用户进行访问管控
3. 在任何环境下实现会话API
4. 在授权/访问控制/会话生命周期对事件进行反馈
5. 汇总一个或多个用户安全数据源并以“视图”方式呈现
6. 支持single sign on 功能
![[Pasted image 20231115165259.png]]

# High-Level Overview
![Alt text](图片/image-14.png)
# architecture
* Subject 主体
* SecurityManager 安全管理
* implementations
* Authentication
* Authorization
* Session Management
* Cache Management
* Realm coordination
* Event propagation
* "Remember Me" Services
* Subject creation
* Logout and more.
![Alt text](图片/image-15.png)
# configuration
## INI Configuration
配置文件前缀读取：file:, classpath:, or url:
### SecurityManager from an INI resource
```java
Factory<SecurityManager> factory = new IniSecurityManagerFactory("classpath:shiro.ini");
SecurityManager securityManager = factory.getInstance();
SecurityUtils.setSecurityManager(securityManager);
```
### SecurityManager from an INI instance
```java
Ini ini = new Ini();
//populate the Ini instance as necessary
Factory<SecurityManager> factory = new IniSecurityManagerFactory(ini);
SecurityManager securityManager = factory.getInstance();
SecurityUtils.setSecurityManager(securityManager);
```
## ini配置基础
### **main**
配置安全管理实例及其依赖，领域等
1. 定义对象及设置对象属性
```ini
[main]
sha256Matcher = org.apache.shiro.authc.credential.Sha256CredentialsMatcher

myRealm = com.company.security.shiro.DatabaseRealm
myRealm.connectionTimeout = 30000
myRealm.username = jsmith
myRealm.password = secret
myRealm.credentialsMatcher = $sha256Matcher
securityManager.sessionManager.globalSessionTimeout = 1800000
securityManager.rememberMeManager.cipherKey = kPH+bIxk5D2deZiIxcaaaA==
securityManager.sessionManager.sessionListeners = $sessionListener1, $sessionListener2
```
### **user**
```ini
[users]
admin = secret
lonestarr = vespa, goodguy, schwartz
darkhelmet = ludicrousspeed, badguy, schwartz
#格式要求
username = password, roleName1, roleName2, …, roleNameN
#加密密码
user1 = 2bb80d537b1da3e38bd30361aa855686bde0eacd7162fef6a25fe97bf527a25b, role1, role2, ...
```
### **roles**
```ini
[roles]
# 'admin' role has all permissions, indicated by the wildcard '*'
admin = *
# The 'schwartz' role can do anything (*) with any lightsaber:
schwartz = lightsaber:*
# The 'goodguy' role is allowed to 'drive' (action) the winnebago (type) with
# license plate 'eagle5' (instance specific id)
goodguy = winnebago:drive:eagle5
```
### 顺次问题
1. 覆盖特性
2. securitymanager实例默认自动生成


# authentication(确认身份)
## core elements
subject's _unique primary principal_ and **credentials**
## process 
### collect primary principal and credentials
```java
//Example using most common scenario of username/password pair:
UsernamePasswordToken token = new UsernamePasswordToken(username, password);
//"Remember Me" built-in:
token.setRememberMe(true);
```
### Submit the principals and credentials
```java
Subject currentUser = SecurityUtils.getSubject();
currentUser.login(token);
```
### Handling Success or Failure
```java
try {
    currentUser.login(token);
} catch ( UnknownAccountException uae ) { ...
} catch ( IncorrectCredentialsException ice ) { ...
} catch ( LockedAccountException lae ) { ...
} catch ( ExcessiveAttemptsException eae ) { ...
} ... catch your own ...
} catch ( AuthenticationException ae ) {
    //unexpected error?
}
//No problems, continue on as expected...
```
### logging out 
```java
currentUser.logout();
```
|properties|remembered|authenticated|
|---|------|------|
|identity|known from last sessions|known from current sessions|
|isremembered()|true|false|
![Alt text](图片/image-16.png)
# authorization（授权）
## permission
 permission statements at a minimum are based on Resources and Actions
## roles
A Role is a named entity that typically represents a set of behaviors or responsibilities.
## user
 the Subject is really Shiro’s 'User' concept.
# reaml
A Realm is essentially a security-specific DAO.
## Realm Configuration
显示声明
```ini
fooRealm = com.company.foo.Realm
barRealm = com.company.another.Realm
bazRealm = com.company.baz.Realm
securityManager.realms = $fooRealm, $barRealm, $bazRealm
```
## Realm Authentication
### Supporting AuthenticationTokens
before a Realm is consulted to perform an authentication attempt, its supports method is called. If the return value is true, only then will its getAuthenticationInfo(token) method be invoked.
### Handling supported AuthenticationTokens
1. Inspects the token for the identifying principal (account identifying information)
2. Based on the principal, looks up corresponding account data in the data source
3. Ensures that the token’s supplied credentials matches those stored in the data store
   
4. If the credentials match, an AuthenticationInfo instance is returned that encapsulates the account data in a format Shiro understands

5. If the credentials DO NOT match, an AuthenticationException is thrown
## Credentials Matching
```java
Realm myRealm = new com.company.shiro.realm.MyRealm();
CredentialsMatcher customMatcher = new com.company.shiro.realm.CustomCredentialsMatcher();
myRealm.setCredentialsMatcher(customMatcher);
```
### Hashing Credentials
 HashedCredentialsMatcher implementations
### Hashing and Corresponding Matchers
```ini
credentialsMatcher = org.apache.shiro.authc.credential.Sha256CredentialsMatcher
# base64 encoding, not hex in this example:
credentialsMatcher.storedCredentialsHexEncoded = false
credentialsMatcher.hashIterations = 1024
# This next property is only needed in Shiro 1.0\.  Remove it in 1.1 and later:
credentialsMatcher.hashSalted = true
```
# Realm Authorization
SecurityManager delegates the task of Permission or Role checking to Authorizer, defaulted to ModularRealmAuthorizer.
## Role based Authorization
1. Subject delegates to SecurityManager for identifying if the given Role is assigned

2. SecurityManager then delegates to Authorizer

3. Authorizer then referrers to all the Authorizing Realms one by one until it found given role assigned to the subject. Deny access by returning false if no none of the Realm grants Subject given Role

4. Authorizing Realm AuthorizationInfo getRoles() method to get all Roles assigned to Subject

5. Grant access if it found the given Role in list of roles returned from AuthorizationInfo.getRoles call.
## Permission based Authorization
1. Subject delegates the task to grant or deny Permission to SecurityManager

2. SecurityManager then delegates to Authorizer

3. Authorizer then referrers to all the Authorizer Realms one by one until it Permission is granted If Permission is not granted by any of the Authorizing Realm, Subject is denied Permission

4. Authorizing Realm does the following in order to check if a Subject is permitted:

	1. First it gets identify all Permissions assigned to Subject directly by calling getObjectPermissions() and getStringPermissions methods on AuthorizationInfo and aggregating the results.

	2. If a RolePermissionResolver is registered, it is used to retrieve Permissions based on all the roles assigned to Subject by calling the RolePermissionResolver.resolvePermissionsInRole()

	3. For aggregated Permissions from a. and b. the implies() method is called to check if any of these permission are implied the checked permission. See WildcardPermission
# session（对话）
```java
ubject currentUser = SecurityUtils.getSubject();
Session session = currentUser.getSession();
session.setAttribute( "someKey", someValue);
```
## The SessionManager
```ini
[main]
...
sessionManager = com.foo.my.SessionManagerImplementation
securityManager.sessionManager = $sessionManager
# customize sessionmanager regulated by securitymanager
securityManager.sessionManager.globalSessionTimeout = 3600000
# session time out 
securityManager.sessionManager.sessionListeners = $aSessionListener, $anotherSessionListener, etc.
```
# JSP
```jsp
<%@ taglib prefix="shiro" uri="https://shiro.apache.org/tags" %>
<!-- declaration -->
<shiro:guest>
    Hi there!  Please <a href="login.jsp">Login</a> or <a href="signup.jsp">Signup</a> today!
</shiro:guest>
<!-- the logical counter of user -->
<shiro:user>
    Welcome back John!  Not John? Click <a href="login.jsp">here<a> to login.
</shiro:user>
<!-- defined the wrapped content as user -->
<shiro:authenticated>
    <a href="updateAccount.jsp">Update your contact information</a>.
</shiro:authenticated>
<!-- authenticated -->
Hello, <shiro:principal/>, how are you today?
<!-- principal display -->
Hello, <shiro:principal property="firstName"/>, how are you today?
<!-- principal properties -->
now
```
# Java Annotation List
* RequiresAuthentication - Requires the current Subject to have been authenticated during their current session for the annotated class/instance/method to be accessed or invoked

* RequiresGuest - Requires the current Subject to be a "guest", that is, they are not authenticated or remembered from a previous session for the annotated class/instance/method to be accessed or invoked.

* RequiresPermissions - Requires the current executor’s Subject to imply a particular permission in order to execute the annotated method. If the executor’s associated Subject determines that the executor does not imply the specified permission, the method will not be executed.

* RequiresRoles - Requires the currently executing Subject to have all the specified roles. If they do not have the role(s), the method will not be executed and an AuthorizationException is thrown.

* RequiresUser - Requires the current Subject to be an application user for the annotated class/instance/method to be accessed or invoked.



