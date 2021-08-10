# This program uses recursive method to find the power a given number

def power(x,n):
    if n == 0:
        return 1
    else:
        return x*power(x, n-1)


x = int(input("Enter value of base: "))
n = int(input("Enter value of exponent: "))
print(power(x,n))