import os
import platform
import subprocess

import sys


def update_progress_bar(iteration, total, length=50):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = '█' * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\rProgress: |{bar}| {percent}% Complete')
    sys.stdout.flush()


n = 0
OS = platform.system()
wrong_op = 0

# Open the CSV file in append mode with the right headers
with open("tc1.csv", "w") as opfile:
    opfile.write("test case, not working output, working output\n")

nooftc = int(input("Number of test cases to check (integer): "))

for a in range(nooftc):
    # Read the multi-line input from tc.py
    input_data = subprocess.run(
        ["python3", "tc.py"], stdout=subprocess.PIPE, text=True).stdout
    # print(a)
    update_progress_bar(a, nooftc)

    # Run the input data through working.out and notworking.out and store the outputs
    if OS == 'Windows':
        working_output = subprocess.check_output(
            ["./working.exe"], input=input_data, text=True).replace("\n", " ")
        not_working_output = subprocess.check_output(
            ["./notworking.exe"], input=input_data, text=True).replace("\n", " ")
    else:
        working_output = subprocess.check_output(
            ["./workin.out"], input=input_data, text=True).replace("\n", " ")
        not_working_output = subprocess.check_output(
            ["./notworkin.out"], input=input_data, text=True).replace("\n", " ")

    # Write the output to separate files
    with open("tc1.csv", "a") as opfile:
        if working_output != not_working_output:
            wrong_op += 1
            print("wrong output number", wrong_op)
            print("{} ,{} ,{} \n".format(input_data.strip(),
                                         not_working_output.strip(), working_output.strip()))
            opfile.write("{} ,{} ,{} \n".format(input_data.strip(),
                                                not_working_output.strip(), working_output.strip()))
            opfile.write("++++++++++++++++++++++++++++++++++++++++++++++\n")
            n += 1

# Print the number of failed test cases
print("\nNumber of failed TC =", n)
