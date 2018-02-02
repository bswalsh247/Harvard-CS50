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
// Here we are using the FILE type, part of C, and a library function fopen, 
// that allows us to open files. "w" allows us to write to the file.
    FILE *file = fopen("students.csv", "w");
    if (file != NULL) // make sure nothing goes wrong for example, you don't have permissions to create files or the computer doens't have enough space to create a file
    {
        for (int i = 0; i < STUDENTS; i++) // do this three times.
        {
            // After we use fprintf, another library function to write to the file, we close the file.
            fprintf(file, "%s,%s\n", students[i].name, students[i].dorm);
        }
        fclose(file);
    }
}

// With all these tools, we can now do more and more interesting things!