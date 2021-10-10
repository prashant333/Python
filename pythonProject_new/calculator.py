def cal(val1, val2, operator):
    if operator == "+":
        return val1+val2
    elif operator == "-":
        return val1-val2
    elif operator == "*":
        return val1*val2
    elif operator == "/":
        return val1 / val2
    else:
        print("incorrect operation")

# this is comment


value1 = input("Enter first number: ")
value2 = input("Enter second number: ")
op = input("Enter operation to perform: ")
print(cal(float(value1), float(value2), op))
