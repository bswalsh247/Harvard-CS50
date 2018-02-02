# Let’s implement structures in Python:

import cs50
from student import Student

students = [] 
for i in range(3):

    print("name: ", end="")
    name = cs50.get_string()

    print("dorm: ", end="")
    dorm = cs50.get_string()

    students.append(Student(name, dorm)) # this is similar to malloc in C. This automatically stores name and dorm somewhere inside of this structure and svae permanantly in what are called instant variables inside of self. self just reffers to the object that has been allocated 

for student in students:
    print("{} is in {}.".format(student.name, student.dorm))


# First, we declare a student file that we’ll soon write, and import the Student class from it.

# Then we can create an empty list to store students called students, 
# which we can add or remove things to.

# Then we get a name and dorm, create a Student objects by passing those strings 
# in as arguments, and append it, or add it, to the end of our list students. 
# (Lists, too, have built-in functionality, one of which is append.)

# Finally, for each student, we print the properties back with the . syntax.

# C
# And we’ll learn one new keyword to easily represent this, a struct. We can create a more complicated data type and name it:

typedef struct
{
    string name;
    string dorm;
}
student;

# To represent a student, we can include two pieces of information, string name 
# and string dorm.

# And we can use this container like so:

#include <cs50.h>
#include <stdio.h>
#include <string.h>

#include "structs.h"

#define STUDENTS 3

int main(void)
{
    student students[STUDENTS];

    for (int i = 0; i < STUDENTS; i++)
    {
        printf("name: ");
        students[i].name = get_string();

        printf("dorm: ");
        students[i].dorm = get_string();
    }

    for (int i = 0; i < STUDENTS; i++)
    {
        printf("%s is in %s.\n", students[i].name, students[i].dorm);
    }
}

# We can create an array of student structs called students, with STUDENTS number of elements.

# We used #define STUDENTS 3 to set a constant, STUDENTS, to the value 3. This prevents having 
# to make a variable that might otherwise be changed.

# Then we can access properties in the structs with syntax like students[i].name, since 
# students is an array and students[i] gets an individual student struct for us to use.

# We can even open a file in C and use it with our structs:

#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "structs.h"

#define STUDENTS 3

int main(void)
{
    student students[STUDENTS];

    for (int i = 0; i < STUDENTS; i++)
    {
        printf("name: ");
        students[i].name = get_string();

        printf("dorm: ");
        students[i].dorm = get_string();
    }

    FILE *file = fopen("students.csv", "w");
    if (file != NULL)
    {
        for (int i = 0; i < STUDENTS; i++)
        {
            fprintf(file, "%s,%s\n", students[i].name, students[i].dorm);
        }
        fclose(file);
    }
}


# Here we are using the FILE type, part of C, and a library function fopen, 
# that allows us to open files. "w" allows us to write to the file.

# After we use fprintf, another library function to write to the file, we close the file.



