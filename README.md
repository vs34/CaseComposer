# CaseComposer

# Test Case Generator

## Description

The Test Case Generator is a tool designed to automate the generation of test cases for C code. It compiles two C files, `file1.c` and `file2.c`, using `clang` to create two separate executable files, `working.out` and `notworking.out`, respectively. It then compares the output of both executable files and adds any differing outputs to `tc1.csv`. Additionally, it takes input from `tc.py` to generate the test cases.

## Prerequisites

- `clang` compiler installed on the system
- Python 3.x
- you have to write tc.py that print testcase 

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/username/test-case-generator.git
2. Navigate to the project directory:
   ```bash
   cd CaseComposer
 
 
## Usage
1. you have to make a python file named tc.py which print random test cases according to the question inside Case Composer directory. you can change language of tc file change source code (tcc.py) line 13

1. Open the terminal and navigate to the project directory.

2. Modify file1.c and file2.c to contain the desired C code.

FOR UNIX AND LINUX

       clang file1.c -o working.out
       clang file2.c -o notworking.out
FOR WINDOWS

       clang file1.c -o working.exe
       clang file2.c -o notworking.exe
 4. Run the following command to generate the test cases:

        python3 tcc.py

This command will compile file1.c and file2.c into working.out and notworking.out, respectively according to tc.py genrated testcase. It will then compare the outputs of both executables and add any differing outputs to tc1.csv.

View the generated test cases in tc1.csv.
## Working
The tcc.py code takes input from the tc.py code, which prints the test cases. The tcc.py executable file then compares the output printed by the working.out and notworking.out files using the os module and bash scripting.

Here is a more detailed explanation of each step:
1. The tc.py code prints the test cases.
2. The tcc.py executable file runs the test cases and saves the output to the working.out and notworking.out files.
3. The tcc.py executable file uses the os module to get the current working directory.
4. The tcc.py executable file uses bash scripting to compare the output of the working.out and notworking.out files.
5. The tcc.py executable file prints a message indicating whether the test cases passed or failed.

This process can be used to automate the testing of software. By running the test cases and comparing the output, the tcc.py executable file can identify any errors in the software. This can help to improve the quality of the software and ensure that it is working properly.
