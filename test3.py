
IsTrue = True
x = 5
user = input("What is your name?: ")
print("Hello, " + user + "! ")
while IsTrue:
    answer = int(input("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n:"))
    if answer == 1:
        addition = int(input("How much are you gonna add? "))
        x = x + addition
        print(f"Total sum is {x}")
    elif answer == 2:
        subtraction = int(input("How much are you gonna subtract?: "))
        x = x - subtraction
        print(f"The total difference is {x}")
    elif answer == 3:
        multiplication = int(input("How much are you gonna multiply?: "))
        x = x * multiplication
        print(f"The total product is {x}")
    else:
        division = int(input("How much are you gonna divide?: "))
        x = x / division
        print(f"Here is the total quotient: {x}")
        IsTrue = False
"""
def addition(num1, num2):
    add = num1 + num2
    return add

num1, num2 = input("Enter two numbers separated by a space: ").split()
num1 = int(num1)
num2 = int(num2)

result = addition(num1, num2)
print("The sum is:", result)
"""





