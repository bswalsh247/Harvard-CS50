# We can see another convenient feature:

import cs50
import csv
from student import Student

students = []
for i in range(3):

    print("name: ", end="")
    name = cs50.get_string()

    print("dorm: ", end="")
    dorm = cs50.get_string()

    students.append(Student(name, dorm))

file = open("students.csv", "w")
writer = csv.writer(file)
for student in students:
    writer.writerow((student.name, student.dorm))
file.close()

# Now, instead of printing the students to the screen, we can write them to a 
# file students.csv by opening it and using a built-in module, csv, that writes 
# comma-separated values files.

# With csv.writer(file), we pass in the file we open to get back a writer object 
# that will take in tuples, and write them to the file for us with just writerow.

# If we were to run this program without import csv, the interpreter would start 
# the input, collecting input like name and dorm and creating students, but only 
# when it reaches the line that calls for csv will it notice that it wasn’t defined, 
# and raise an exception (stop the program because there is an error).