# this program is used to demonstrate who has tweeted the most.

from collections import Counter

n = int(input())
tweet_record = []
for i in range(n):
    total_record = int(input())
    for j in range(total_record):
        tweet_record.append(input())

name = [val.split()[0] for val in tweet_record]
name_count = Counter(name)
x = name_count.most_common()[0]
for i in x:
    print(i, end=" ")

"""
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


