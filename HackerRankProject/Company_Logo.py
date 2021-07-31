"""
A newly opened multinational brand has decided to base their company logo on the three most common characters
in the company name. They are now trying out various combinations of company names and logos based on this
condition. Given a string s, which is the company name in lowercase letters, your task is to find the top three
most common characters in the string.
"""

if __name__ == '__main__':
    s = input("Enter company name: ")

    Dict = {}
    for x in sorted(s):
        Dict[x] = Dict.get(x, 0) + 1
        # Sorting Dict by value & storing sorted keys in Dict_keys.
    Dict_keys = sorted(Dict, key=Dict.get, reverse=True)

    for key in Dict_keys[:3]:
        print(key, Dict[key])


