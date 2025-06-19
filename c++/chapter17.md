## stream and buffers
![[Pasted image 20240605191032.png]]
## structure
![[Pasted image 20240605191340.png]]
![[chapter17 2024-06-05 19.15.02.excalidraw]]
## cout
### the overload << operator
```cpp
ostream & operator<<(int);
cout << "I'm feeling sedimental over " << boundary << "\n";
```
### output and pointers
```cpp
char name[20] = "Dudly Diddlemore";
char * pn = "Violet D'Amore";
cout << "Hello!";
cout << name;
cout << pn;

int eggs = 12;
char * amount = "dozen";
cout << &eggs; // prints address of eggs variable
cout << amount; // prints the string "dozen"
cout << (void *) amount; // prints the address of the "dozen" string

```

### other ostream methods
![[Pasted image 20240605193102.png]]

#### put()
```cpp
ostream & put(char);  //put prototype
cout.put('W'); // display the W character
cout.put('I').put('t'); // displaying It with two put() calls
cout.put(65); // display the A character
cout.put(66.3); // display the B character
```

#### write()
```
basic_ostream<charT,traits>& write(const char_type* s, streamsize n);
```

### flush the output buffer
```cpp
cout << "Hello, good-looking! " << flush;   //flush manipulator
cout << "Wait just a moment, please." << endl; //endl also works
```

### formatting with cout
#### default format
1. 一个字符占一个位宽
2. 数字以十进制显示
3. 根据字符串长度显示
4. floating types  6位

#### 数字进制转换
```cpp
cout<<hex;
hex(cout);  // 8进制

cout.with(12) //显示位宽

cout.fill('*') // fill the unused spaces
```

### setting float-point precision
```cpp
cout.precision(n);  //浮点数进度
cout.setf(ios_base::showpoint); //Printing Trailing Zeros and Decimal Points

```

![[Pasted image 20240605195148.png]]

## cin
### >> views input
![[Pasted image 20240605195749.png]]
## stream state(流状态)
### members
1. eofbit (endoffile)
2. badbit()
3. failbit(fail to read ,access denied)
![[Pasted image 20240607111738.png]]

![[Pasted image 20240607111808.png]]

### setting state
clear() set all three states (default to 0)
setstate() set single member state
**If you want a program to read further input after a stream state bit has been set, you have to reset the stream state to good**

### single character input
1. get(char &) return a a reference to the istream object used to invoke it
2. If cin.get(char &) encounters the end of a file, either real or simulated from the keyboard, it does not assign a value to its argument,call setstate(fallbit)
3. getchar() returns type int (or some larger integer type, depending on the character set and locale)
4. reaching the end-of-file, real or simulated, cin.get(void) returns the value EOF

| functions                              | description                      | extension                        |
| -------------------------------------- | -------------------------------- | -------------------------------- |
| istream & get(char *, int, char);      | the third argument as delimiter  | leaves the newline character     |
| istream & get(char \*, int);           | newline character as a delimiter | leaves the delimiter character   |
| istream & getline(char \*, int, char); |                                  | discards the newline character   |
| istream & getline(char \*, int);       |                                  | discards the delimiter character |
### other methods
1. read()/write() doesn’t convert input to string form
2. peek() peek the next character with altering it or the stream
3. The gcount() method returns the number of characters read by the last unformatted extraction method(except the extration)
## file input and ouput
### steps
1. Create an ofstream object to manage the output stream.
2. Associate that object with a particular file.
3. Use the object the same way you would use cout
```cpp
// file output 
ofstream fout; // create an ofstream object named fout
fout.open("jar.txt"); // associate fout with jar.txt
fout << "Dull Data";
// file input
// two statements
ifstream fin; // create ifstream object called fin
fin.open("jellyjar.txt"); // open jellyjar.txt for reading
// one statement
ifstream fis("jamjar.txt"); // create fis and associate with jamjar.txt
fout.close(); // close output connection to file
fin.close(); // close input connection to file
```

### stream checking
1. is_open() attempting to open a file by using an inappropriate file mode
2. int main(int argc, char \*argv[])
### file mode
![[Pasted image 20240607121407.png]]

### binary file
```
ofstream fout("planets.dat",
ios_base:: out | ios_base::app | ios_base::binary);
fout.write( (char *) &pl, sizeof pl);
```


### random access
fstream class
1. seekg() moves the input pointer to a given file location
2. seekp()moves the output pointer to a given file location
```cpp
istream & seekg(streamoff, ios_base::seekdir);
istream & seekg(streampos);
fin.seekg(30, ios_base::beg); // 30 bytes beyond the beginning
fin.seekg(-1, ios_base::cur); // back up one byte
fin.seekg(0, ios_base::end); // go to the end of the file
```

tellg()/tellpp() tell the current position in bytes in output/input stream
**When you create an fstream object, the input and output pointers move in
tandem, so tellg() and tellp() return the same value**
## incore formatting
### ostringsteam
```cpp
outstr << "The hard disk " << hdisk << " has a capacity of "
<< cap << " gigabytes.\n";
string result = outstr.str(); // save result
cout << result; // show contents
```

### istringsteam
```cpp
istringstream instr(facts); // use facts to initialize stream
```

