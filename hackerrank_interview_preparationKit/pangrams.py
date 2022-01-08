# A pangram is a string that contains every letter of the alphabet.
# this program determines if a given string is pangram or not.

def pangram(s):
    # set only contains unique values, if the same value is passed on twice, set considers that value only once.
    # we use replace method to remove any space, if present in the input string.
    return "Pangram" if len(set(s.replace(" ", '').lower())) == 26 else "not pangram"


input_string = input("Inter a string: ")
print(pangram(input_string))
