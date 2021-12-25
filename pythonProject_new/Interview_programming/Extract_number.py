# getting numbers from string
# using List comprehension + isdigit() +split()

# initializing string
test_string = "There are 2 apples for 4 persons"

# printing original string
print("The original string : " + test_string)

# using List comprehension + isdigit() +split()
# getting numbers from string
res = [int(i) for i in test_string.split() if i.isdigit()]

# print result
print("The numbers list is : " + str(res))

# this can also be done using python regex, we can use the findall
# function to check for the numeric occurrences using matching regex string.
