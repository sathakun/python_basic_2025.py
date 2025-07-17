# Sample: Using the math library in Python
import math

# 1. Square root
num = 16
print("Square root of", num, "is", math.sqrt(num))

# 2. Power
base = 2
exp = 8
print(f"{base} to the power of {exp} is", math.pow(base, exp))

# 3. Trigonometric functions
angle_deg = 45
angle_rad = math.radians(angle_deg)
print(f"sin({angle_deg}) =", math.sin(angle_rad))
print(f"cos({angle_deg}) =", math.cos(angle_rad))
print(f"tan({angle_deg}) =", math.tan(angle_rad))

# 4. Constants
print("Pi:", math.pi)
print("Euler's number (e):", math.e)

# 5. Logarithm
print("log(100, 10):", math.log(100, 10))
print("ln(10):", math.log(10))

# 6. Factorial
print("Factorial of 5:", math.factorial(5))

# 7. Ceiling and Floor
num2 = 3.7
print("Ceiling of", num2, ":", math.ceil(num2))
print("Floor of", num2, ":", math.floor(num2))
