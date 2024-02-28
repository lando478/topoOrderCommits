# !/usr/local/cs/bin/python3
import os
import sys



'''
1. Start from the current directory. Begin a while loop, checking if the current directory contains a .git directory. 
If true, return True. Otherwise, update the current directory with its parent and check if the parent directory is equal to the current directory. If they are the same, return False because we have reached the root of the file system.
'''
def find_git_directory():
    current_directory = os.getcwd()
    return_statement = False
    while True:
        git_directory = os.path.join(current_directory, '.git')
        if os.path.exists(git_directory) and os.path.isdir(git_directory):
            # print(".git directory exists in the current directory path:\n" + git_directory)
            return git_directory
        else:
            parent_directory = os.path.dirname(current_directory)
            if parent_directory == current_directory:
                # Reached root directory
                sys.stderr.write("Not inside a Git repository\n")
                sys.exit(1)  # Exit with status 1
            else:
                current_directory = parent_directory


#one directory or one file
#we dont have to worrry about multiple files in one directory in git. #file is the commit head hash for the branch. If two files, it would be two branches. 
#utilize file command to find what a file is!
                #branches with two slash are not valiid : a//b
#Helper function to work with branches with /. 
def check_for_file(directory, branch_name=""):
    entries = os.listdir(directory)
    for entry in entries:
        entry_path = os.path.join(directory, entry)
        # Construct the full branch name
        full_branch_name = os.path.join(branch_name, entry) if branch_name else entry
        # Check if the entry is a file containing ASCII text
        if os.path.isfile(entry_path) and os.path.splitext(entry)[1] == '.txt':
            print("ASCII text file:", full_branch_name)
        elif os.path.isfile(entry_path):
            print("Non-ASCII text file:", full_branch_name)
        # Check if the entry is a directory and recursively explore it
        elif os.path.isdir(entry_path):
            check_for_file(entry_path, full_branch_name)
        else:
            print("Unknown type:", full_branch_name)

def get_Branches():
    git_directory = find_git_directory()
    if git_directory:
        git_refs_directory = os.path.join(git_directory, 'refs/heads')  # Path to the 'refs' directory inside the Git directory
        os.chdir(git_refs_directory) 
        check_for_file(git_refs_directory)
    else:
        print("Git directory not found.")
                  
                      
# git_dir = find_git_directory()


# If not found, move up to the parent directory and repeat the process until .git is found or the root directory is reached.
# Print the path to the top-level Git directory when found.
# If .git cannot be found up to the root directory, print "Not inside a Git repository" to standard error and exit with status code 1.


if __name__ == "__main__":
      # perform function calls    
      get_Branches()