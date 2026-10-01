# To test that you can successfully download a file and upload it to gradescope

# You are going to write a very simple program:

# Ask a user to enter two numbers (one per input)
try:
    num1=int(input("Kindly enter your first number:"))
    num2=int(input("Kindly enter your second number:"))
    

# print out the answer
    print(f"You entered {num1} and {num2}, which when added together, give us {answer} as the final answer")
except:
    print("Please enter numbers only.")
# multiply those numbers together
    answer= num1 * num2
# print out the result
    print(f"You entered {num1} and {num2}, which when added together, give us {answer} as the final answer")
# There is an extra point available for validating that they entered numbers!
# Add to your code so that if they entered something other than an integer it prints
# 'That is not a number' and exits.
except:
    print("That is not a number")

# Download your file, and upload it to the 'Week 1 Session 2 - Practice Upload' task on Minerva.
# You will get some feedback - ensure you are passing the tests!