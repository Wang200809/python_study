# 1. Intro 



## 1.1 Hardware basic



### **CPU**

- Executes **native machine instructions** only
- Fetches instructions from **RAM** according to the **program counter (PC)**
- Does **not** understand Python, bytecode, files, or processes

------

### **RAM (Main Memory)**

- Temporarily holds:
  - Running programs’ machine code
  - Runtime data
- All instructions executed by the CPU **must be in RAM**

------

### **Secondary Storage (Disk)**

- Stores data **permanently**
- Programs and data **cannot execute directly** from here

------



## 1.2 **Operating System (OS)**

- A privileged program that:
  - Loads programs from disk into RAM
  - Schedules CPU time
  - Manages memory and I/O
- Parts of the OS are:
  - Stored on disk
  - Loaded into RAM
  - Executed by the CPU when needed (kernel mode)

------

## 1.3 Python Interpreter&PVM

**Interpreter: **

- A native executable program (machine code)
- Responsibilities:
  - Compile Python source code into bytecode
  - Execute bytecode via the PVM
- Stored on disk, loaded into RAM, executed by CPU

**PVM:**

- A component **inside** the Python interpreter
- Interprets Python bytecode by:
  - Determining interpreter control flow
  - Selecting which interpreter machine-code paths execute
- Not hardware, not OS, not kernel code



**Python Script (.py)**

- Text source code
- Stored on disk
- Loaded into RAM as data

**Input / Output Devices**

- Input: keyboard, mouse, etc. (send data to system)
- Output: screen, printer, etc. (receive data from system)
- Accessed **only through the OS**, never directly by Python or CPU





## 1.4 Python execution process

1. **Input devices** generate an input event (e.g. user runs a program),
    which is delivered to the **Operating System** via interrupts.

2. **The Operating System (in RAM)**:
   1. loads the **Python interpreter executable** from secondary storage into RAM;
   2. loads the **Python script (.py file)** from secondary storage into RAM;
   3. creates a process and schedules it on the CPU.
3. **The Python interpreter** compiles the Python script in RAM into **bytecode**.

4. **The Python Virtual Machine (PVM)** interprets the bytecode by selecting
    and executing corresponding **existing machine code** inside the interpreter.

5. **The CPU** fetches and executes the interpreter’s machine instructions
    from RAM, following the Program Counter (PC).

6. When the Python program needs to **produce output** (e.g. `print()`):

   1. the interpreter calls **operating system services** (system calls);
   2. the OS writes output data from RAM to the appropriate **device buffer**.

7. **Output devices** (screen, file, network, etc.) read data from their buffers
    and present the result to the outside world.



# 2. Language basic & Syntax



## 2.1 Variables&Constants

### Constants:

