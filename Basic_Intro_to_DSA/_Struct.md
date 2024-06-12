# Basic Theory
There are two kinds of data types, namely:
- Standard data type
  That is the type of data that has been defined by the compiler that can directly be declared when needed. Examples such as `int`, `float`, `char`, `double`, `void`.
- User defined data type
  That data types defined by the user according to his needs. The first step is to define or create the desired data type first, then declare variables with these data types. Examples like `struct` and `union`.

## Need of structures in C?
- C has built in primitive and derrived data types. Still not all real world problems can be solved using those types. You need custom data type for different 
 situations.

- For example, if you need to store 100 student record that consist of name, age and mobile number. To code that you will create 3 array variables each of size 
 100 i.e. name[100], age[100], mobile[100]. For three fields in student record it say seem feasible to you. But, think how cumbersome it would be to manage 
 student record with more than 10 fields, in separate variables for single student.

- To overcome this we need a user defined data type. In this tutorial I am going to explain how easily we will deal with these situations using structures in C 
 programming language.

## What is structure in C?
- Structure is a user defined data type. It is a collection of different data type, to create a new data type.

- For example, You can define your custom type for storing student record containing name, age and mobile. Creating structure type will allow you to handle all 
 properties (fields) of student with single variable, instead of handling it separately.

## How to declare, define and access structure members?
- To declare or define a structure, we use struct keyword. It is a reserved word in the C compiler. You must only use it for structure or its object declaration 
 or definition.

## Syntax to define a structure
```c
struct structure_name
{
    member1_declaration;
    member2_declaration;
    ...
    ...
    memberN_declaration;
};
```

- Here, structure_name is name of our custom type. memberN_declaration is structure member i.e. variable declaration that structure will have.

- Example to define a structure
- Let us use our student example and define a structure to store student object.
```c
struct student
{
    char name[40];        // Student name
    int  age;             // Student age
    unsigned long mobile; // Student mobile number
};
```
## Points to remember while structure definition
- You must terminate structure definition with semicolon ;.
- You cannot assign value to members inside the structure definition, it will cause compilation error. Since you are defining type you aren’t associating data.
- For example, following is an invalid structure definition.
```c
struct student
{
    char name[40] = "Raj";
    int  age      = 26;
    unsigned long mobile = 9891000033;
};
```
- You can define a structure anywhere like global scope (accessible by all functions) or local scope (accessible by particular function).
 Structure member definition may contain other structure type.

## How to create structure object (structure variable)?
- A data type is useless without variables. A data type defines various properties about data stored in memory. To use any type we must declare its variable. - -- 
 Hence, let us learn how to create our custom structure type objects also known as structure variable.

- In C programming, there are two ways to declare a structure variable:
```c
1.Along with structure definition
2.After structure definition
```
## Declaration along with the structure definition
- Out of two ways to declare structure variable. You can declare a structure variable along with structure before terminating the structure definition.

- Syntax:
```c
struct structure_name
{
    member1_declaration;
    member2_declaration;
    ...
    ...
    memberN_declaration;
}structure_variable;
```

- So, if you want to declare student type object along with student structure definition you can use this approach.

```c
struct student
{
    char name[40];        // Student name
    int  age;             // Student age
    unsigned long mobile; // Student mobile number
}student1;
```
## Declaration after structure definition
- The other way to declare, gives you luxury to declare structure variable anywhere in program based on the structure scope. If structure is defined in global 
 scope, we can declare its variable in main() function, any other functions and in the global section too.

Syntax:
```c
struct structure_name structure_variable;
```
- For above example, if we want to declare its variable with name student1, it will be declared as given below:
```c
struct student
{
    char name[40];        // Student name
    int  age;             // Student age
    unsigned long mobile; // Student mobile number
};

// Declare student variable
struct student student1;
```

## How to access structure members (data)?
- You created structure and its variable. But since structure is a complex data type, you cannot assign any value directly to it using assignment operator. You 
 must assign data to individual structure members separately.

## C supports two operators to access structure members, using a structure variable.

- 1.Dot/period operator .
- 2.Arrow operator ->
- 3.Dot/period operator (.) in C
- 4.Dot/period operator also known as member access operator. We use dot operator to access members of simple structure variable.

- Syntax:
```c
structure_variable.member_name;
```
```
Example:-

// Assign age of student1
student1.age = 26;

```
## Arrow operator (->) in C
- Since structure is a user defined type and you can have pointers to any type. Hence, you may also create pointers to structure.

- In C language it is illegal to access a structure member from a pointer to structure variable using dot operator. We use arrow operator -> to access structure 
 member from pointer to structure.

