if __name__ == '__main__':
    n = int(input())
    mark_sheet = [[input(), float(input())] for _ in range(n)]
    print(mark_sheet)

second_lowest = sorted(list(set([marks for name, marks in mark_sheet])))
print('\n'.join([a for a, b in sorted(mark_sheet) if b == second_lowest]))

