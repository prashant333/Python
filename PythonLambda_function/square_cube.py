"""
This program demonstrates the use of lambda function to calculate square and cube of given list.
"""
numbers = [1, 4, 54, 34, 23, 78]
cube = list(map(lambda x: x**3, numbers))
squ = list(map(lambda x: x**2, numbers))
print("cube of numbers: ", cube, "square of numbers: ", squ)
