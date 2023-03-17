# Find the contiguous sub array within a 1D array with higest sum.

def findSum(l):
    x =[[]]
    maxi = []

    # we will create all possible contiguous subarray using the loops below
    for i in range(len(l)+1):
        for j in range(i):
            x.append(l[j:i])

    # finding the sum of all the subarray 
    for i in x:
        maxi.append(sum(i))
    print("Largest sum of subarray is: ",max(maxi))

    # we will then find which subarray sum is equal to the max sum found 
    for i in x:
        if sum(i) == max(maxi):
            print("Largest contiguous subarray is: ",i)


l1 = [-2, -3, 4, -1, -2, 1, 5, -3]
findSum(l1)