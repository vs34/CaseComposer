# CaseComposer : Test Case Generator

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

## Setup and Execution
### 1. Clone the repository
```bash
git clone https://github.com/yourusername/CaseComposer.git
cd CaseComposer
```

### 2. Compile the C++ Programs
```bash
g++-14 correct.cpp -o working.out
g++-14 wrong.cpp -o notworking.out
```

### 3. Run the Test Framework
```bash
python3 tester.py
```

Alternatively, you can use the shell script:
```bash
bash runCaseComposer.md
```

## How It Works
1. Generates test cases using `testCaseGenerator.py`.
2. Runs both `working.out` and `notworking.out` on the same test cases.
3. Compares the outputs and logs discrepancies in `wrongCases.csv`.
4. Displays the number of failed test cases and optionally prints them.

## Output Format
If discrepancies are found, they will be logged in `wrongCases.csv` as:
```
Test Case, Not Working Output, Expected Output
4 1\n10 2 3 3 9, Yes, No
10 1\n4 7 4 4 2 9 2 4 8 1, No, Yes
```
Additionally, if the user opts to view the incorrect cases, they are displayed as:
```
------------------------------------------------------------
| Wrong Output Number | Not Working Output | Expected Output |
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
