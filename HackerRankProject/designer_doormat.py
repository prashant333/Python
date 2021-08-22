"""
Hackerrank - Designer Door mat.

Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

1. Mat size must be N X M(N is an odd natural number, and M is 3 times N.)
2. The design should have 'WELCOME' written in the center.
3. The design pattern should only use |, . and - characters.
"""

N, M = map(int, input("Input the length and width of doormat: ").split())
for i in range(1, N, 2):
    print((i * ".|.").center(M, "-"))
print("WELCOME".center(M, "-"))
for i in range(N - 2, -1, -2):
    print((i * ".|.").center(M, "-"))

