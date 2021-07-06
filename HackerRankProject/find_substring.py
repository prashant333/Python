def count_sub(string, sub_string):
    occ = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            occ += 1
    return occ


if __name__ == '__main__':
    String = input().strip()
    sub_string = input().strip()

    count = count_sub(String, sub_string)
    print(count)