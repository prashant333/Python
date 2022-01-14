# Hackerrank problem to find captions room.
from collections import Counter

k = int(input())
rooms = list(map(int, input().split()))

# We use the counter to count total number of rooms entries.
rooms_1 = Counter(rooms)

# Room entry that is exactly one is the caption's room.
for x, y in rooms_1.items():
    if y == 1:
        print("Caption's room is room number: ", x)
