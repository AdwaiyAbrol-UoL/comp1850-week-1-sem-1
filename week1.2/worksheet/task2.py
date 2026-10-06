# Worksheet 1.2: Task 2 Solution

import sys
from util import read_numbers

numbers = read_numbers()

if len(numbers) == 0:
    sys.exit("Error: no numbers provided")

minimum_num = min(numbers)
maximum_num = max(numbers)
mean_num = sum(numbers)/len(numbers)

mid_num = len(numbers)//2
numbers.sort()

if len(numbers) % 2 == 0:
    median_num = (numbers[mid_num - 1] + numbers[mid_num]) /2 
else:
    median_num = numbers[mid_num]

print(f"Minimum = {minimum_num}")
print(f"Maximum = {maximum_num}")
print(f"Mean = {mean_num}")
print(f"Median = {median_num}")