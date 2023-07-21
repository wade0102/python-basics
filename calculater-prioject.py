# A simple calculator app in Python

# Define the operations
def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  return x / y

# Print the menu
print("Select an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Take the user input
choice = input("Enter your choice (1/2/3/4): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform the calculation and print the result
if choice == "1":
  print(num1, "+", num2, "=", add(num1, num2))
elif choice == "2":
  print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == "3":
  print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == "4":
  print(num1, "/", num2, "=", divide(num1, num2))
else:
  print("Invalid input")
