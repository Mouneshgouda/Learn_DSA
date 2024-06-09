# What is Data Structure
- A data structure is a specialized and systematic format of storing, processing and organizing data in the memory of a computer. It is stored in a way that it can be 
  accessed and used efficiently. It is essential for algorithms because of several data structure types. You can learn more about data structures with an online Data 
  Structures and Algorithms course.



# 2 Different Types of Data Structures
![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/1ba44524-201e-43fe-bac3-8f4ac5239030)


- Various types of data structures allow storing data in the computer memory in such a way that the data can be accessed quickly for the required calculations. 

- Two broad data structure types based on the type of operations they are required to perform are primitive and non-primitive data structures. They have further 
 classifications which we will discuss in subsequent sections. 

### - 1. Primitive Data Structure
- The primitive data structures are also known as built-in data structures as they are basic data structures in many high-level programming languages. They operate 
  directly according to the machine’s instructions. The following are the various types of data structures that are primitive. 

- Boolean: The data in this type is either true or false or positive or negative. Boolean type depicts whether the data is positive or negative. Here binary 
 variables, logical values, and algebra are used. 
- Integer: In this data structure type, both positive and negative numbers along with zero are stored. These integers help with the arithmetic operations. 
 Floating-point Numbers: In this type of DS, approximate values are used in the form of a formula to allow the trade-off between range and precision. They include 
 real numbers positive, negative, fractions, and numbers with decimal points. 
- Character: It stores information in a fixed-length field or variable-length string. The fixed-length field is used by the CHAR data type. They are extended with 
 spaces on output but the variable-length string is not. Numbers, alphabets, and special characters are all included but represented inside single or double 
 inverted commas. 
- Pointer: The pointer data structure stores the memory address of another variable as its value. 
### 2. Non-Primitive Data Structure
- Non-primitive data structures are complex data structures that use primitive data structures to form a structure of their own. This is why they are also known as 
 derived types. Though in-built support is provided for these data structures by many programming languages, they are mostly user-defined. Non-primitive data 
 structures can be further classified into linear and non-linear data structures. 

### Linear Data Structure
- The linear data structure sequentially stores the values, that is, each value is linked to the previous one. The following are the categories of linear data 
 structure. 

- Array: In a fundamental data structure,
- Array stores a collection of data items in a linear sequence and contiguous memory location.
- Each data item is called an “element”. Retrieval of data is easy with this data structure due to the storage of elements in contiguous memory locations. 
- Each array element has a unique associated index value with which it can be accessed. 
- The size of an array can be expressed mathematically as Length*Element size. 
- Here length is the number of elements in the array and the element size is the memory size of the individual element. 
- Arrays can be used to store data in tabular format, in financial analysis, in scientific computing, to represent graphs, CPU scheduling, in management systems 
 in libraries, in online ticket booking systems, etc. 
- Linked List: The linked list data structure:
- Uses data memory allocation to store its elements in different locations. Despite being in different locations, these elements are arranged in a sequence and 
 linked with one another. 
- The element contains a data item and a link or reference to the subsequent item on the same list. This is why they are most preferred when one has to handle 
 dynamic data elements. 
- There are four major types of lists in data structures, singly linked lists, doubly linked lists, circular linked lists, and circular doubly linked lists. 
  Linked lists can be used to implement stacks, graphs, etc., to perform arithmetic operations on long integers, for representation of sparse metrics, in memory 
  management.
- Stack: The stack data structure is:
- One of the types of data structure that uses LIFO or Last In First Out to store and retrieve data elements. It simply means that the element stored last in the 
  stack will be retrieved first.
- Stack uses two operations for implementing the LIFO principle, push and pop.
- The push() method inserts the element in the stack and the pop() method retrieves one or more elements from the stack. 
- Stacks are used to maintain the call logs in mobile phones, to keep track of visited pages on a browser, etc. 
- Queue: The queue data structure:
- Uses the FIFO or First In First Out principle. 
- Here the element stored first or the oldest element in the structure is retrieved first. It is retrieved by the dequeue() method. 
- It is used for handling website traffic, asynchronous transfer of data, switching to multiple applications on an operating system, etc. 
  Also Read: Types of Queues in Data Structure

### Non-linear Data Structure
- In the non-linear data structure, the elements are stored in a non-linear or non-sequential manner. It is complicated since values are arranged at multiple 
 levels, that is, each value is connected to one or more values. The following are the types of non-linear data structures. 

- Graph: The graph is a node-based type of DS that has a list of other nodes that are linked in the graph. It has two components, vertices, and edges. The edges 
 are used to connect vertices. This data structure is used for network representation. The graph data structure is used to represent the flow of computation, in 
 modeling graphs, in Google Maps, to study molecules of physics and chemistry, etc.
- Tree: A subtype of the graph that represents its elements in a hierarchical order. A tree uses a node-like structure to make a hierarchical form and each node 
 here represents a value. The root node is the uppermost node of the tree and the leaf node is the node at the bottom of the tree. This data structure imposes a 
 rule that nodes of a tree do not create loops in the data structure. A tree is used for indexing databases, scanning, parsing, and generating code in compiler 
 design, in routers in computer networks, social networking sites, etc. 


# Data structure Operations
Data structure operations are the data that is stored in our data structures that are processed by a certain set of operations.
therefore, while selecting a particular data structure for the application then we choose a given data structure largely on the frequency with which specific operations are performed.
there are the following Data structure operations we can perform on the data structures:

Traversing:
 Accessing each data exactly once in the data structure so that each data item in traversed or visited.
 In data structure operation, traversing operation of an array, every element of an array is accessed exactly for once for processing.
 it is also called the visiting of an array.
 
