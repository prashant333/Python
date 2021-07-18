#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.

def gradingStudent(grades):
    for i in range(len(grades)):
        if grades[i] >= 38:
            if 5 - (grades[i] % 5) < 3:
                grades[i] = grades[i] + (5 - grades[i] % 5)
    return grades


if __name__ == '__main__':
    total = int(input().strip())
    grades = []

    for _ in range(total):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudent(grades)
    print(result)
