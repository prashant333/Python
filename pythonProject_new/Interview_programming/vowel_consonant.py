# separate the vowel and consonant from a given string.

def vowelConsonant(s):
    vow = []
    con = []
    for i in enumerate(s):
        if (i[1] == 'A' or i[1] == 'a' or i[1] == 'E' or i[1] == 'e' or i[1] == 'I'
                or i[1] == 'i' or i[1] == 'O' or i[1] == 'o' or i[1] == 'U' or i[1] == 'u'):
            vow.append(i[1])
        else:
            con.append(i[1])
    print(vow)
    print(con)


vowelConsonant("howareyou")
