# Lab: Python Variables

# 1. Create variables of different types
integer_var = 10           # integer
decimal_var = 3.14         # float
string_var = "Hello, Python!"  # string
boolean_var = True         # boolean
complex_var = 2 + 3j       # complex

# 2. Print the variables
print("Integer:", integer_var)
print("Float:", decimal_var)
print("String:", string_var)
print("Boolean:", boolean_var)
print("Complex:", complex_var)

# 3. Change the value of a variable
integer_var = 20
print("Updated Integer:", integer_var)

# 4. Use input to get a variable from the user
user_name = input("Enter your name: ")
print("Hello,", user_name)

# 5. Demonstrate variable naming conventions
snake_case_var = 100
CamelCaseVar = 200
print("snake_case_var:", snake_case_var)
print("CamelCaseVar:", CamelCaseVar)

# 6. Show type conversion
num_str = "123"
num_int = int(num_str)
print("String to int:", num_int)

# 7. Use type() to display variable types
print("Type of integer_var:", type(integer_var))
print("Type of decimal_var:", type(decimal_var))
print("Type of string_var:", type(string_var))
print("Type of boolean_var:", type(boolean_var))
print("Type of complex_var:", type(complex_var))
