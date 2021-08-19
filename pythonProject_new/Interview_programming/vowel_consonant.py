# separate the vowel and consonant from a given string.

def vowelConsonant(s):
    vow = []
    con = []
    for i in range(len(s)):
        if (s[i] == 'A' or s[i] == 'a' or s[i] == 'E' or s[i] == 'e' or s[i] == 'I'
                or s[i] == 'i' or s[i] == 'O' or s[i] == 'o' or s[i] == 'U' or s[i] == 'u'):
            vow.append(s[i])
        else:
            con.append(s[i])
    print(vow)
    print(con)


vowelConsonant("howareyou")
