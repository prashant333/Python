# Write a program to compute the product of two positive number without using multiplication.

def twonumber(a, b):
    product = 0
    for i in range(b):
        product += a
    return product


print(twonumber(3, 98))
