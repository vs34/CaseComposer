# CaseComposer : Test Case Generator
**💡 Original Concept & Implementation:** Developed by [Vaibhav Singh (the BESTEST vaibhav around)](https://github.com/vs34) 🎯  

CaseComposer is a test case generation and validation framework that compares the outputs of a correct and incorrect implementation. It automatically identifies discrepancies and logs incorrect outputs.

## Directory Structure
```
CaseComposer/
│── tester.py              # Main script to run test cases and compare outputs
│── testCaseGenerator.py   # Script to generate test cases
│── wrongCases.csv         # Stores test cases where the output differs
│── correct.cpp            # Correct implementation (reference solution)
│── wrong.cpp              # Incorrect implementation (to be tested)
│── notworking.out         # Executable for the incorrect implementation
│── working.out            # Executable for the correct implementation
│── runTCGen.md            # Shell script to compile and execute the test framework
│── README.md              # Documentation
```

## Prerequisites
Ensure you have the following installed:
- Python 3+
- GCC (g++-14 or compatible version)

## Setup and Installation
### 1. Clone the repository
```bash
git clone https://github.com/yourusername/CaseComposer.git
cd CaseComposer
```

### 2. Add Your Implementations
- Copy and paste your **correct** code into `correct.cpp`.
- Copy and paste your **incorrect** (to be tested) code into `wrong.cpp`.
- Make sure both programs take input from `stdin` and output results to `stdout`.

### 3. Set Up the Test Case Generator
- The test cases are generated using `testCaseGenerator.py`.
- If you already have a test case generator, copy your logic into this file.
- You can generate a new one using ChatGPT, Gemini, DeepSeek, etc.
- Ensure that the output format matches the expected input of your programs.

### 4. Compile the C++ Programs
```bash
g++-14 correct.cpp -o working.out
g++-14 wrong.cpp -o notworking.out
```

### 5. Run the Test Framework
```bash
python3 tester.py
```
Alternatively, you can use the shell script:
```bash
bash runCaseComposer.md
```

## How It Works
1. You will be asked to enter the number of test cases to generate and evaluate.
2. The script generates test cases using `testCaseGenerator.py`.
3. It runs both `working.out` and `notworking.out` on the same test cases.
4. The outputs are compared, and discrepancies are logged in `wrongCases.csv`.
5. At the end, you will be asked if you want to see all the incorrect test cases.

## Progress Tracking

As the test cases are being executed, you will see a progress bar indicating the completion percentage, after you enter the number of test cases you wish to test for.  
```
Number of test cases to check (integer): 2
Progress: |██████████████████████████████████████████████████| 100.0% Complete
```
This helps you monitor the execution status in real time.  

## Output Format
If discrepancies are found, they will be logged in `wrongCases.csv` as:
```
test case, not working output, working output
1
10 1
2 8 1 8 7 9 2 2 2 3
6 , No , Yes 
++++++++++++++++++++++++++++++++++++++++++++++
1
3 1
8 6 8
6 , Yes , No 
++++++++++++++++++++++++++++++++++++++++++++++
```
Additionally, if the user opts to view the incorrect cases, they are displayed as:
```
------------------------------------------------------------
| Wrong Output Number | Not Working Output | Expected Output |
------------------------------------------------------------

Test Case 1:
----------------
1
5 1
9 8 9 6 10
10
------------------------------------------------------------
|         1          |        Yes         |       No        |
------------------------------------------------------------
```

## Troubleshooting
- **Error: `testCaseGenerator.py` not found!**  
  Ensure the file exists in the directory.

- **Error: One of the executables failed to run properly!**  
  Verify the compilation of `correct.cpp` and `wrong.cpp`.

- **Progress bar stuck at 0%**  
  Ensure `testCaseGenerator.py` is generating valid test cases.

## License
This project is open-source under the MIT License.

## Contributions
Feel free to submit pull requests or open issues for improvements!

---
Happy Testing! 🚀
