# Pointer
- In this comprehensive C Pointers tutorial, my primary goal is to guide you through the fundamentals of C pointers from the ground up. By the end of this tutorial, you will have gained an in-depth understanding of the following fundamental topics:
```c
1.What is a Pointer?
2.How Data is Stored in Memory?
3.Storing Memory Addresses using Pointers
4.Accessing Data through Pointers
5.Pointer Arithmetic
6.Pointer to Pointer (Double Pointers)
7.Passing Pointers as Function Arguments
8.Arrays of Pointers
9.NULL Pointers
```

# What is a pointer?
- A pointer serves as a reference that holds the memory location of another variable. This memory address allows us to access the value stored at that location in 
 the memory. You can think of a pointer as a way to reference or point to the location where data is stored in your computer's memory

- Pointers can be a challenging concept for beginners to grasp, but in this tutorial, I'll explain them using real-life analogies to make the concept clearer. 
 However, Before delving into pointers and their workings, it's important to understand the concept of a memory address.

- A memory address is a unique identifier that points to a specific location in a computer's memory. Think of it like a street address for data stored in your 
 computer's RAM (Random Access Memory). Just as a street address tells you where a particular house is located in the physical world, a memory address tells the 
 computer where a specific piece of information or data is stored in its memory.

- Take a look at the image below for a better understanding:
![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/25151120-7c1d-4f32-ad13-807f0b1ce086)

- In this illustration, each block represents one byte of memory. It's important to note that every byte of memory has a unique address. To make it easier to 
 understand, I've represented the addresses in decimal notation, but computers actually store these addresses using hexadecimal values. Hexadecimal is a base-16 
 numbering system commonly used in computing to represent memory addresses and other low-level data. It's essential to be aware of this representation when working 
 with memory-related concepts in computer programming

## How data is stored in the memory:
- Every piece of data in your computer, whether it's a number, a character, or a program instruction, is stored at a specific memory address. The amount of space 
 reserved for each data type can vary, and it is typically measured in bytes (where 1 byte equals 8 bits, with each bit representing either 0 or 1). The specific 
 sizes of data types also depend on the computer architecture you are using. For instance, on most 64-bit Linux machines, you'll find the following typical sizes 
 for common data types:
- 1.char = 1 byte
- 2.int = 4 bytes
- 3.float = 4 bytes
- 4.double = 8 bytes
- 5.These sizes define how much memory each data type occupies and are crucial for memory management and efficient data representation in computer systems.

- You can use the sizeof operator to determine the size of data types on your computer.
- In this example:

example:
```c
#include <stdio.h>
int main() {
printf("Size of char: %zu bytes\n", sizeof(char));
printf("Size of int: %zu bytes\n", sizeof(int));
printf("Size of float: %zu bytes\n", sizeof(float));
printf("Size of double: %zu bytes\n", sizeof(double));

return 0;
}
```
```c
Output:
Size of char: 1 bytes
Size of int: 4 bytes
Size of float: 4 bytes
Size of double: 8 bytes
```
- sizeof(char) returns the size of the char data type in bytes.
- sizeof(int) returns the size of the int data type in bytes.
- sizeof(float) returns the size of the float data type in bytes.
- sizeof(double) returns the size of the double data type in bytes.
- When you run this code, it will print the sizes of these data types on your specific computer, allowing you to see the actual sizes used by your system.

- When you declare a variable, the computer allocates a specific amount of memory space corresponding to the chosen data type. For instance, when you declare a 
 variable of type char, the computer reserves 1 byte of memory because the size of the 'char' data type is conventionally 1 byte.
```c
char n;
```
![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/c8a2d235-9e63-483a-9e59-c74f1b125163)

- In this example, we declare a variable n of type char without assigning it a specific value. The memory address allocated for the n variable is 106. This 
 address, 106, is where the computer will store the char variable n, but since we haven't assigned it a value yet, the content of this memory location may 
 initially contain an unpredictable or uninitialized value.
```c
char n;
n = C;
```
- When we assign the value 'C' to the variable n, the character 'C' is stored in the memory location associated with the variable n. When we assign the value 'C' 
 to the variable n, the character 'C' is stored in the memory location associated with the variable n.

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/e236a021-28e8-4037-8422-1f233d491510)

- As mentioned earlier, a byte can only store numerical values. When we store the letter 'C' in a byte, the byte actually holds the ASCII code for 'C,' which is 
 67. In computer memory, characters are represented using their corresponding ASCII codes. So, in memory, the character 'C' is stored as the numerical value 67. 
 Here's how it looks in memory

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/0dadeb63-7ff4-4f7c-bb66-2acc0c8fc82b)

