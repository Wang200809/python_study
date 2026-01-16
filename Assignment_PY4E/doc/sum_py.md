# Intro Hardware



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

### **Operating System (OS)**

- A privileged program that:
  - Loads programs from disk into RAM
  - Schedules CPU time
  - Manages memory and I/O
- Parts of the OS are:
  - Stored on disk
  - Loaded into RAM
  - Executed by the CPU when needed (kernel mode)

------

### **Python Interpreter (CPython)**

- A native executable program (machine code)
- Responsibilities:
  - Compile Python source code into bytecode
  - Execute bytecode via the PVM
- Stored on disk, loaded into RAM, executed by CPU

------

### **PVM (Python Virtual Machine)**

- A component **inside** the Python interpreter
- Interprets Python bytecode by:
  - Determining interpreter control flow
  - Selecting which interpreter machine-code paths execute
- Not hardware, not OS, not kernel code

------

### **Python Script (.py)**

- Text source code
- Stored on disk
- Loaded into RAM as data

------

### **Input / Output Devices**

- Input: keyboard, mouse, etc. (send data to system)
- Output: screen, printer, etc. (receive data from system)
- Accessed **only through the OS**, never directly by Python or CPU





# Python execution process

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



# Variables&Expression



### intro

#### Assignment Statement

an assignment statement is a process that assigns a value to a variable, not just a statement on its own.

#### Expression

assume x is a variable.

Expressions can manipulate variables, such as adding one to x and storing the result back in x.

#### Reserved word

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





# Program Steps

**Sequential Steps**

- **Def:** The most basic pattern is sequential, where instructions are executed one after another.
- ex: An example is provided with a simple Python program that assigns a value to a variable and prints it.

**Conditional Steps**

- **Def:** Conditional programming involves using "if" statements to execute code based on certain conditions.
- A flowchart illustrates how the program evaluates conditions and executes corresponding statements.

**Looping Steps**

- The repeat pattern allows for executing a block of code multiple times using loops like "while" and "for."
- The explanation includes how to avoid infinite loops by managing iteration variables, ensuring the loop terminates correctly.



## Terminology

**iteration variable:** n is iteration variable

~~~python
n=5
while n>0:
    print(n)
    n=n-1
print("Over")
~~~



**Nesting** （嵌套）a loop or a conditional statement inside another loop or conditional statement. This allows you to create more complex behaviors in your programs.



**indented:** 缩进 In Python, the way you can tell that a sequential code is when it's not being indented.
