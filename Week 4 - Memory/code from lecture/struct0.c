#include <cs50.h>
#include <stdio.h>
#include <string.h>

#include "structs.h"

#define STUDENTS 3 // We used #define STUDENTS 3 to set a constant, STUDENTS, to the value 3. This prevents having to make a variable that might otherwise be changed.

int main(void)
{
    student students[STUDENTS]; // We can create an array of student structs called students, with STUDENTS number of elements.

    for (int i = 0; i < STUDENTS; i++)
    {
        printf("name: ");
        students[i].name = get_string(); // Then we can access properties in the structs with syntax like students[i].name, since students is an array and students[i] gets an individual student struct for us to use.

        printf("dorm: ");
        students[i].dorm = get_string();
    }

    for (int i = 0; i < STUDENTS; i++)
    {
        printf("%s is in %s.\n", students[i].name, students[i].dorm);
    }
}