- Since integers are typically stored within four bytes of memory, let's consider the same example with an int variable. In this scenario, the memory structure 
 would appear as follows:
```c
int t;
t = 104;
```
![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/fda9149f-20f5-45cf-b8b1-1a9c37b7baac)

- In this example, the memory address where the variable t is stored is 121. An int variable like “t” typically uses four consecutive memory addresses, such as 
 121, 122, 123, and 124. The starting address, in this case, 121, represents the location of the first byte of the int, and the subsequent addresses sequentially 
 represent the following bytes that collectively store the complete int value.

- If you want to know the memory address of a variable in a program, you can use the 'address of' unary operator, often denoted as the '&' operator. This operator 
 allows you to access the specific memory location where a variable is stored.
```c
#include <stdio.h>

int main() {
    char c;
    int n;

    // Initialize variables with values
    c = 'A';
    n = 42;

    // Access and display memory addresses
    printf("Memory address of char c: %p\n", &c);
    printf("Memory address of int n: %p\n", &n);

    return 0;
}
```
```c
output:
Memory address of char c: 0x7fff8b9efdaf
Memory address of int n: 0x7fff8b9efda8
```
### When you run the following program on your computer:
- It will provide you with specific memory addresses for the variables c and n. However, each time you rerun the program, it might allocate new memory addresses 
 for these variables.
- It's important to understand that while you can determine the memory address of a variable using the & operator, the exact memory location where a variable is 
 stored is typically managed by the system and the compiler. As a programmer, you cannot directly control or assign a specific memory location for a variable. 
 Instead, memory allocation and management are tasks handled by the system and the compiler.

### Storing memory address using pointers
- As mentioned earlier, a pointer is a variable that stores the memory address of another variable. This memory address allows us to access the value stored at 
 that location in memory. You can think of a pointer as a way to reference or point to the location where data is stored in your computer's memory.

- Now, let's begin by declaring and initializing pointers. This step is essential because it sets up the pointer to hold a specific memory address, enabling us to 
 interact with the data stored at that location.

- Declaring Pointers: To declare a pointer, you specify the data type it points to, followed by an asterisk (*), and then the pointer's name. For example:
```c
int *ptr; // Declaring an integer pointer
```
- Here, we've declared a pointer named ptr that can point to integers.
- ![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/1be19c50-7a59-4643-89bc-4df7e48cd350)
- he size of pointers on 64-bit systems is usually 8 bytes (64 bits).
- To determine the pointer size on your system, you can use the sizeof operator:
```c
#include <stdio.h>

int main() {
    int *ptr;
    printf("Size of pointer: %zu bytes\n", sizeof(ptr));
    return 0;
}
```
```c
Output:
Size of pointer: 8 bytes
```
- Initializing Pointers: Once you've declared a pointer, you typically initialize it with the memory address it should point to. Once again, To obtain the memory 
 address of a variable, you can employ the address-of operator (&). For instance:
```c
#include <stdio.h>

int main() {
    // Declaring and initialize an integer variable
    int x = 10;

    // Declaring an integer pointer
    int *ptr;

    // Initialize the pointer with the address of x
    ptr = &x;

    printf("Address of X: %p\n", &x); 
    printf("Value of ptr: %p\n", ptr);
    return 0;
}
```
```c
Output:
Address of X: 0x7ffe33307c84
Value of ptr: 0x7ffe33307c84
```
- In this program:

- 1.We declare an integer variable x and initialize it with the value 10. This line creates a variable x in memory and assigns the value 10 to it.

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/7f7ac748-74ec-49df-aee3-cb0a0edfb4c5)
- 2.We declare an integer pointer ptr using the int *ptr syntax. This line tells the compiler that ptr will be used to store the memory address of an integer variable.


![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/a9ab78eb-e5ed-4a7c-9e31-01b748d60ed3)

- 3.We initialize the pointer ptr with the memory address of the variable x. This is achieved with the line ptr = &x;. The & operator retrieves the memory address of x, and this address is stored in the pointer ptr.
  
![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/2e0e4694-4081-420f-9d1e-0069dc3b73c5)

### Accessing Data through Pointers
- 1.Dereferencing Pointers:
- To access the data that a pointer is pointing to, you need to dereference the pointer.
 Dereferencing a pointer means accessing the value stored at the memory address that the pointer points to. In C, you can think of pointers as variables that 
 store memory addresses rather than actual values. To get the actual value (data) stored at that memory address, you need to dereference the pointer.

