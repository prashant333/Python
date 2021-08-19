# program to check if the given string is palindrome or not.

def palindrome(s):
    s1 = s[::-1]
    if s == s1:
        return "given Value is palindrome"
    else:
        return "Not a palindrome"


w = input("Enter a string or number value: ")
print(palindrome(w))
