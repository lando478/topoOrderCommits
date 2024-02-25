# !/usr/local/cs/bin/python3
print("hello world")

# Once the script finishes executing, if you check the working directory in your shell or environment, it will remain in its original directory, unaffected by the change made within the script. If you want to persistently change the working directory, you would need to use shell commands or manually change it after running the script.
# Use Python's os module to interact with the filesystem.
import os
#test
try:
    os.mkdir('trial_run')  # Try to create the directory
    print("Directory 'trial_run' created successfully.")
except FileExistsError:
    print("Directory 'trial_run' already exists.")

try:
    os.chdir('trial_run')  # Try to change the working directory
     # Open the file in read mode to read its contents
    with open('test_file.txt', 'w') as f:
        f.write("hello world")

    with open('test_file.txt', 'r') as f:
        file_contents = f.read()
        print("Contents of the file:")
        print(file_contents)

    
      
    print("Changed working directory to 'trial_run'.")
except FileNotFoundError:
    print("Directory 'trial_run' does not exist.")
except PermissionError:
    print("Permission denied to change directory to 'trial_run'.")


# Start from the current directory and use os.path functions to check if .git exists.
# If not found, move up to the parent directory and repeat the process until .git is found or the root directory is reached.
# Print the path to the top-level Git directory when found.
# If .git cannot be found up to the root directory, print "Not inside a Git repository" to standard error and exit with status code 1.

