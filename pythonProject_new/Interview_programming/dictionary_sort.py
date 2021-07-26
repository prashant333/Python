# This program demonstrate sorting of dictionary.

def dictionary_sort(d):
    print("Keys and Values sorted in the given dictionary is given as: ")
    for i in sorted(d, reverse=True):
        print((i, d[i]), end=" ")


input_dictionary = {3: "how", 2: "are", 1: "you"}
dictionary_sort(input_dictionary)