- Dereferencing is done using the asterisk (*) operator. Here's an example:
```c
 // Declaring and initializing an integer variable
int x = 10; 

// Create a pointer 'ptr' and make it point to the address of 'x'
int *ptr = &x;   

// Dereference 'ptr' to get the value stored at the address it points to
int value = *ptr; 

// Now, 'value' contains the value 10, which is the value stored at the memory address of 'x'.
```
- It looks like this in the memory:
- int x = 10; variable 'x' stores the value 10:

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/e4b50d1c-dfae-4a8b-a9ef-a2579a8342a0)

- int *ptr = &x; Now, the pointer 'ptr' point to the address of 'x':

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/8e430ba7-b923-4e5b-935a-fcb459842762)

- int value = *ptr; Dereference 'ptr' to get the value stored at the address it points to:


![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/bb80f183-a972-4c2f-b459-9ebb38f22042)

- In this example, *ptr retrieves the value stored at the memory address pointed to by ptr, which is the value of the integer variable x. So, value will be 
 assigned the value 10.

### Reading and Modifying Data:
- Pointers allow you to not only read but also modify data indirectly:
```c
#include <stdio.h>

int main() {
  int x = 10;   // Declare and initialize an integer variable
  int *ptr;     // Declare an integer pointer
  ptr = &x;     // Initialize the pointer with the address of x

  printf("Value of X is: %d\n", x);

  *ptr = 20;    // Change the value of x through the pointer
  printf("Value of X through pointer 'ptr': %d\n", *ptr);

    return 0;
}
```
```c
Output:
Value of X is: 10
Value of X through pointer 'ptr' is: 20
```
```c
Note: The asterisk is a versatile symbol with different meanings depending on where it's used in your C program, for example:
Declaration: When used during variable declaration, the asterisk (*) indicates that a variable is a pointer to a specific data type. For example: int *ptr; declares 'ptr' as a pointer to an integer.
```
- Dereferencing: Inside your code, the asterisk (*) in front of a pointer variable is used to access the value stored at the memory address pointed to by the 
 pointer. For example: int value = *ptr; retrieves the value at the address 'ptr' points to.

### Pointer Arithmetic:
- Pointer arithmetic is the practice of performing mathematical operations on pointers in C. This allows you to navigate through arrays, structures, and 
 dynamically allocated memory. You can increment or decrement pointers, add or subtract integers from them, and compare them. It's a powerful tool for efficient 
 data manipulation, but it should be used carefully to avoid memory-related issues.

- Incrementing a Pointer:
```
#include <stdio.h>

int main() {
  int arr[4] = {10, 20, 30, 40};
  int *ptr = arr; // Point to the start of the array

  // Print the first element of the array using dereferencing
  printf("The first element of the array: %d\n", *ptr);

  // Accessing elements using pointer arithmetic
  int secondElement = *(ptr + 1); // Moves the pointer to the second element
  printf("The second element of array: %d\n", secondElement);

  int thirdElement = *(ptr + 2); // Moves the pointer to the third element
  printf("The third element of array: %d\n", thirdElement);

  return 0;
}
```
```c
Output:
The first element of the array: 10
The second element of array: 20
The third element of array: 30
```
- Now, this program is how it looks in the memory:
- int arr[4] = {10, 20, 30, 40};
![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/50714850-723f-4580-b7e4-67f07a8c6440)

- int *ptr = arr; creates a pointer ptr that points to the first element of the array arr. In C, arrays are zero-indexed, so the first element can also be 
 accessed using arr + 0. so that means the first element's address is the same as the array's address (i.e., arr or arr + 0).

- In the line int secondElement = *(ptr + 1);, the expression ptr + 1 adjusts the pointer to point to the second element of the array. The variable secondElement 
 now stores the value of the second element. Similarly, with int thirdElement = *(ptr + 2);, the pointer is incremented to point to the third element of the array.

- Here is how it looks in the memory:

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/ceae563a-a050-4fa3-aabb-d5a4c0e65564)


![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/f895d2b4-d4b4-46ed-9c88-39aa9d611fc8)

- This behavior is a key aspect of pointer arithmetic. When you add an integer to a pointer, it moves to the memory location of the element at the specified 
 index, allowing you to efficiently access and manipulate elements within the array. It's worth noting that you can use pointer arithmetic to access elements in 
 any position within the array, making it a powerful technique for working with arrays of data.
 Now, let's print the memory addresses of the elements in the array from our previous program.

