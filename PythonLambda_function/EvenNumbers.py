# This set of code demonstrates the use of lambda function to obtain even numbers from a set of given list.

def FindEven(given_list):
    return list(filter(lambda x: x % 2 == 0, given_list))


unsorted_list = list(map(int, input("Enter the list values to be sorted: ").split()))
print(FindEven(unsorted_list))
