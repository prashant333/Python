# creating dictionary from user input and finding percentage of a student.

n = int(input("Enter total number of values:"))
student_list = {}
for _ in range(n):
    name, *lines = input("Enter values:").split() # *lines, here * is used to store the rest of input in variable named lines.
    score = list(map(float, lines))
    student_list[name] = score

query_name = input("Enter student name: ")
total_marks = sum(student_list[query_name])
average = total_marks/3
print("%.2f"%(average)) # here "%.2f"% is a format specifier.

