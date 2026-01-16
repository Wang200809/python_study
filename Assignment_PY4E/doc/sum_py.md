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





## Python execution process

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



