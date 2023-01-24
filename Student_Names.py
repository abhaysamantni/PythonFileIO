s = open('studentnames.txt', 'r')
numStudents = 0
for student in s:
    name = student.rstrip('\n')
    if len(name) > 0:
        print(name)
        numStudents += 1
print("There were " + str(numStudents) + " students in the file.")
# print(s.readline().rstrip('\n'))
# print(s.readline().rstrip('\n'))
# print(s.readline().rstrip('\n'))
# print(s.readline().rstrip('\n'))
# print(s.readline().rstrip('\n'))
# print(s.readline().rstrip('\n'))

s.close()