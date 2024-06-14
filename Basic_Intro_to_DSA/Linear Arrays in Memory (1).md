# Representation of Linear Arrays in Memory
- In Data Structures and Algorithms (DSA), a linear array (or simply an array) is a collection of elements stored in contiguous memory locations. Arrays are a 
 fundamental data structure in C programming due to their simplicity and efficiency in accessing elements. Here's a detailed explanation of how linear arrays are 
 represented in memory in C

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/f5a8fba6-4ece-421b-b866-830698082c06)

### 1. Declaration and Initialization
- In C, an array can be declared and initialized as follows:
```c
------------------------------------------------------------------------------------------------
int arr[5] = {1, 2, 3, 4, 5};
-------------------------------------------------------------------------------------------------

- This declaration creates an array arr of size 5, and initializes it with the values 1, 2, 3, 4, 5.

```
## Sizeof() in array
```c
#include <stdio.h>

int main() {
    int myArray[] = {10, 20, 30, 40, 50};  // Declare and initialize an array

    // Calculate the total size of the array in bytes
    size_t totalSize = sizeof(myArray);

    // Calculate the size of one element in bytes
    size_t elementSize = sizeof(myArray[0]);

    // Calculate the total number of elements
    size_t totalElements = totalSize / elementSize;

    // Print the results
    printf("Total size of the array in bytes: %zu\n", totalSize);
    printf("Size of one element in bytes: %zu\n", elementSize);
    printf("Total number of elements: %zu\n", totalElements);

    return 0;
}

```
## Modify
```c
#include <stdio.h>

int main() {
    int myArray[5];  // Declare an array of 5 integers

    // Initialize the array elements
    myArray[0] = 10;
    myArray[1] = 20;
    myArray[2] = 30;
    myArray[3] = 40;
    myArray[4] = 50;

    // Access and print the array elements
    for (int i = 0; i < 5; i++) {
        printf("Element at index %d: %d\n", i, myArray[i]);
    }

    // Modify the array elements
    myArray[2] = 35; // Change the third element

    // Print the modified array
    printf("\nAfter modification:\n");
    for (int i = 0; i < 5; i++) {
        printf("Element at index %d: %d\n", i, myArray[i]);
    }

    return 0;
}
```

### 2. Memory Representation

- When an array is declared, memory is allocated for it in a contiguous block. Each element of the array is stored in consecutive memory locations. The size of 
 each element depends on the data type of the array. For example, in the case of an integer array, each element typically occupies 4 bytes (assuming int is 4 bytes 
 on the system).

For the above array arr, the memory representation might look like this:
```c
------------------------------------------------------------------------------------------------
Memory Address   Value
0x1000           1
0x1004           2
0x1008           3
0x100C           4
0x1010           5
------------------------------------------------------------------------------------------------

```
- Here, 0x1000 is the starting address of the array, and each subsequent element is stored 4 bytes apart.

### 3. Accessing Elements
- Elements of the array can be accessed using their indices. In C, array indices start at 0. The general formula to calculate the address of any element arr[i] is:
```c

Address(arr[i]) = BaseAddress + (i * SizeOfElement)


```
- For example, to access the third element (arr[2]):
```c
------------------------------------------------------------------------------------------------
Address(arr[2]) = 0x1000 + (2 * 4) = 0x1008
------------------------------------------------------------------------------------------------

```
### 4. Example Code
- Here is a complete example in C that demonstrates the declaration, initialization, and accessing of an array:
```c
#include <stdio.h>

int main() {
    // Declaration and initialization
    int arr[5] = {1, 2, 3, 4, 5};

    // Accessing elements
    printf("Element at index 0: %d\n", arr[0]);
    printf("Element at index 1: %d\n", arr[1]);
    printf("Element at index 2: %d\n", arr[2]);
    printf("Element at index 3: %d\n", arr[3]);
    printf("Element at index 4: %d\n", arr[4]);

    // Calculating addresses
    printf("Address of arr[0]: %p\n", (void*)&arr[0]);
    printf("Address of arr[1]: %p\n", (void*)&arr[1]);
    printf("Address of arr[2]: %p\n", (void*)&arr[2]);
    printf("Address of arr[3]: %p\n", (void*)&arr[3]);
    printf("Address of arr[4]: %p\n", (void*)&arr[4]);

    return 0;
}
```
```c
Output:-
Element at index 0: 1
Element at index 1: 2
Element at index 2: 3
Element at index 3: 4
Element at index 4: 5
Address of arr[0]: 0x7ffe03e4c1f0
Address of arr[1]: 0x7ffe03e4c1f4
Address of arr[2]: 0x7ffe03e4c1f8
Address of arr[3]: 0x7ffe03e4c1fc
Address of arr[4]: 0x7ffe03e4c200

```

