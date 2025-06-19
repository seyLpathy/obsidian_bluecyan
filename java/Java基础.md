# I/O 
![[Pasted image 20230922200509.png]]
![[Pasted image 20230922200534.png]]
![[Pasted image 20230922201030.png]]
字节流（bytestream):  FileInputStream and the FileOutputStream
字符流（characterstream):
## File class
- File 是对文件或者文件目录的抽象
- 相对路径或者绝对路径
- 实例一旦创建则不可修改
### basic methods
- createfile()/delete()/scanner()
# 注解
**@**
- 注解能改变编译器对程序的处理方式
- 注解能提供额外的信息
- 注解不能改变已编译程序的行动
## 注解的层次结构
![[Pasted image 20230922134126.png]]
## 注解的分类
- Marker Annotations（标记）
不含成员或数据
- Single value Annotations（单值）
只含一个成员并指定成员的值
- Full Annotations（全）
包含多个成员数据，姓名，值
-  Type Annotations（类型）
## 内置注解
-  Repeating Annotations（重复注解）
- @Override - 检查该方法是否是重写方法。如果发现其父类，或者是引用的接口中并没有该方法时，会报编译错误。
- @Deprecated - 标记过时方法。如果使用该方法，会报编译警告。
- @SuppressWarnings - 指示编译器去忽略注解中声明的警告。
作用在其他注解的注解(或者说 元注解)是:
- @Retention - 标识这个注解怎么保存，是只在代码中，还是编入class文件中，或者是在运行时可以通过反射访问。
- @Documented - 标记这些注解是否包含在用户文档中。
- @Target - 标记这个注解应该是哪种 Java 成员。
- @Inherited - 标记这个注解是继承于哪个注解类(默认 注解并没有继承于任何子类)

从 Java 7 开始，额外添加了 3 个注解:

- @SafeVarargs - Java 7 开始支持，忽略任何使用参数为泛型变量的方法或构造函数调用产生的警告。
- @FunctionalInterface - Java 8 开始支持，标识一个匿名函数或函数式接口。
- @Repeatable - Java 8 开始支持，标识某注解可以在同一个声明上使用多次。
# 反射
![[Pasted image 20230922145748.png]]
![[Pasted image 20230922163045.png]]
反射基础：一种是“传统的”RTTI，它假定我们在编译时已经知道了所有的类型；另一种是“反射”机制，它允许我们在运行时发现和使用类的信息。
基础支持类：Class类与java.lang.reflect类
# SPI机制
# 泛型
泛型的本质是为了参数化类型（==在不创建新的类型的情况下，通过泛型指定的不同类型来控制形参具体限制的类型）。也就是说在泛型使用过程中，操作的数据类型被指定为一个参数，这种参数类型可以用在类、接口和方法中，分别被称为泛型类、泛型接口、泛型方法。==

# 异常
>[!Definition]
>Exception is an unwanted or unexpected event, which occurs during the execution of a program, i.e. at run time, that disrupts the normal flow of the program’s instructions. Exceptions can be caught and handled by the program. When an exception occurs within a method, it creates an object. This object is called the exception object. It contains information about the exception, such as the name and description of the exception and the state of the program when the exception occurred.

error与exception的区别在于后者是可用try-catch 结构进行覆盖，前者则尽力避免
## 异常的层次结构
![[Pasted image 20230922131454.png]]
![[Pasted image 20230922131538.png]]
- 内部异常
    - 检查异常 （编译异常）
    - 未检查异常（非编译异常）

printStackTrace() 打印异常的具体信息
toString() 描述具体的异常信息
JVM的异常处理
![[Pasted image 20230922132250.png]]
##如何处理异常
### 关键字
 five keywords: try, catch，throw，throws，finally
 try{codes where exception may occur}
 catch{exception handler}
 finally{codes that will definitely excute }
 throws{a signature that indicates that the method may inccurs exception ,so evey methods that call this method must handle exception with try catch block} only for  checked exceptions
 throw() Instance must be of type **Throwable** or a subclass of **Throwable**(exception specifically)
# 图形化
java swing 图形化界面
![[Pasted image 20230921180202.png]]

