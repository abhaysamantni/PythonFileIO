
class_data = open('ClassList.txt', 'w')
for classes in range(3):
   class_name = input("Please enter a class (e.g. MIS 304): ")
   class_data.write(class_name + "\n")
class_data.close()