- This line prints the address of the first element of the array. The %p format specifier is used to print the address. (void*)&arr[0] is used to cast the address 
 to void* for proper format.

## 2. Two-Dimensional Arrays
 Two-dimensional arrays can be visualized as a table with rows and columns.

Declaration and Initialization
```c
------------------------------------------------------------------------------------------------
int arr[3][4] = {
    {1, 2, 3, 4},
    {5, 6, 7, 8},
    {9, 10, 11, 12}
};
------------------------------------------------------------------------------------------------

```

- This creates a 3x4 matrix.

### Memory Representation
- In memory, a two-dimensional array is stored in row-major order, meaning all elements of the first row are stored first, followed by the elements of the second 
 row, and so on.
```c
------------------------------------------------------------------------------------------------

Address      Value
0x1000       1
0x1004       2
0x1008       3
0x100C       4
0x1010       5
0x1014       6
0x1018       7
0x101C       8
0x1020       9
0x1024       10
0x1028       11
0x102C       12
------------------------------------------------------------------------------------------------

```

### Accessing Elements

- The general formula to calculate the address of an element arr[i][j] in a 2D array is:
```c
 Address(arr[i][j]) = BaseAddress + (i * NumberOfColumns + j) * SizeOfElement
```
- For example, to access arr[1][2] (element 7):
```
Address(arr[1][2]) = 0x1000 + (1 * 4 + 2) * 4 = 0x1018
```
### Example for Acesss
```c
#include <stdio.h>

int main() {

    int myArray[3][4] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12}
    };

    // Access and print elements in the array
    printf("Element at (0, 0): %d\n", myArray[0][1]); // Output: 1
    printf("Element at (1, 2): %d\n", myArray[2][2]); // Output: 7

    return 0;
}
 
 //Address(arr[i][j]) = BaseAddress + (i * NumberOfColumns + j) * SizeOfElement

```
### Modify the array
```c
#include <stdio.h>

int main() {
    // Declare and initialize a 3x4 array
    int myArray[3][4] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12}
    };

    // Access and print specific elements
    printf("Element at (0, 0): %d\n", myArray[0][0]); // Output: 1
    printf("Element at (1, 2): %d\n", myArray[1][2]); // Output: 7

    // Modify an element
    myArray[2][3] = 15;

    // Print the modified array
    printf("\nAfter modification:\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++) {
            printf("Element at (%d, %d): %d\n", i, j, myArray[i][j]);
        }
    }

    return 0;
}


```
### Example Code
```c
#include <stdio.h>

int main() {
    int arr[3][4] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12}
    };

    // Accessing elements
    printf("Element at arr[0][0]: %d\n", arr[0][0]);
    printf("Element at arr[1][2]: %d\n", arr[1][2]);
    printf("Element at arr[2][3]: %d\n", arr[2][3]);

    // Calculating addresses
    printf("Address of arr[0][0]: %p\n", (void*)&arr[0][0]);
    printf("Address of arr[1][2]: %p\n", (void*)&arr[1][2]);
    printf("Address of arr[2][3]: %p\n", (void*)&arr[2][3]);

    return 0;
}
```
## 3. Multi-Dimensional Arrays
- Multi-dimensional arrays are an extension of two-dimensional arrays. They can be thought of as arrays of arrays.