```c
#include <stdio.h>

int main() {
  int arr[4] = {10, 20, 30, 40};

  printf("The Address of the first element of the array: %p\n", &arr[0]);

  printf("The Address of the second element of the array: %p\n", &arr[1]);

  printf("The Address of the third element of the array: %p\n", &arr[2]);

  return 0;
}
```
```c
Output:
The Address of the first element of the array: 0x7fff76995f40
The Address of the second element of the array: 0x7fff76995f44
The Address of the third element of the array: 0x7fff76995f48
```
- If you observe the last two digits of the first address is 40, and the second one is 44. You might be wondering why it's not 40 and 41. This is because we're 
 working with an integer array, and in most systems, the size of an int data type is 4 bytes. Therefore, the addresses are incremented in steps of 4. The first 
 address shows 40, the second 44, and the third one 48

If you observe the last two digits of the first address is 40, and the second one is 44. You might be wondering why it's not 40 and 41. This is because we're working with an integer array, and in most systems, the size of an int data type is 4 bytes. Therefore, the addresses are incremented in steps of 4. The first address shows 40, the second 44, and the third one 48

Decrementing a Pointer
Decrement (--) a pointer variable, which makes it point to the previous element in an array. For example, ptr-- moves it to the previous one.
For example:
#include <stdio.h>

int main() {
    int arr[5] = {10, 20, 30, 40, 50};
    int *ptr = &arr[3]; // Point to the fourth element (value 40)

    // Decrement the pointer
    ptr--;

    // Print the decremented value using pointer dereferencing
    printf("The decremented value: %d\n", *ptr);

    return 0;
}
Output:
The decremented value: 30
Explanation:

We have an integer array arr with 5 elements, and we initialize a pointer ptr to point to the fourth element (value 40) using &arr[3].

Then, we decrement the pointer ptr by one with the statement ptr--. This moves the pointer to the previous memory location, which now points to the third element (value 30).

Finally, we print the value pointed to by the decremented pointer using *ptr, which gives us the value 30.

In this program, we demonstrate how decrementing a pointer moves it to the previous memory location in the array, allowing you to access and manipulate the previous element.

### Pointer to pointer
- Pointers to pointers, or double pointers, are variables that store the address of another pointer. In essence, they add another level of indirection. These are 
  commonly used when you need to modify the pointer itself or work with multi-dimensional arrays.

- To declare and initialize a pointer to a pointer, you need to add an extra asterisk (*) compared to a regular pointer. Let's go through an example:
```c
int x = 10;
int *ptr1 = &x;      // Pointer to an integer
int **ptr2 = &ptr1;  // Pointer to a pointer to an integer
```
- In this example, ptr2 is a pointer to a pointer. It points to the memory location where the address of x is stored (which is ptr1).

- The diagram of ptr2 pointing to ptr1 pointing to x looks like this:
  int **ptr2 = &ptr1; // Pointer to a pointer to an integer

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/f2e1b383-a00c-4144-ad3e-09de069ab297)

- int *ptr1 = &x; // Pointer to an integer

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/9c14aaa7-0ca7-4fa4-9c2e-5b6b068a0dcc)

- int x = 10;

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/7d43bd74-fa10-4f32-b374-b86430b1e54d)

- In this example, ptr2 is a pointer to a pointer. It points to the memory location where the address of x is stored (which is ptr1).

- The below program will show you how to print the value of x through pointer to pointer
```c
#include <stdio.h>

int main() {
    int x = 10;
    int *ptr1 = &x;      // Pointer to an integer
    int **ptr2 = &ptr1;  // Pointer to a pointer to an integer

    // Printing the values
    printf("Value of x: %d\n", x);
    printf("Value of x using ptr1: %d\n", *ptr1);
    printf("Value of x using ptr2: %d\n", **ptr2);

    printf("==========================\n");
    // Printing the memory addresses
    printf("Address of x: %p\n", &x);
    printf("Address of ptr1: %p\n", &ptr1);
    printf("Address of ptr2: %p\n", &ptr2);

    return 0;
}
```
```c
Output:
Value of x: 10
Value of x using ptr1: 10
Value of x using ptr2: 10
==========================
Address of x: 0x7ffdcbcfe24c
Address of ptr1: 0x7ffdcbcfe240
Address of ptr2: 0x7ffdcbcfe238
```
- In this program, we first explain that it prints the value of x using a regular variable, a pointer, and a pointer to a pointer. We then print the memory 
 addresses of x, ptr1, and ptr2.

### Passing Pointers as Function Arguments:
- In C, you can pass pointers as function arguments. This allows you to manipulate the original data directly, as opposed to working with a copy of the data, as 
 you would with regular variables. Here's how it works:

