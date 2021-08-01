# Hackerrank challenge.
import collections

numShoes = int(input())
# using counter to count the different size of shoes available in shop
shoes = collections.Counter(map(int, input().split()))
# takes input for number of customers
numCust = int(input())

income = 0

for i in range(numCust):
    # taking input for size requirement by the customer and price of the shoe.
    size, price = map(int, input().split())
    if shoes[size]:
        income += price
        shoes[size] -= 1

print(income)

