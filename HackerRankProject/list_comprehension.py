"""
 You are given three integers x,y and z representing the dimensions of a cuboid along with an integer n.
 Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n.
"""

X = int(input("Please enter x:"))
Y = int(input("Please enter y:"))
Z = int(input("Please enter z:"))
n = int(input("Enter integer value n:"))
list_comp = [(x, y, z) for x in range(X+1) for y in range(Y+1) for z in range(Z+1) if x+y+z != n]
print(list_comp)
