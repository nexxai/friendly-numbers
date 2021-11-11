# friendly.py - v1.0
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
import sys, os

index_search = 1.8          # This is the index of '10'
where_to_start = 10**12     # 1 trillion
where_to_end = 10**13       # 10 trillion (e.g. search from 1 trillion to 10 trillion)

# See if there's a progress file...
progress_file_name = "progress.txt"
if os.path.isfile(progress_file_name):
    # If so, open it...
    progress_file = open(progress_file_name, "r")
    if progress_file.mode == 'r':
        # and get the current checkpoint
        start_num = progress_file.read()
        
        # If it contains the text 'FOUND' just print it out and exit
        if start_num.startswith('FOUND'):
            print(start_num)
            print(divisors(start_num))
            sys.exit()
        # Otherwise we're loading in that checkpoint
        start_num = int(start_num)
else:
    # No progress file found, so just start at 1 trillion
    start_num = where_to_start

# Just start looping through each number, one by one
for num in range(start_num, where_to_end):
    # Get each of the factors from the current number
    factors = divisors(num)

    # Initialize the counter
    sum_of_factors = 0
    # and then add the factors together
    for factor in factors:
        sum_of_factors += factor

    # Calculate the index by dividing the sum of the factors by the number we're working on
    index = sum_of_factors / num

    # If it matches index_search, we found one so break out of the loop
    if index == index_search:
        print(f'{sum_of_factors} / {num} = {index}')
        print(factors)
        break

    # Just give the user some visual feedback that we haven't stalled
    # so every 10000 numbers we check, show the status on the screen
    if num % 10**4 == 0:
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
