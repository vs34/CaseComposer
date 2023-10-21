import os
import platform
import subprocess

n = 0
OS = platform.system()

# Open the CSV file in append mode with the right headers
with open("tc1.csv", "w") as opfile:
    opfile.write("test case, not working output, working output\n")

nooftc = int(input("Number of test cases to check (integer): "))

for a in range(nooftc):
    # Read the multi-line input from tc.py
    input_data = subprocess.run(
        ["python3", "tc.py"], stdout=subprocess.PIPE, text=True).stdout
    print(a)

    # Run the input data through working.out and notworking.out and store the outputs
    if OS == 'Windows':
        working_output = subprocess.check_output(
            ["./working.exe"], input=input_data, text=True).replace("\n", " ")
        not_working_output = subprocess.check_output(
            ["./notworking.exe"], input=input_data, text=True).replace("\n", " ")
    else:
        working_output = subprocess.check_output(
            ["./working.out"], input=input_data, text=True).replace("\n", " ")
        not_working_output = subprocess.check_output(
            ["./notworking.out"], input=input_data, text=True).replace("\n", " ")

    # Write the output to separate files
    with open("tc1.csv", "a") as opfile:
        if working_output != not_working_output:
            opfile.write("{} ,{} ,{} \n".format(input_data.strip(),
                                                not_working_output.strip(), working_output.strip()))
            opfile.write("++++++++++++++++++++++++++++++++++++++++++++++\n")
            n += 1

# Print the number of failed test cases
print("Number of failed TC =", n)
