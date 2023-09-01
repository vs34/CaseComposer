import os
import platform
import subprocess
n = 0
OS = platform.system()
with open("tc1.csv", "w") as opfile:
    pass

# Create the output file with headers
with open("tc1.csv", "w") as opfile:
    opfile.write("test case, not working output, working output"))
    
nooftc = int(input("Number of test case to check (integer) : ")
for a in range(nooftc):
    # Read the multi-line input from tc.py
    input_data = subprocess.run(["python3", "tc.py"], stdout=subprocess.PIPE, text=True).stdout
    print(a)
# Run the input data through working.out and store the output
    if OS == 'Windows':
        working_output = subprocess.check_output(["./working.exe"], input=input_data, text=True).replace("\n", " ")
        not_working_output = subprocess.check_output(["./notworkin.exe"], input=input_data, text=True).replace("\n", " ")
        
    else :
        working_output = subprocess.check_output(["./working.out"], input=input_data, text=True).replace("\n", " ")
        not_working_output = subprocess.check_output(["./notworkin.out"], input=input_data, text=True).replace("\n", " ")

# Run the input data through notworking.out and store the output
    # print(not_working_output,working_output)
    # print(not_working_output==working_output)
# Write the output to separate files
    with open("tc1.csv", "a") as opfile:
        if working_output != not_working_output:
            opfile.write("{} ,{} ,{} \n".format(input_data.strip(), not_working_output.strip(), working_output.strip()))
            opfile.write("++++++++++++++++++++++++++++++++++++++++++++++\n")
            n += 1

# Print the number of failed test cases
print("Number of failed TC = ", n)