- How to Declare and Define Functions that Take Pointer Arguments:
In your function declaration and definition, you specify that you're passing a pointer by using the * operator after the data type. For example:
```c
void modifyValue(int *ptr) {
    // Function code here
}
```
- In the above function, we declare ptr as a pointer to an integer. This means it can store the memory address of an integer variable.

- Why Would You Pass Pointers to Functions?

- Passing pointers to functions allows you to:

- 1.Modify the original data directly within the function.
- 2.Avoid making a copy of the data, which can be more memory-efficient.
- 3.Share data between different parts of your program efficiently.
- 4.This concept is especially important when working with large data structures or when you need to return multiple values from a function.

### Call by Value vs. Call by Reference:
- Understanding how data is passed to functions is crucial when working with pointers. there are two common ways that data can be passed to functions: call by 
 value and call by reference.

### Call by Value:
- When you pass data by value, a copy of the original data is created inside the function.
- Any modifications to this copy do not affect the original data outside of the function.
- This is the default behavior for most data types when you don't use pointers.

### Call by Reference (Using Pointers):
- When you pass data by reference, you're actually passing a pointer to the original data's memory location.
- This means any changes made within the function will directly affect the original data outside the function.
- This is achieved by passing pointers as function arguments, making it call by reference.
- Using pointers as function arguments allows you to achieve call by reference behavior, which is particularly useful when you want to modify the original data 
  inside a function and have those changes reflected outside the function.

- Let's dive into some code examples to illustrate how pointers work as function arguments. We'll start with a simple example to demonstrate passing a pointer to 
 a function and modifying the original data.

- Consider this example:
```c
#include <stdio.h>

void modifyValue(int *ptr) {
    *ptr = *ptr * 2;
}

int main() {
    int num = 5;
    printf("Original value: %d\n", num);
    modifyValue(&num);
    printf("Modified value: %d\n", num);
    return 0;
}
```
```c
Output:
Original value: 5
Modified value: 10
```
- In this code, we define a function modifyValue that takes a pointer to an integer. We pass the address of the variable num to this function, and it doubles the 
 value stored in num directly.

- This is a simple demonstration of passing a pointer to modify a variable's value. Pointers allow you to work with the original data efficiently.

## Arrays of Pointers
- An array of pointers is essentially an array where each element is a pointer. These pointers can point to different data types (int, char, etc.), providing 
 flexibility and efficiency in managing memory.

## How to Declare an Array of Pointers?
- To declare an array of pointers, you specify the type of data the pointers will point to, followed by square brackets to indicate it's an array, and then the 
 variable name. For example:
```c
int *intArray[5];  // Declares an array of 5 integer pointers
```
### Initializing an Array of Pointers

- You can initialize an array of pointers to each element to point to a specific value, For example:
```c
int *intArray[5]; // Declare an array of 5 integer pointers.
int x = 10;
int y = 20;
intArray[0] = &x; // Initialize the first element to point to x.
intArray[1] = &y; // Initialize the second element to point to y.
```
### How to Access Elements Through an Array of Pointers?
- To access elements through an array of pointers, you can use the pointer notation. For example:
```c
#include <stdio.h>

int main() {
  int *intArray[5];
  int x = 10;
  int y = 20;
  intArray[0] = &x;
  intArray[1] = &y;

  // Accessing the values using pointers
  printf("Value at intArray[0]: %d\n", *intArray[0]);
  printf("Value at intArray[1]: %d\n", *intArray[1]);

  return 0;
}
```
```c
Output"
Value at intArray[0]: 10
Value at intArray[1]: 20
```
- This program demonstrates how to access and print the values pointed to by the pointers in the array.

## NULL Pointers
- A NULL pointer is a pointer that lacks a reference to a valid memory location. It's typically used to indicate that a pointer doesn't have a specific memory 
 address assigned, often serving as a placeholder or default value for pointers.

- Here's a code example that demonstrates the use of a NULL pointer:
```c
#include <stdio.h>

int main() {
    int *ptr = NULL; // Declare and initialize a null pointer

    if (ptr == NULL) {
        printf("The pointer is NULL.\n");
    } else {
        printf("The pointer is not NULL.\n");
    }

    return 0;
}
```
```c
Output:
The pointer is NULL.
```
In this example, we declare a pointer ptr and explicitly initialize it with the value NULL. We then use an if statement to check if the pointer is NULL. Since it is, the program will print "The pointer is NULL." This illustrates how NULL pointers are commonly used to check if a pointer has been initialized or assigned a valid memory address.
