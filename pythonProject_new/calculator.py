def cal(val1, val2, operator):
    if operator == "add":
        return val1+val2
    elif operator == "sub":
        return val1-val2
    elif operator == "mul":
        return val1*val2
    elif operator == "div":
        return val1 / val2
    else:
        print("incorrect operation")

# this is comment


value1 = input("Enter a number:")
value2 = input("Enter second number:")
op = input("Enter operator as 'add', 'sub', 'mul', 'div':")
print(cal(float(value1), float(value2), op))
