# So to create our student module, we would:

class Student: # give me a structure
    def __init__(self, name, dorm):
        self.name = name
        self.dorm = dorm


# We declare a class of objects called Student, which will only have one method, 
# or built-in function, init, which we won’t call directly but gets called when 
# we create a Student as we did above with Student(name, dorm).

# This function gets the object itself as an argument and the other arguments 
# we want to be passed in when the object is created, in this case name and dorm. 
# Then inside the function, we store the arguments to the object that’s just been created.

## C
# And we’ll learn one new keyword to easily represent this, a struct. We can create a more complicated data type and name it:

typedef struct
{
    string name;
    string dorm;
}
student;

# To represent a student, we can include two pieces of information, string name 
# and string dorm.