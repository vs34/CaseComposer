import os
import platform
import subprocess
import sys

def update_progress_bar(iteration, total, length=50):
    """Displays a progress bar in the terminal."""
    if total == 0:  # Prevent division by zero
        return
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

try:
    nooftc = int(input("Number of test cases to check (integer): "))
except ValueError:
    print("Invalid input! Please enter an integer.")
    sys.exit(1)

for a in range(nooftc):
    # Run the test case generator script (with a timeout)
    try:
        input_data = subprocess.run(
            ["python3", "tc.py"], stdout=subprocess.PIPE, text=True, timeout=10
        ).stdout
    except subprocess.TimeoutExpired:
        print("\nError: `tc.py` took too long to generate test cases!")
        sys.exit(1)
    except FileNotFoundError:
        print("\nError: `tc.py` not found!")
        sys.exit(1)

    # Update progress bar
    update_progress_bar(a + 1, nooftc)

    # Check if the required executables exist
    if OS == 'Windows':
        working_exe = "working.exe"
        not_working_exe = "notworking.exe"
    else:
        working_exe = "./working.out"
        not_working_exe = "./notworking.out"

    if not os.path.exists(working_exe):
        print(f"\nError: {working_exe} not found!")
        sys.exit(1)

    if not os.path.exists(not_working_exe):
        print(f"\nError: {not_working_exe} not found!")
        sys.exit(1)

    # Run both versions and compare outputs
    try:
        working_output = subprocess.check_output(
            [working_exe], input=input_data, text=True, timeout=5
        ).replace("\n", " ")
        not_working_output = subprocess.check_output(
            [not_working_exe], input=input_data, text=True, timeout=5
        ).replace("\n", " ")
    except subprocess.TimeoutExpired:
        print("\nError: One of the executables took too long to run!")
        sys.exit(1)
    except subprocess.CalledProcessError:
        print("\nError: One of the executables failed to run properly!")
        sys.exit(1)

    # Write the output to CSV if there is a difference
    with open("tc1.csv", "a") as opfile:
        if working_output != not_working_output:
            wrong_op += 1
            print(f"\nWrong output number {wrong_op}")
            print(f"{input_data.strip()} , {not_working_output.strip()} , {working_output.strip()} \n")
            opfile.write(f"{input_data.strip()} , {not_working_output.strip()} , {working_output.strip()} \n")
            opfile.write("++++++++++++++++++++++++++++++++++++++++++++++\n")
            n += 1

# Print the number of failed test cases
print(f"\nNumber of failed TC = {n}")