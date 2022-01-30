# this program is used to demonstrate who has tweeted the most.

from collections import Counter

test_cases = int(input())
tweet_record = []            # a list variable to store the tweets.

for i in range(test_cases):
    total_record = int(input())
    for j in range(total_record):
        tweet_record.append(input())      # this is where the tweets will be appended in the list.

# we use list comprehension and split to take out the names of person tweeting.
name = [val.split()[0] for val in tweet_record]

# we use counter to count the total number of occurrence of person names
name_count = Counter(name)
x = name_count.most_common()[0]   # we take out the first name from the output in x
for i in x:                     # x is tuple and we use for loop to print out the output.
    print(i, end=" ")

"""
The code above only meets the below output. working on other test cases.
Sample 1:
Input 
1
4
sachin tweet_id_1
sehwag tweet_id_2
sachin tweet_id_3
sachin tweet_id_4

Output
sachin 3

"""
