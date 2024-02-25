# !/usr/local/cs/bin/python3
import os

#to run in other directories: python3 /Users/daydreamer/Desktop/CS35L/Assignment5/topoOrderCommits/topo_order_commits.py 

# Once the script finishes executing, if you check the working directory in your shell or environment, it will remain in its original directory, unaffected by the change made within the script. If you want to persistently change the working directory, you would need to use shell commands or manually change it after running the script.

# Start from the current directory and use os.path functions to check if .git exists
current_directory = os.getcwd()
while True:
      git_directory = os.path.join(current_directory, '.git')
      if os.path.exists(git_directory) and os.path.isdir(git_directory):
            print(".git directory exists in the current directory path:\n" + git_directory)
            break
      else:
            parent_directory = os.path.dirname(current_directory)
            # perform check to see if parent equals the current then we are at the end of check. 
            if parent_directory == current_directory:
                  print("Reached root direcrotory. .git directory not found")
                  break
            else:
                  current_directory = parent_directory

# If not found, move up to the parent directory and repeat the process until .git is found or the root directory is reached.
# Print the path to the top-level Git directory when found.
# If .git cannot be found up to the root directory, print "Not inside a Git repository" to standard error and exit with status code 1.