- Fixed values such as numbers, letters, and strings
- String constants use single quotes (') or double quotes (")
- Numeric constants are as you expect

### Variables:

- A variable is a named place in the memory where a programmer can store data and later retrieve the data using the variable "name"
- Programmers get to choose the names of the variables
- You can change the contents of a variable in a later statement

### Variable Naming rule

1. **Must start with a letter or underscore**
   - Valid: `name`, `_value`, `data1`
   - Invalid: `1data`, `9count`
2. **Can only contain letters, numbers, and underscores**
   - Valid: `user_name`, `value2`, `_private_var`
   - Invalid: `user-name`, `value@2`, `my.variable`
3. **Case-sensitive**
   - `Name`, `name`, and `NAME` are three different variables
4. **Cannot use reserved words**
   - Cannot use: `class`, `def`, `if`, `for`, `while`, `return`, `True`, `False`, `None`, etc.
   - Your notes already list all the reserved words

## 2.2 Expression

Expressions can **manipulate variables**, such as adding one to x and storing the result back in x.

### Operator Precedence Rules

![](C:\work\preparation-monash\python\hello_world_demo\Assignment_PY4E\doc\assets\01_string\operator_precedence_rule.png)





### Rmq:

#### difference between `==` and `is`

To clarify the difference between `==` and `is`:

- `==` checks if the values of two objects are equal.
- `is` checks if two references point to the same object in memory (identity).

#### **+ operator**: 

The plus operator behaves differently based on the types of its operands: it adds integers and concatenates strings.

## 2.3 Reserved word

A reserved word in Python, also known as a keyword, is a word that has a special meaning in the language and cannot be used for any other purpose, such as naming variables or functions. 

|        |          |         |          |        |
| ------ | -------- | ------- | -------- | ------ |
| False  | await    | else    | import   | pass   |
| None   | break    | except  | in       | raise  |
| True   | class    | finally | is       | return |
| and    | continue | for     | lambda   | try    |
| as     | def      | from    | nonlocal | while  |
| assert | del      | global  | not      | with   |
| async  | elif     | if      | or       | yield  |



# 3. Function

## 3.1 Build-in Function

### Data type conversion

**Data Types and Conversion**

- Python distinguishes between integers (whole numbers) and floating-point numbers (numbers with decimals).
- Built-in functions like `int()` and `float()` can convert between types, allowing for manipulation of data.

### Input/output

**Input Handling**

- The `input()` function reads user input as a string, regardless of whether the input looks like a number.
- Proper type conversion is necessary to perform arithmetic operations on user input.



## 3.2 user-definite function

### Definition of Function & Code Sample

**Definition**
 A function is a named block of code that is stored using `def` and executed only when called.

**Code sample**

```python
def greet(name):
    print("Hello", name)

greet("Alice")
```

------

### Why Use Functions

- To **avoid code repetition** (DRY: Don’t Repeat Yourself).
- To **store logic in one place** and reuse it multiple times.
- To make programs **easier to read, modify, and maintain**.
- To break a program into **smaller, manageable units**.

------

### Mechanism: How Functions Work in a Program (Invocation)

- Defining a function **does not execute** its code.
- When a function is **called (invoked)**:
  1. Python temporarily jumps to the function code.
  2. The function code is executed.
  3. Python returns to the point where the function was called.
- Python always **remembers where to continue execution** after the function finishes.

------

### How to Use Functions (Details)

#### 3.1 Parameters and Arguments

- **Parameters**:
  - Variables in the function definition.
  - Receive values when the function is called.
- **Arguments**:
  - Actual values passed into the function.
- Argument order must match parameter order.

```python
def subtract(a, b):
    return b-a
print(subtract(1, 2))  
```



#### 3.2 Return Values

- `return`:
  - stops the function,
  - sends a value back to the caller.
- Returned values can be stored or used in expressions.

------

#### 3.3 Types of Functions

- **Fruitful functions**:
  - return a value.
- **Non-fruitful functions**:
  - do not return a value (return `None`).

```python
def say_hi():
    print("Hi")   # non-fruitful
```

# 4. Execution Flow

### Rmq:

1. Conditional statement order: Order conditions from smallest scope to largest scope(specific to general)
   wrong example:

~~~python
# ❌ WRONG: Largest scope first (least restrictive first)
age = int(input("Enter age: "))

# WRONG: Check largest scope first
if age >= 13:  # Scope: [13, ∞) - TOO BROAD! Catches both teenagers AND adults
    print("Teenager")

# This condition will NEVER execute!
elif age >= 18:  # Scope: [18, ∞) - UNREACHABLE CODE!
    print("Adult")

else:
    print("Child")
~~~



## **Assignment Statement**

an assignment statement is a process that assigns a value to a variable, not just a statement on its own.

## **Sequential Steps**

- **Def:** The most basic pattern is sequential, where instructions are executed one after another.
- ex: An example is provided with a simple Python program that assigns a value to a variable and prints it.

## **Conditional Steps**

- **Def:** Conditional programming involves using "if" statements to execute code based on certain conditions.

- ~~~python
  # if  statement
  age=int(input("Enter age: "))
  if age>=18:
      print("Adult")
  elif age>=13:
      print("Teenager")
  else:
      print("Child")
  ~~~

- A flowchart illustrates how the program evaluates conditions and executes corresponding statements.

## **Looping Steps**

A **loop** is a control structure that allows a program to execute a block of code repeatedly, which is essential for processing multiple values efficiently.

------

### 1. Why Use Loops

- To perform **repetitive tasks** without duplicating code.
- To process **collections of data** (numbers, strings, lists) one element at a time.
- To derive results such as:
  - maximum / minimum
  - total
  - count
  - membership (filtering)

------

### 2. Types of Loops in Python

#### 2.1 Indefinite Loops (`while`)

- A `while` loop runs **as long as a condition is true**.
- The condition is checked **before each iteration**.
- An iteration variable must change inside the loop to avoid **infinite loops**.

```
while n > 0:
    print(n)
    n = n - 1
```

------

#### 2.2 Definite Loops (`for`)

- A `for` loop runs over a **known set of items**.
- It is more predictable and easier to reason about.
- Commonly used to iterate over lists, strings, or other collections.

```
for i in [5, 4, 3, 2, 1]:
    print(i)
```

------

### 3. Loop Control Statements

- `break`: immediately exits the loop.
- `continue`: skips the current iteration and moves to the next one.

These statements allow finer control over loop execution and help prevent unintended behavior.

------

### 4. Loop Execution Model (How Loops Work)

- A loop processes data **sequentially**, one item per iteration.
- Variables are:
  - initialized **before** the loop,
  - updated **during** each iteration.
- The final result is obtained **after all iterations complete**.

This reflects how computers naturally process data step by step.

------

### 5. Common Loop Idioms (Patterns)

#### 5.1 Counting

- Use a counter variable to track how many times a loop runs.

```
count = 0
for item in items:
    count = count + 1
```

------

#### 5.2 Totaling

- Accumulate values to compute a sum.

```
total = 0
for num in numbers:
    total = total + num
```

------

#### 5.3 Filtering

- Use conditionals inside loops to select specific values.
- Boolean variables can be used as **flags** to record whether a condition is met.

------

### 6. Finding the Largest Value

- Initialize a variable before the loop.
- Compare each value with the current largest value.
- Update the variable when a larger value is found.

```
largest = -1
for num in numbers:
    if num > largest:
        largest = num
```

------

### 7. Finding the Smallest Value

**Problem with Fixed Initial Values**

- Initializing with a fixed number (e.g. `-1`) can produce incorrect results.

**Using *None* as a Flag Value**

- `None` indicates that no value has been seen yet.
- The first value encountered becomes the initial smallest value.

```
smallest = None
for num in numbers:
    if smallest is None or num < smallest:
        smallest = num
```

This approach is safer and more flexible.

# 5. Data Structures



## 5.1 Strings

String is **immutable**, every change of string is a creation of new string.

| b    | a    | n    | a    | n    | a    |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 0    | 1    | 2    | 3    | 4    | 5    |

| M    | o    | n    | t    | y    | ,    | p    | y    | t    | h    | o    | n    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | 10   | 11   |



~~~python
>>> s1='ban'
>>> s2='ana'
>>> n='10'
>>> concatenation=s1+s2
# 1. Concatenation and in
>>> print(concatenation)
banana
>>> print('a' in s1)
True
# 2. converting
>>> print(int(n)-1)
9
# 3. index and slicing
>>> print(concatenation[0:2])
ba
>>> s="Monty,python"
#end index num is not included 
>>> print(s[0:4])
Mont
>>> print(s[5:6])
,
# without start index means from the first index
>>> print(s[:2])
Mo
# no end index means untill to the end
>>> print(s[10:])
on
# 4. length
>>>fruit="banana"
>>>length=len(fruit)
>>>print(length)
6
# 5. find(): find the first occurrence of the substring
>>> concatenation.find('na')
2
# 6. upper lower
>>> print(name.upper())
BOB
>>> print(name.lower())
bob

~~~

#### parsing&extracting

![](C:\work\preparation-monash\python\hello_world_demo\Assignment_PY4E\doc\assets\01_string\parsing&extracting.png)



#### Replace

![](C:\work\preparation-monash\python\hello_world_demo\Assignment_PY4E\doc\assets\01_string\replace.png)

### Iteration

~~~python
#while loop
fruit='banana'
index=0
while index<len(fruit):
    letter=fruit[index]
    print(index,letter)
    index=index+1

#for loop is better!!!!
fruit='banana'
for letter in fruit:
    print(letter)
~~~





### String Comparison and Methods

- Strings can be compared using `==`, `<`, and `>`, with uppercase letters being less than lowercase letters.

##### Python String Comparison Rules

1. **Compare the first characters** using their **Unicode (ASCII) values**.
2. **If they are equal, compare the next characters.**
3. **Continue until a difference is found or one string ends.**
   - If one string ends first, **the shorter string is smaller**.

##### Examples

~~~python
"letter" > "Letter"`
#because `l (108) > L (76)`
"apple" < "apply"`
#because `e (101) < y (121)`
"cat" < "catalog"`
#because `"cat"` ends first
~~~

~~~css
65 ───────── 90     97 ───────── 122
   A ... Z          	a ... z
~~~



- Strings are objects with built-in methods, such as `lower()`, which returns a lowercase copy without altering the original string.









## 5.2 Files

~~~python
# 1. open file to load files in RAM as a variable
file_variable=open("file_name",'mode')
# file_name require the file in the same dic
# mode: r: read  w: write
# 2. newline(\n): indicate the end of a line
>>> stuff='n\nm'
>>> print(stuff)
n
m
# 3. iterate file as lines
file=open('test.txt')
for line in file:
    # wrong: print() add \n in the end of each line
    print(line)
	# correct: 
	print(line.rstrip())
# 4. read(): input the whole file(newlines and all) as a single string
>>> input=file.read()
>>> print(len(input))
470

~~~







## 5.3 Lists

### Intro

**Understanding Algorithms and Data Structures**

- Algorithms: A set of rules or steps used to solve a problem
- Data structures: A particular way of organizing data in a computer



~~~python
# 1. Introduction
# Lists can hold multiple values in a single variable even another list
>>> list=[1,'red',[5,6.01]]
>>> print(list)
[1, 'red', [5, 6.01]]
# list could be empty
>>> empty_list=[]
>>> print(empty_list)
[]
# 2. Mutable list
>>> list[0]=2
>>> print(list)
[2, 'red', [5, 6.01]]
# 3. length of a list
>>> print(len(list))
3
# 4. range function: 
# return a list of numbers that rane from zero to one less than the parameter
# use it as an index during iteration
list_01 = [2, 'red', [5, 6.01]]
print("list before iteration: "+str(list_01))
for i in range(len(list_01)):
    print(i)
    if i+1 < len(list_01):
        temp = list_01[i]
        list_01[i] = list_01[i + 1]
        list_01[i + 1] = temp
    print("list current status: "+str(list_01))
print("list after iteration: "+str(list_01))


~~~



Mutable vs. Immutable Data Types

- Lists are mutable, meaning their contents can be changed, while strings are immutable and cannot be altered directly.
- The lecture explains how to access and modify list elements using indexing.

Using Lists in Loops

- The lecture discusses how to iterate through lists using loops, emphasizing the use of the `for` loop and the `range` function for indexed access.
- It highlights the importance of understanding the index positions when working with lists.

This summary captures the key points of the lecture on data structures, particularly focusing on lists and their functionalities in Python programming.

### Manipulate list

~~~python
# 1. concatenating list
>>> a=[1,2]
>>> b=[3,4]
>>> print(a+b)
[1, 2, 3, 4]
# 2. slicing as a string
>>> c=a+b
>>> c[:2]
[1, 2]
>>> c[1:2]
[2]
>>> c[2:]
[3, 4]
>>> c[:]
[1, 2, 3, 4]
# 3. building a list from Scratch
>>> d=list()
>>> d.append('hahahah')
>>> print(d)
['hahahah']
# 4. Is sth in a list?
>>> 'ha' in d
False
>>> 'hahahah' in d
True
# 5. sort
>>> d.sort()
Traceback (most recent call last):
  File "<python-input-8>", line 1, in <module>
    d.sort()
    ~~~~~~^^
TypeError: '<' not supported between instances of 'int' and 'str'
>>> d.remove(0)
>>> d.append("you")
>>> d.sort()
>>> d[]
  File "<python-input-12>", line 1
    d[]
    ^
SyntaxError: invalid syntax. Did you mean 'del'?
>>> d[:]
['hahahah', 'you']

# 6. split
# defaut split with space
>>> abc='How are you?'
>>> group=abc.split()
>>> print(group)
['How', 'are', 'you?']
>>> for g in group:
...     print(g)
...
How
are
you?
# indicate the split signal
>>> line='alice;bob;camille'
>>> friends=line.split()
>>> print(friends)
['alice;bob;camille']
>>> friends=line.split(";")
>>> print(friends)
['alice', 'bob', 'camille']

~~~



### Terminology:

| EN             | CN   | EN   | CN   | EN   | CN   |
| -------------- | ---- | ---- | ---- | ---- | ---- |
| square bracket | [ ]  |      |      |      |      |
|                |      |      |      |      |      |
|                |      |      |      |      |      |



## 5.4 Dictionaries

### Intro

Like HashMap in Java

~~~python
>>> d1={"alice":13}
>>> d2={"dic":d1}
>>> print(d2)
{'dic': {'alice': 13}}
>>> d3={"d1":d1,"d2":d2}
>>> print(d3)
{'d1': {'alice': 13}, 'd2': {'dic': {'alice': 13}}}
~~~



### manipulate

~~~python
# ==================== 1. 创建字典 ====================
# 方式1：直接创建空字典
empty_dict = {}
# 方式2：创建带初始值的字典
person = {
    "name": "Alice",
    "age": 25,
    "city": "Beijing",
    "hobbies": ["reading", "running"]  # 值可以是列表
}
# 方式3：通过 dict() 函数创建
fruit = dict(apple=3, banana=5, orange=2)

# ==================== 2. 访问字典的值 ====================
# 方式1：通过键访问（最常用）
print(person["name"])  # 输出: Alice
# 方式2：通过 get() 方法（推荐，键不存在时不会报错）
print(person.get("age"))  # 输出: 25
print(person.get("gender", "unknown")+1)  # 键不存在时返回默认值: unknown, 如果存在则+1
if key in counts:
    counts[key] = counts[key] + 1
else:
    counts[key] = 1

# ==================== 3. 添加/修改键值对 ====================
# 添加新键值对（键不存在时）
person["gender"] = "female"
# 修改已有键的值（键存在时）
person["age"] = 26
print(person)  # 输出: {'name': 'Alice', 'age': 26, 'city': 'Beijing', 'hobbies': ['reading', 'running'], 'gender': 'female'}

# ==================== 4. 删除键值对 ====================
# 方式1：del 语句（删除指定键，键不存在会报错）
del person["city"]
# 方式2：pop() 方法（删除并返回对应值，可指定默认值）
hobbies = person.pop("hobbies")
print(hobbies)  # 输出: ['reading', 'running']
# 方式3：popitem() 方法（删除并返回最后插入的键值对，3.7+ 有序）
last_item = person.popitem()
print(last_item)  # 输出: ('gender', 'female')
# 方式4：clear() 清空所有键值对
fruit.clear()
print(fruit)  # 输出: {}

# ==================== 5. 遍历字典 ====================
# 遍历所有键
for key in person.keys():
    print(key)  # 输出: name, age

# 遍历所有值
for value in person.values():
    print(value)  # 输出: Alice, 26

# 遍历所有键值对（最常用）
for key, value in person.items():
    print(f"{key}: {value}")  # 输出: name: Alice, age: 26

# ==================== 6. 其他常用操作 ====================
# 判断键是否存在
print("name" in person)  # 输出: True
print("city" in person)  # 输出: False

# 获取字典长度（键值对数量）
print(len(person))  # 输出: 2

# 合并两个字典（3.9+ 语法）
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = dict1 | dict2
print(merged_dict)  # 输出: {'a': 1, 'b': 3, 'c': 4}

# 复制字典（浅拷贝）
person_copy = person.copy()
person_copy["age"] = 27
print(person)  # 原字典不变: {'name': 'Alice', 'age': 26}
print(person_copy)  # 拷贝字典修改: {'name': 'Alice', 'age': 27}
~~~





# 6. Terminology

#### variable

**iteration variable:** 

n is iteration variable

~~~python
n=5
while n>0:
    print(n)
    n=n-1
print("Over")
~~~



**Nesting** （嵌套）

a loop or a conditional statement inside another loop or conditional statement. This allows you to create more complex behaviors in your programs.

**indented:** 

缩进 In Python, the way you can tell that a sequential code is when it's not being indented.

### Signal

| Symbol | English name              | Symbol | English name         |
| ------ | ------------------------- | ------ | -------------------- |
| `,`    | comma                     | `@`    | at                   |
| `.`    | dot / period              | `#`    | hash                 |
| `?`    | question mark             | `$`    | dollar sign          |
| `!`    | exclamation mark          | `%`    | percent              |
| `:`    | colon                     | `^`    | caret                |
| `;`    | semicolon                 | `&`    | ampersand            |
| `'`    | apostrophe / single quote | `*`    | asterisk             |
| `"`    | double quote              | `_`    | underscore/underline |
| ```    | backtick                  | `~`    | tilde                |



| Brackets Symbol | English name          |
| --------------- | --------------------- |
| `( )`           | parentheses           |
| `[ ]`           | square brackets       |
| `{ }`           | curly braces / braces |
| `< >`           | angle brackets        |

| Operators Symbol | English name          |
| ---------------- | --------------------- |
| `=`              | equals                |
| `==`             | double equals         |
| `!=`             | not equal             |
| `>`              | greater than          |
| `<`              | less than             |
| `>=`             | greater than or equal |
| `<=`             | less than or equal    |
| `+`              | plus                  |
| `-`              | minus                 |
| `*`              | multiply              |
| `/`              | divide                |
| `%`              | modulo 取余           |



1. **Operators: + - \* / %**
2. **modulo operator(%): 取余**
3. **odd values:** 奇数 （number%2≠0）
4. **parentheses**: 圆括号
5. **exponentiation**: 求幂
6. **multiplication**: 乘法
7. **subtraction**: 减法
8. precedence: the condition of being more important than somebody else and therefore coming or being dealt with first
9. quotient: a number which is the result when one number is divided by another
10. remainder: the numbers left after one number has been subtracted from another, or one number has been divided into another差数；余数

### build-in function

1. operand: the number on which an operation is to be done
2. concatenate: link
3. Tracebacks: An error?
4. distinguish: to recognize the difference between two people or things
5. Built-in functions:  existing as an essential part of something
6. decimal: a&n 小数

# 7. Errors

6. Errors & Debugging
│
├── SyntaxError
├── IndentationError
├── TypeError
├── ValueError
└── try / except

## 6.1 Syntax Error

### String related

#### unterminated string literal

***SyntaxError: unterminated string literal (detected at line 26)***

```python
s1="This is a
test string"
print(s1)
# reason：double quotes doesn't allow a line break in the mid
# solution: use """""", tripple quotes are multi-line strings
s2="""This is a
test string"""
```



## 6.2 Indentation Error

> ❗ 会的。Tabs 和 4 spaces 混用，确实会导致 Python 识别错误，而且是新手最常见、最隐蔽的坑之一。

下面我用**非常清晰、工程化的方式**给你讲明白：**为什么会出问题、什么时候会出问题、以及你应该怎么做**。

------

### 一、Python 对缩进的“残酷事实”

#### ✅ Python **不是“看起来一样就行”**

Python **不是**像 Java / C 那样用 `{}`，而是：

> 缩进 = 语法的一部分

也就是说：

- 缩进不对

  → **语法就不对**

- 混用缩进

  → **解释器可能直接报错，或者更糟：逻辑错误**

------

### 二、Tabs vs Spaces：为什么会出问题？

#### 表面看起来 👀

```python
if x >0:
print("positive")
```

#### 实际上 Python 看到的是 👇

- `Tab` ≠ `4 spaces`
- Tab 是一个 **控制字符**
- Python **按“字符”判断缩进层级**

------

### 三、典型错误示例（非常常见）

#### ❌ 混用 Tab 和 Space

```python
if x >0:
print("positive")# tab
print("done")# 4 spaces
```

Python 可能报：

```
TabError: inconsistent use of tabs and spaces in indentation
```

或者在某些情况下：

- **不报错**
- 但程序逻辑错了（更危险）

------

### 四、Python 官方立场（很重要）

📌 **PEP 8（Python 官方代码规范）明确规定：**

> 👉 Use 4 spaces per indentation level.
>
> 👉 **Spaces are the preferred indentation method.**

换句话说：

- **Tab：不推荐**
- **4 spaces：唯一正确姿势**

------

### 五、你在 Notepad / Notepad++ / 简单编辑器里要特别小心

#### ⚠️ 为什么 Notepad 风险大？

- 不会高亮显示 Tab
- Tab 看起来像 spaces
- 一旦混用，你**肉眼根本分不出来**

#### 常见新手“中招场景”

- 一开始用 Tab
- 后来复制粘贴代码（spaces）
- 程序突然报错，看不懂

------

### 六、强烈建议你这样做（实操级建议）

#### ✅ 方案 1（最安全）：**只用 4 spaces，从不用 Tab**

- 每一层缩进：**按 4 次空格**
- 完全不要按 Tab 键

📌 这是你现在阶段 **最稳的做法**

------

#### ✅ 方案 2（更推荐）：换一个“懂 Python 的编辑器”

如果你愿意升级工具（强烈建议）：

#### 👍 **VS Code**

- 默认 Python = 4 spaces
- 自动把 Tab 转成 spaces
- 会直接提示缩进错误

#### 👍 **PyCharm**

- 工业级
- 永远不会混用
- 非常适合你未来 Monash 的作业

------

### 七、如何快速检查「有没有 Tab」

如果你怀疑代码有问题：

#### 方法 1（简单）

- 全选代码
- 删除缩进
- 用 **空格重新缩进**

#### 方法 2（编辑器）

- 开启 “显示不可见字符”
- 看是否有 `→`（Tab）



### ✅ 一句话总结（你可以记住这一句）

> Python 中：Tab 和 4 spaces 混用 = 潜在灾难 永远用 4 spaces，或者让编辑器替你管。



## 6.3 Type Error

**Type Errors and Tracebacks**

- Python raises a TypeError when trying to combine incompatible types (e.g., a string and an integer).
- Tracebacks provide information about errors, indicating where the issue occurred and the type of error.

### Example

#### try except traceback error:

~~~python
age=None
try:
    age = int(input("Enter age: "))
except ValueError:
    print("Pls enter integer number as age")
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
elif age <= 0:
    print("Pls enter age larger than 0")
else:
    print("Child")

~~~





## 6.4 Value Error



## 6.5 Reference Error

### index error

![image-20260126151534308](C:\work\preparation-monash\python\hello_world_demo\Assignment_PY4E\doc\assets\01_string\index_error.png)

##  try except else

In Python's `try...except...else` structure, the `else` block serves as a **success handler**.

### The Role of `else`

The code inside the `else` block executes **only if no exceptions were raised** in the `try` block.

#### Key Benefits

- **Separation of Concerns:** It separates the "risky" code (parsing input) from the "logic" code (processing the age).
- **Avoids Over-Catching:** It ensures that you aren't accidentally catching `ValueErrors` that might occur inside your `if/elif` logic itself—it only handles the error from the `input` line.
- **Clean Flow:** It prevents the `TypeError` you encountered by guaranteeing that `age` is a valid integer before any comparisons happen.

```python
try:
    age = int(input("Enter age: "))
except ValueError:
    print("Invalid input!") # Runs ONLY if try FAILS
else:
    print("Valid age!")     # Runs ONLY if try SUCCEEDS
    if age >= 18:           # Logic is now safe from TypeError
        print("Adult")
```



~~~python

~~~

