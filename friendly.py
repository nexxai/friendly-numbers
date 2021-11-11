# friendly.py - v1.0
# 
# Usage: python3 friendly.py
#
# Check for friendly numbers as described here: https://www.youtube.com/watch?v=KZ1BVlURwfI
# 
# Features:
# - Checkpoint saving so the script can be exited and resumed with little loss of work
# 
# To-Do:
# - Multithreading?
# - Use shaders for calculations?

from datetime import datetime
from sympy import divisors
from functions import find_index
import sys, os, re

# SETTINGS
index_search = 10                       # Get the index of '10'
where_to_start = 10**12                 # 1 trillion
where_to_end = 10**13                   # 10 trillion (e.g. search from 1 trillion to 10 trillion)
checkpoint = 10**4                      # Update the checkpoint after how many checks?
progress_file_name = "progress.txt"     # Name of the checkpoint file

# See if there's a progress file...
if os.path.isfile(progress_file_name):
    # If so, open it...
    progress_file = open(progress_file_name, "r")
    if progress_file.mode == 'r':
        # and get the current checkpoint
        start_num = progress_file.read()
        
        # If it contains the text 'FOUND' just print it out and exit
        match = re.search(r"FOUND:\s(\d{1,})", start_num)
        if match:
            print(start_num)
            print(divisors(int(match.group(1))))
            sys.exit()
        # Otherwise we're loading in that checkpoint
        start_num = int(start_num)
else:
    # No progress file found, so just start at the beginning
    start_num = where_to_start

# Find the index of the provided integer
# (The [0] is because find_index returns 3 values, we only want the first)
search = find_index(index_search)[0]

# Just start looping through each number, one by one
for num in range(start_num, where_to_end):
    # Destructure find_index into its appropriate variables
    index, sum_of_factors, factors = find_index(num)

    # If it matches index_search, we found one so break out of the loop
    if index == search:
        print(f'{sum_of_factors} / {num} = {index}')
        print(factors)
        break

    # Just give the user some visual feedback that we haven't stalled
    # so every [checkpoint] numbers we check, show the status on the screen
    if num % checkpoint == 0:
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        print(f'[{current_time}] Working on: {num}')
        print(f'{sum_of_factors} / {num} = {index}')
        print(factors)

        # And update the checkpoint file
        progress = open(progress_file_name, "w")
        progress.write(str(num))
        
# We found one so update the checkpoint file with the details
print('FOUND ONE!')
progress = open(progress_file_name, "w")
progress.write(f'FOUND: {str(num)}')
