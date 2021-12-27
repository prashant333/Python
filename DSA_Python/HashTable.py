# Hash table implementation using python

class HashTable:
    def __init__(self):
        # we can take max value for array size as input the user as well.
        self.Max = 50
        self.table = [None] * self.Max

    def cal_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
            return h % self.Max

    # we use the inbuilt python operator for setting items
    def __setitem__(self, key, value):
        h = self.cal_hash(key)
        self.table[h] = value

    # we use the inbuilt python operator for getting items
    def __getitem__(self, key):
        h = self.cal_hash(key)
        return self.table[h]


t = HashTable()
t["march 1"] = 320
t["march 2"] = 300
print(t["march 1"])
