
def sort_marksheet(nested_list):

    return sorted(nested_list, key= lambda x: x[1])
marksheet = []
for _ in range(0, int(input())):
    marksheet.append([input(), float(input())])

print(sort_marksheet(marksheet))

"""
    # this could be one way of taking input as nested list 
    marksheet = [[input(), float(input())] for _ in range(int(input()))]
    print(marksheet)
"""