|Class|Description|
|-----|-------|
|Component|A Component is the Abstract base class for about the non menu user-interface controls of SWING. Components are represents an object with a graphical representation|
|Container|A Container is a component that can container SWING Components|
|JComponent|A JComponent is a base class for all swing UI Components In order to use a swing component that inherits from JComponent, component must be in a containment hierarchy whose root is a top-level Swing container|
|JLabel|A JLabel is an object component for placing text in a container|
|JButton|This class creates a labeled button|
|JColorChooser|A JColorChooser provides a pane of controls designed to allow the user to manipulate and select a color|
|JCheckBox|A JCheckBox is a graphical(GUI) component that can be in either an on-(true) or off-(false) state|
|JRadioButton|The JRadioButton class is a graphical(GUI) component that can be in either an on-(true) or off-(false) state in the group|
|JList|A JList component represents the user with the scrolling list of text items|
|JComboBox|A JComboBox component is Presents the User with a show up Menu of choices|
|JTextField|A JTextField object is a text component that will allow for the editing of a single line of text|
|JPasswordField|A JPasswordField object it is a text component specialized for password entry|
|JTextArea|A JTextArea object is a text component that allows for the editing of multiple lines of text|
|Imagelcon|A ImageIcon control is an implementation of the Icon interface that paints Icons from Images|
|JScrollbar|A JScrollbar control represents a scroll bar component in order to enable users to Select from range values|
|JOptionPane|JOptionPane provides set of standard dialog boxes that prompt users for a value or Something|
|JFileChooser |A JFileChooser it Controls represents a dialog window from which the user can select a file.|
|JProgressBar|As the task progresses towards completion, the progress bar displays the tasks percentage on its completion|
|JSlider| A JSlider this class is lets the user graphically(GUI) select by using a value by sliding a knob within a bounded interval.|
|JSpinner|A JSpinner this class is a single line input where the field that lets the user select by using a number or an object value from an ordered sequence
# 容器
# 多线程
**一个 Java 程序的运行是 main 线程和多个其他线程同时运行**
![[

]]
**程序计数器主要有下面两个作用：**
1. 字节码解释器通过改变程序计数器来依次读取指令，从而实现代码的流程控制，如：顺序执行、选择、循环、异常处理。
2. 在多线程的情况下，程序计数器用于记录当前线程执行的位置，从而当线程被切换回来的时候能够知道该线程上次运行到哪儿了。
- **并发**：两个及两个以上的作业在同一 **时间段** 内执行。
- **并行**：两个及两个以上的作业在同一 **时刻** 执行。
## 线程状态
==Java 线程在运行的生命周期中的指定时刻只可能处于下面 6 种不同状态的其中一个状态：==
- NEW: 初始状态，线程被创建出来但没有被调用 `start()` 。
- RUNNABLE: 运行状态，线程被调用了 `start()`等待运行的状态。
- BLOCKED：阻塞状态，需要等待锁释放。
- WAITING：等待状态，表示该线程需要等待其他线程做出一些特定动作（通知或中断）。
- TIME_WAITING：超时等待状态，可以在指定的时间后自行返回而不是像 WAITING 那样一直等待。
- TERMINATED：终止状态，表示该线程已经运行完毕。
==线程在生命周期中并不是固定处于某一个状态而是随着代码的执行在不同状态之间切换。==
join()/start()
## 线程优先级
- The default priority is set to 5 as excepted.
- Minimum priority is set to 1.
- Maximum priority is set to 10.
### 相关变量
    1. public static int NORM_PRIORITY
    2. public static int MIN_PRIORITY
    3. public static int MAX_PRIORITY
### 常用方法
currentthread()/getname()获取当前线程的名字
setname()修改线程名
public final int getPriority(): java.lang.Thread.getPriority() 获取线程的优先值
public final void setPriority(int newPriority):设定线程优先值
thread scheduler’s algorithm(Round-Robin, First Come First Serve
![[Pasted image 20230927175602.png]]
### daemon thread(守护线程)
守护线程是程序运行时在后台提供服务的线程，不属于程序中不可或缺的部分。
当所有非守护线程结束时，程序也就终止，同时会杀死所有守护线程。
main() 属于非守护线程。
使用 setDaemon() 方法将一个线程设置为守护线程。
### join()
在线程中调用另一个线程的 join() 方法，会将当前线程挂起，而不是忙等待，直到目标线程结束。
对于以下代码，虽然 b 线程先启动，但是因为在 b 线程中调用了 a 线程的 join() 方法，b 线程会等待 a 线程结束才继续执行，因此最后能够保证 a 线程的输出先于 b 线程的输出。

---
### Java.lang.Thread 类
1. Creating own class which is extending to parent Thread class
2. Implementing the Runnable interface
主要的方法
1. run()
2. start()
![[Pasted image 20231002161436.png]]
