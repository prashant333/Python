# More than 2 lines will result in 0 score. Do not leave a blank line also
"""
for i in range(1, int(input())):
    print('{}'.format(i) * i)
"""

# OR
# this solution assumes that the entered value will be between 1 to 9.
for i in range(1, int(input())):
    print([0, 1, 22, 333, 4444, 55555, 666666, 7777777, 88888888, 999999999][i])