- Declaration and Initialization
```c
------------------------------------------------------------------------------------------------
int arr[2][3][4] = {
    {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12}
    },
    {
        {13, 14, 15, 16},
        {17, 18, 19, 20},
        {21, 22, 23, 24}
    }
};
------------------------------------------------------------------------------------------------

```
- This creates a 2x3x4 array.

## Memory Representation
- In memory, a three-dimensional array is stored in row-major order, with the first index varying the slowest, and the last index varying the fastest.

- For the array arr, the memory representation might look like this:
```c
------------------------------------------------------------------------------------------------
Address      Value
0x1000       1
0x1004       2
0x1008       3
...
0x102C       12
0x1030       13
...
0x1068       24
------------------------------------------------------------------------------------------------

```

### Accessing Elements
- The general formula to calculate the address of an element arr[i][j][k] in a 3D array is:
```c
Address(arr[i][j][k]) = BaseAddress + ((i * NumberOfRows * NumberOfColumns) + (j * NumberOfColumns) + k) * SizeOfElement
```
- For example, to access arr[1][2][3] (element 24):
```c
Address(arr[1][2][3]) = 0x1000 + ((1 * 3 * 4) + (2 * 4) + 3) * 4 = 0x1068
```
```c
Address(arr[1][2][3]) = 0x1000 + ((1 * 3 * 4) + (2 * 4) + 3) * 4 = 0x1068
```
## Example code
```c
#include <stdio.h>

int main() {
    int arr[2][3][4] = {
        {
            {1, 2, 3, 4},
            {5, 6, 7, 8},
            {9, 10, 11, 12}
        },
        {
            {13, 14, 15, 16},
            {17, 18, 19, 20},
            {21, 22, 23, 24}
        }
    };

    // Accessing elements
    printf("Element at arr[0][0][0]: %d\n", arr[0][0][0]);
    printf("Element at arr[1][2][3]: %d\n", arr[1][2][3]);

    // Calculating addresses
    printf("Address of arr[0][0][0]: %p\n", (void*)&arr[0][0][0]);
    printf("Address of arr[1][2][3]: %p\n", (void*)&arr[1][2][3]);

    return 0;
}
```


## Array Opearion

### Traversal
```c
#include <stdio.h>

int main() {
    int arr[5] = {1, 2, 3, 4, 5};
    printf("Array elements: ");
    for (int i = 0; i < 5; i++) {
        printf("%d ", arr[i]); // Printing all elements
    }
    printf("\n");
    return 0;
}
```

### Insertion
```c
#include <stdio.h>

int main() {
    int arr[10] = {1, 2, 3, 4, 5};  // Array with 10 capacity but 5 elements
    int n = 5; // Number of elements
    int pos = 2;
    int elem = 10;

    printf("Array before insertion: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    // Insertion
    for (int i = n; i > pos; i--) {
        arr[i] = arr[i - 1]; // Shift elements to the right
    }
    arr[pos] = elem; // Insert element at pos
    n++; // Increment number of elements

    printf("Array after insertion of %d at position %d: ", elem, pos);
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}

```

### Deletion
```c
#include <stdio.h>

int main() {
    int arr[5] = {1, 2, 3, 4, 5};
    int n = 5; // Number of elements
    int del_pos = 3;

    printf("Array before deletion: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    // Deleting elements
    for (int i = del_pos; i < n - 1; i++) {
        arr[i] = arr[i + 1]; // Shift elements to the left
    }
    n--; // Decrement number of elements

    printf("Array after deletion at position %d: ", del_pos);
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}

```
### Searching
```c
#include <stdio.h>

int main() {
    int arr[5] = {1, 2, 3, 4, 5};
    int n = 5; // Number of elements
    int target = 3;
    int found = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] == target) {
            found = 1;
            break;
        }
    }
    if (found) {
        printf("Element %d found\n", target);
    } else {
        printf("Element %d not found\n", target);
    }
    return 0;
}
```

![Uploading image.png…]()

