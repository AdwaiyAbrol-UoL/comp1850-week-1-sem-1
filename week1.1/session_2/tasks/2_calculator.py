# Fill out the code to make a very simple calculator

# ask the user to enter number1:
try:
    num1=int(input("Kindly enter your first number:"))

# ask the user to enter number 2:
    num2=int(input("Kindly enter your second number:"))

# calculate the result of adding those numbers together
    answer= num1 + num2

# print out the answer
    print(f"You entered {num1} and {num2}, which when added together, give us {answer} as the final answer")
except:
    print("Please enter numbers only.")