- Syntax:
```c
pointer_to_structure->member_name;
```
- Example:
```c
// Student2 is a pointer to student type
student2->age = 29;
```
## Example
```c
#include <stdio.h>
#include <string.h>

// create struct with person1 variable
struct Person {
  char name[50];
  int citNo;
  float salary;
} person1;

int main() {

  // assign value to name of person1
  strcpy(person1.name, "George Orwell");

  // assign values to other person1 variables
  person1.citNo = 1984;
  person1. salary = 2500;

  // print struct variables
  printf("Name: %s\n", person1.name);
  printf("Citizenship No.: %d\n", person1.citNo);
  printf("Salary: %.2f", person1.salary);

  return 0;
}
```

## Example 2

```c
#include <stdio.h>
#include <string.h>

// Define struct Person
struct Person {
  char name[50];
  int citNo;
  float salary;
};

int main() {
  // Declare struct variable person1
  struct Person person1;

  // Assign values to person1 variables
  strcpy(person1.name, "George Orwell");
  person1.citNo = 1984;
  person1.salary = 2500.00;

  // Print struct variables
  printf("Name: %s\n", person1.name);
  printf("Citizenship No.: %d\n", person1.citNo);
  printf("Salary: %.2f\n", person1.salary);

  return 0;
}


```

```c
#include <stdio.h>
#include <string.h>

// Define a structure to store car details
struct Car {
    int id;
    char color[20];
    char model[20];
    char name[20];
};

int main() {
    // Create an instance of the Car structure
    struct Car car1;
    
    // Assign values to the car1 instance
    car1.id = 1;
    strcpy(car1.color, "Red");
    strcpy(car1.model, "Sedan");
    strcpy(car1.name, "Toyota");

    // Display the car details
    printf("Car Details:\n");
    printf("ID: %d\n", car1.id);
    printf("Color: %s\n", car1.color);
    printf("Model: %s\n", car1.model);
    printf("Name: %s\n", car1.name);

    return 0;
}
```

## Keyword typedef
- We use the typedef keyword to create an alias name for data types. It is commonly used with structures to simplify the syntax of declaring variables.

- For example, let us look at the following code:
```c
struct Distance{
  int feet;
  float inch;
};

int main() {
  struct Distance d1, d2;
}
```
```c
typedef struct Distance {
  int feet;
  float inch;
} distances;

int main() {
  distances d1, d2;
}
```
# typedef Example
```c
#include <stdio.h>
#include <string.h>

// struct with typedef person
typedef struct Person {
  char name[50];
  int citNo;
  float salary;
} person;

int main() {

  // create  Person variable
  person p1;

  // assign value to name of p1
  strcpy(p1.name, "George Orwell");

  // assign values to other p1 variables
  p1.citNo = 1984;
  p1. salary = 2500;

  // print struct variables
  printf("Name: %s\n", p1.name);
  printf("Citizenship No.: %d\n", p1.citNo);
  printf("Salary: %.2f", p1.salary);

  return 0;
}
```
## Nested Structures

- You can create structures within a structure in C programming. For example,
```c
struct complex {
  int imag;
  float real;
};

struct number {
  struct complex comp;
  int integers;
} num1, num2;
```
- Suppose, you want to set imag of num2 variable to 11. Here's how you can do it:
```c
num2.comp.imag = 11;
```
## C Nested Structures
```
#include <stdio.h>

struct complex {
  int imag;
  float real;
};

struct number {
  struct complex comp;
  int integer;
} num1;

int main() {

  // initialize complex variables
  num1.comp.imag = 11;
  num1.comp.real = 5.25;

  // initialize number variable
  num1.integer = 6;
	
  // print struct variables
  printf("Imaginary Part: %d\n", num1.comp.imag);
  printf("Real Part: %.2f\n", num1.comp.real);
  printf("Integer: %d", num1.integer);

  return 0;
}
```

- Output
```c
Imaginary Part: 11
Real Part: 5.25
Integer: 6
```
## Array and Structure in c
```c
#include <stdio.h>

// Define the structure
struct Student {
  int rollNumber;
  char studentName[20];
  float percentage;
};

int main() {
  // Declare and initialize an array of structs
  struct Student studentRecord[5] = {{1, "John", 78.5},
                                     {2, "Alice", 89.2},
                                     {3, "Bob", 76.8},
                                     {4, "Eva", 91.7},
                                     {5, "Mike", 85.0}};

  // Display student information
  printf("Student Information:\n");
  for (int i = 0; i < 5; ++i) {
    printf("Roll Number: %d\tName: %s\tPercentage: %.2f\n",
           studentRecord[i].rollNumber, studentRecord[i].studentName,
           studentRecord[i].percentage);
  }

  return 0;
}
```
