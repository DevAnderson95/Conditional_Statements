# Task 1: Identify The Greatest
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
num3 = int(input("Enter your third number: "))

if num1 >= num2 and num1 >= num3:
    greatest = num1 
    print(f"The greatest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    greatest = num2
    print(f"The greatest number is:", num2)
else:
    greatest = num3
    print(f"The greatest number is:", num3)

# Task 2: Identify the smallest 

if num1 <= num2 and num1 <= num3:
    smallest = num1
    print(f"The smallest number is: ", num1 )
elif num2 <= num1 and num2 <= num3:
    smallest = num2
    print("The smallest number is: ", num2)
else:
    smallest = num3
    print("The smallest number is: ", num3)

    

