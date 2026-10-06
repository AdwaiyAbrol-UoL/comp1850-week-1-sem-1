# Worksheet 1.2: Task 1 Solution

import sys

try:
    grade = int(input("Enter your integer grade from 0 to 100:"))
except:
    sys.exit("Error: Grade must be an integer between 0 and 100")


if not 0<=grade<=100:
    sys.exit("Error: Grade must be an integer between 0 and 100")


if grade >= 70:
    result = "Distinction"
elif grade >= 40:
    result = "Pass"
else:
    result = "Fail"

print(f"{grade} is a {result}")