```c
For Example:
Let CB is a Linear Array (unordered) with N elements.

//Write a Program which performs traversing operation.
#include <stdio.h>
void main()
{
   int CB[] = {3,5,7,9,11};
   int i, n = 5;
   printf("The array elements are:\n");
   for(i = 0; i < n; i++)
   {
      printf("CB[%d] = %d \n", i, CB[i]);
   }
}

The array elements are:
CB[0] = 3 
CB[1] = 5 
CB[2] = 7 
CB[3] = 9 
CB[4] = 11
```

- Searching: it is Finding the location of data within the data structure that satisfies the searching condition or the criteria.

- Inserting: Adding new data in the data structure is referred to as insertion.

- Deleting: in this operation Removing data from the data structure is referred to as deletion.

- Sorting: Arranging the data in some logical order, for example, is numerical increasing order or alphabetically.

- Merging: Combining the data of two different sorted files into a single sorted file.

# Union
- Unions in C allow you to store different data types in the same memory location. You can only store one type of data at a time in a union. Unions are useful 
 when you need to manage different types of data but only one type at a time.

- Example: Union to Store Different Data Types
- Here’s an example of how a union can be used to store different data types:
```c
#include <stdio.h>

// Define a union to store different types of data
union Data {
    int i;
    float f;
    char str[20];
};

int main() {
    union Data data;

    // Store an integer
    data.i = 10;
    printf("data.i: %d\n", data.i);

    // Store a float
    data.f = 220.5;
    printf("data.f: %f\n", data.f);

    // Store a string
    strcpy(data.str, "Hello, World!");
    printf("data.str: %s\n", data.str);

    return 0;
}

```
# Union and structure
- Union and structure in C  are same in concepts, except allocating memory for their members.
- Structure allocates storage space for all its members separately.
 Whereas, Union allocates one common storage space for all its members
- We can access only one member of union at a time. We can’t access all member values at the same time in union. But, structure can access all member values at 
 the same time. This is because, Union allocates one common storage space for all its members. Where as Structure allocates storage space for all its members 
 separately.
- Many union variables can be created in a program and memory will be allocated for each union variable separately.
- Below table will help you how to form a C union, declare a union, initializing and accessing the members of the union.

| **Using Normal Variable** | **Using Pointer Variable** |
|---------------------------|----------------------------|
| **Syntax:**               | **Syntax:**                |
| `union tag_name {`        | `union tag_name {`         |
| `    data type var_name1;`| `    data type var_name1;` |
| `    data type var_name2;`| `    data type var_name2;` |
| `    data type var_name3;`| `    data type var_name3;` |
| `};`                      | `};`                       |
| **Example:**              | **Example:**               |
| `union student {`         | `union student {`          |
| `    int mark;`           | `    int mark;`            |
| `    char name[10];`      | `    char name[10];`       |
| `    float average;`      | `    float average;`       |
| `};`                      | `};`                       |
| **Declaring Union:**      | **Declaring Union:**       |
| `union student report;`   | `union student *report, rep;` |
| **Initializing Union:**   | **Initializing Union:**    |
| `union student report = {100, "Mani", 99.5};` | `union student rep = {100, "Mani", 99.5};` |
|                           | `report = &rep;`           |
| **Accessing Union Members:** | **Accessing Union Members:** |
| `report.mark;`            | `report->mark;`            |
| `report.name;`            | `report->name;`            |
| `report.average;`         | `report->average;`         |



### Using Normal Variable
```c
#include <stdio.h>
#include <string.h>

union student 
{
            char name[20];
            char subject[20];
            float percentage;
};

int main() 
{
    union student record1;
    union student record2;

    // assigning values to record1 union variable
       strcpy(record1.name, "Raju");
       strcpy(record1.subject, "Maths");
       record1.percentage = 86.50;

       printf("Union record1 values example\n");
       printf(" Name       : %s \n", record1.name);
       printf(" Subject    : %s \n", record1.subject);
       printf(" Percentage : %f \n\n", record1.percentage);

    // assigning values to record2 union variable
       printf("Union record2 values example\n");
       strcpy(record2.name, "Mani");
       printf(" Name       : %s \n", record2.name);

       strcpy(record2.subject, "Physics");
       printf(" Subject    : %s \n", record2.subject);

       record2.percentage = 99.50;
       printf(" Percentage : %f \n", record2.percentage);
       return 0;
}

```
```c
Output:-

Union record1 values example
Name :
Subject :
Percentage : 86.500000;
Union record2 values example
Name : Mani
Subject : Physics
Percentage : 99.500000
```


# Structure

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/8bc04054-d747-4ce8-b3c0-baba3147ff54)

**DIFFERENCE BETWEEN STRUCTURE AND UNION IN C**
**DIFFERENCE BETWEEN STRUCTURE AND UNION IN C**

| **C Structure** | **C Union** |
|-----------------|-------------|
| Structure allocates storage space for all its members separately. | Union allocates one common storage space for all its members. |
| Structure occupies higher memory space. | Union occupies lower memory space over structure. |
| We can access all members of structure at a time. | We can access only one member of union at a time. |
| **Example:**              | **Example:**               |
| `struct student{`         | `union student {`          |
| `    int mark;`           | `    int mark;`            |
| `    char name[10];`      | `    char name[10];`       |
| `    double average;`      | `    double average;`       |
| `};`                      | `};`                       |
| For above structure, memory allocation will be like below. | For above union, memory allocation will be like below. |
| `int mark – 4B` | The largest member (`double average`) needs 8 bytes, so the total memory allocation for the union will be 8 bytes. |
| `char name[6] – 6B` | |
| `double average – 8B` | |
| `Total memory allocation = 4 + 6 + 8 = 18 Bytes` | |


