# CaseComposer

# Test Case Generator

## Description

The Test Case Generator is a tool designed to automate the generation and testing of test cases for C or C++ code. Here's a streamlined and specific description:

---

### Test Case Generator

The Test Case Generator automates the creation and validation of test cases for C or C++ programs. It performs the following tasks:

1. **Compilation**:
   - Compiles two C files (`file1.c` and `file2.c`) using `clang`, or two C++ files (`file1.cpp` and `file2.cpp`) using `clang++`.
   - Produces two executables: `working.out` and `notworking.out`.

2. **Test Case Generation and Execution**:
   - Runs `tc.py` to generate test cases. **You need to write tc.py to genrate testcase according to the given question**
   - Executes the generated test cases using both `working.out` and `notworking.out`.

3. **Output Comparison**:
   - Compares the outputs of `working.out` and `notworking.out`.
   - If the outputs differ, it prints the differing test case and logs it to `tc1.csv`.

### Workflow

1. **Generate Test Cases**:
   - `tc.py` generates the input test cases.

2. **Run and Compare Outputs**:
   - `tester.py` runs the generated test cases through both executables.
   - Compares the outputs:
     - If different, prints the test case and appends it to `tc1.csv`.

### Example Usage

1. **Compilation**:
   ```bash
   clang file1.c -o working.out
   clang file2.c -o notworking.out
   ```

2. **Generate Test Cases**:
   ```bash
   python tc.py
   ```

3. **Run and Compare**:
   ```bash
   python tester.py
   ```

## Prerequisites

- `clang++` for C++ compiler installed on the system
- `clang` for C compiler installed on the system
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
2. Modify file1.c/.cpp and file2.c/.cpp to contain the desired C/C++ code.
### FOR C CODE

-- FOR UNIX AND LINUX

       clang file1.c -o working.out
       clang file2.c -o notworking.out
-- FOR WINDOWS

       clang file1.c -o working.exe
       clang file2.c -o notworking.exe
### FOR C++ CODE

-- FOR UNIX AND LINUX

       clang++ file1.cpp -o working.out
       clang++ file2.cpp -o notworking.out
-- FOR WINDOWS

       clang++ file1.cpp -o working.exe
       clang++ file2.cpp -o notworking.exe

 
 3. Run the following command to generate the test cases:

        python3 tester.py

This command will compile file1.c and file2.c into working.out and notworking.out, respectively according to tc.py genrated testcase. It will then compare the outputs of both executables and add any differing outputs to tc1.csv.

View the generated test cases in tc1.csv.
## Working
The tcc.py code takes input from the tc.py code, which prints the test cases. The tcc.py executable file then compares the output printed by the working.out and notworking.out files using the os module and bash scripting.

Here is a more detailed explanation of each step:
1. The tc.py code prints the test cases.
2. The tester.py executable file runs the test cases and saves the output to the working.out and notworking.out files.
3. The tester.py executable file uses the os module to get the current working directory.
4. The tester.py executable file uses bash scripting to compare the output of the working.out and notworking.out files.
5. The tester.py executable file prints a message indicating whether the test cases passed or failed.

This process can be used to automate the testing of software. By running the test cases and comparing the output, the tcc.py executable file can identify any errors in the software. This can help to improve the quality of the software and ensure that it is working properly.
