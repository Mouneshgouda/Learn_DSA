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
- sizeof(char) returns the size of the char data type in bytes.
- sizeof(int) returns the size of the int data type in bytes.
- sizeof(float) returns the size of the float data type in bytes.
- sizeof(double) returns the size of the double data type in bytes.
- When you run this code, it will print the sizes of these data types on your specific computer, allowing you to see the actual sizes used by your system.

- When you declare a variable, the computer allocates a specific amount of memory space corresponding to the chosen data type. For instance, when you declare a 
 variable of type char, the computer reserves 1 byte of memory because the size of the 'char' data type is conventionally 1 byte.
