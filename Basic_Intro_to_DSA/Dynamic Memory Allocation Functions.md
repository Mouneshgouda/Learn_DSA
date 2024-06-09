# Implementing malloc(), calloc(), realloc(), free() in c
- Dynamic memory allocation is the process of assigning the memory space during runtime of the program. This is implemented in C as the functions malloc, calloc, 
 realloc, and free from stdlib. malloc allocates a single block of memory of specified size and returns the pointer to the allocated block. calloc works similarly 
 to malloc but initializes the allocated memory to zero. realloc is used to change the size of an allocated block of memory. Free deallocates memory associated 
 with a pointer.

- In case of static memory allocation there are some drawbacks like: wastage of memory, less flexibility, permanent allocation of variables etc. To overcome 
 these situations the concept of Dynamic Memory Allocation has been introduced. In dynamic memory allocation the memories can be allocated dynamically at run time.

- There 4 library functions that are described under <stdlib.h> (Standard Library Functions)

1. malloc()
2. calloc()
3. realloc()
4. free()


### Contents
* [Approach](#approach-explained)
  * [Overview](#overview)
  * [Malloc.c](#mallocc)
  * [Free.c](#freec)
  * [Calloc.c](#callocc)
  * [Realloc.c](#reallocc)
  * [Main.c](#mainc)
* [References](#references)

## Approach Explained
### Overview
* Each of the functions are implemented in seperate files.
* The memory is being allocated as different blocks as per the requests.
* Each block of memory that is being allocated contains two sections.
* The first part contains the meta information about the block( aka meta_block) and the second part is left to use for storing data.
* Storing meta information about the block is vital and becomes handy when dealing with freeing the memory allocated.
* These blocks are maintained in the order they are being allocated.
* For this purpose, these blocks are made into a doubly linked list. 
* Keeping the list of the blocks of free space and used space as a doubly linked list comes in handy when dealing with fragmentation.
* The requested size is aligned to the multiple of 4 greater than or equal to the size. Handling the addresses becomes simpler when they are aligned. 
* The system calls `sbrk()` and `brk()` are used to move the break of the heap.  

### Malloc.c
- To allocate memory dynamically we use the function which is called as malloc() function. malloc() function on success returns the base address of the allocated 
 memory on failure it returns the NULL value. Every memory location will be initialized with a garbage value.

- Memory allocation fails if sufficient memory is not provided. Unsuccessful memory allocation returns a NULL pointer (nullptr) to the pointer.
```c
Syntax:

ptr = (datatype *)malloc((byte_size)*(number of elements))
```

```c
For example:-
ptr = (int *)malloc(sizeof(int)*10)

It will create an array of 10 elements and will return the base address of the array. Every memory location will be initialized with a garbage value. This above statement will allocate 40 bytes of memory.


```
![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/77280eb6-7a31-4a80-af10-2083d1a48be5)

* Allocates a Block of Memory of a Specified Size
* ```malloc.c``` contains the structure ```meta_block``` which stores information about the memory block.
* Every ```meta_block``` is a node in the doubly linked list. The head of the doubly linked list in maintained globally in the variable ```base```.
* It stores information such as:
  * Size of the coresponding memory block.
  * Whether the coresponding memory block is free or not.
  * The address of the next and previous node in the doubly linked list.
  * Pointer to the starting of the memory block used to store information.
  * A character array variable which does not store any value but is used to get the address from where data can be stored.
* The function ```find_suitable_block()``` when invoked finds if there exist a free block of memory with aleast the required amount of space which is free by going through the linked list.
* The function ```split_space()``` when invoked splits the memory block into two if it contains enough space that can be used to store data.
* The function ```extend_heap()``` when invoked extends the heap and adds a new memory block to the linked list.
* When the function ```malloc()``` is called:
  * Creates a new block by invoking ```extend_heap()``` if the ```base``` is ```NULL```.
  * Else it iterates through the linkedlist to find if any suitable block(block with aleast requested size).
  * If a suitable block is found, it is returned.
  * Else it extends the heap and returns the newly created block.
  * It also check if the block found in the linkedlist has enough extra space to be splited. In this case, ```split_space()``` is invoked.
 
```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *ptr;
    int n = 5;

    // Allocate memory for n integers
    ptr = (int*)malloc(n * sizeof(int));

    if (ptr == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        return 1;
    }

    // Initialize the array
    for (int i = 0; i < n; i++) {
        ptr[i] = i + 1;
    }

    // Print the array
    printf("Array allocated using malloc(): ");
    for (int i = 0; i < n; i++) {
        printf("%d ", ptr[i]);
    }
    printf("\n");

    // Free the allocated memory
    free(ptr);

    return 0;
}

```

### Free.c

- In dynamic memory allocation the memory have to be deallocated explicitly. It releases all the used memory spaces previously allocated by calloc(), malloc() or 
 realloc() functions. If we no longer need the data stored in a particular block of memory, then we should have a practice to release that memory for future use. 
 After freeing the memory blocks the memories are returned to heap.

```c
Syntax:-
free(ptr);

```

free() is used to save unused memory by freeing it. Dynamic allocation have this advantage which static allocation lacks.
* The function `free()` first checks if the pointer passed as argument is a valid pointer or not (i.e., created using malloc()) using `is_addr_valid()`.
* Then using `get_block_addr()` the address of the `meta_block` of that corresponding memory location can be found.
* The block to be freed is merged with the previous or the next memory block it any of it is free using `merge_block()`.
* If the block to be freed is at the end of the linked list, then it is removed from the linkedlist and the break of the heap is modified using `brk()`.


```c
/* C code to execute free() in DMA */
 
#include <stdio.h>
#include <stdlib.h>
 
// Driver code
int main() {
    int *p, n;     // Pointer and the variables are initialized
    printf("Enter the size of array: ");
    scanf("%d", &n);
 
    p = (int*) calloc(n, sizeof(int));  // An int array of n elements has been assigned to the pointer
     
    if(p==NULL) {
        printf("\nMemory allocation unsuccessful using calloc");
        exit(0);
    }
    else {
        printf("\nMemory allocation successful using calloc");
         
        printf("\nEnter the elements of the array: ");
        for(int i=0; i<n; ++i)
            scanf("%d", p+i);   // Array elements are taken as input
         
        printf("\nThe elements of the array: ");
        for(int i=0; i<n; ++i)
             printf("%d ", *(p + i));   // Print element of the array
       
        free(p);     //frees the space allocated in the memory
         
        printf("\nMemory has been freed successfully using free");
    }
     
    return 0;
}
```
```c
Input
Enter the size of array: 5
Enter the elements of the array: 1 2 3 4 5
```
```
Output
Memory allocation successful using calloc
The elements of the array: 1 2 3 4 5 
Memory has been freed successfully using free
```
```c
Explanation

Previously allocated memory was 5 * 4[no. of elements * sizeof(int)] = 20 bytes using calloc. By using the function “free()”, the space allocated to the memory has been deleted thereafter.
```

### Calloc.c

- Calloc stands for Contiguous Allocation. To allocate memory dynamically we also use the function which is called as calloc() function. calloc() function on 
 success returns the base address of the array and every memory location will be initialized to 0. Whereas in malloc() it was initialized by a garbage value.

- Like malloc(), memory allocation fails if sufficient memory is not provided. Unsuccessful memory allocation returns a NULL pointer (nullptr) to the pointer.
```c
Syntax:-
ptr = (data_type *)calloc(number_of_elements, element_size);
```

```c
For example, ptr=(int *)calloc(10, sizeof(int))
will create an array of 10 elements dynamically and will return the base address of the array to ptr.
Every memory location will be initialized to 0.

This above statement will allocate 40 bytes of memory. If space is insufficient then the allocation fails and NULL value is returned.
```

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/d52544d1-4a15-4905-ac14-3cda695ea6de)

* First `malloc()` is used to allocate the required amount of space.
* Then by iterating through every byte the value is set to 0.
```c
#include <stdio.h>
#include <stdlib.h>
  
// Driver code
int main() {
    int n, i;  
    int *p;   // Integer pointer is declared
      
    printf("Enter a valid range: ");
    scanf("%d", &n);
      
    p=(int *)calloc(10, sizeof(int))   // An int array of n elements has been assigned to the pointer
      
    if(p == NULL) {                  // Checking if memory allocation is successful or not
        printf("\nMemory allocation unsuccessful");
        exit(0);
    }
    else {                          // Else memory allocation is successful
        printf("\nMemory allocation successful");
        printf("\nEnter the elements of array: ");
      
        for(i=0; i<n; ++i)
            scanf("%d", p+i);   // Array elements are taken as input
      
        printf("\nElements of the array are: ");
        for(i=0; i<n; i++)
            printf("%d ", *(p+i));  // Print element of the array
    }
    return 0;
}

```
```c
Input:-
Enter a valid range: 10
Enter the elements of array: 1 2 3 4 5 6 7 8 9 10
```
```c
Output:-
Memory allocation successful
Elements of the array are: 1 2 3 4 5 6 7 8 9 10
```
### Realloc.c
- Realloc stand for Reallocation. At the time of memory allocation using calloc() or malloc(), it may be possible memory is excess or insufficient. So for that 
 reason we need to reallocate memory at the run time. realloc() is used to dynamically reallocate those memory without losing the data.

- Like malloc() and calloc(), memory allocation fails if sufficient memory is not provided. Unsuccessful memory allocation returns a NULL pointer (nullptr) to the 
 pointer.

```c
Syntax
ptr = realloc(ptr, (new_size)*(size_of_datatype));
```

```c
#include <stdio.h>
#include <stdlib.h>
  
// Driver code
int main() {
    int *p, i , d1, d2;      //pointer and the variables are initialized
    printf("Enter size: ");
    scanf("%d", &d1);
      
    p=(int *)calloc(d1, sizeof(int));   // An int array of n elements has been assigned to the pointer
      
    if(p == NULL) {                  // Checking if memory allocation is successful or not
        printf("\nMemory allocation unsuccessful");
        exit(0);
    }
    else {                          // Else memory allocation is successful
        printf("\nMemory allocation successful");
        printf("\nEnter the elements of array: ");
      
        for(i=0; i<d1; ++i)
            scanf("%d", p+i);   // Array elements are taken as input
      
        printf("\nElements of the array are: ");
        for(i=0; i<d1; ++i)
            printf("%d ", *(p+i));  // Print element of the array
             
        printf("\nEnter the new size: ");
        scanf("%d", &d2);
         
        p=realloc(p, d2*sizeof(int)); // Reallocation of memory 
         
        if(p == NULL) {                  // Checking if memory allocation is successful or not
            printf("\nMemory allocation unsuccessful using realloc");
            exit(0);
        }
        else {
            printf("\nMemory allocation successful using realloc");
            printf("\nEnter %d new elements of the array: ", d2-d1);
             
            for(i=d1; i<d2; ++i)    // Input new d2-d1 elements
                scanf("%d", p+i);  
             
            printf("\nThe final array is: ");   // Print the final array
             
            for(i=0; i<d2; ++i)
                printf("%d ", *(p+i));
        }
        free(p);
    }
    return 0;
}
```
```c
Input:-
Enter size: 5
Enter the elements of array: 1 2 3 4 5
Enter the new size: 10
Enter 5 new elements of the array: 10 20 30 40 50
```

```c
Output:-
Memory allocation successful
Elements of the array are: 1 2 3 4 5
Memory allocation successful using realloc
The final array is: 1 2 3 4 5 10 20 30 40 50
```
```c
Explanation

As per the program at first the size of the previously allocated memory block was 5. So size was = [5 * sizeof(int)]=20 bytes. Thereafter, by using the realloc() the size has been reallocated to [10 * sizeof(int)]=40 bytes.
```
![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/904379e9-9781-4036-9b2f-dc5aa81c2b35)

* If the pointer to the old address(passed as argument) is `NULL`, then malloc is used to allocate the required memory.
* If the memory block of the old address has at least the required size then it is returned as it is.
* Then the next block is checked if it free and merged using `merge_block()`.
* If the space in the block is more than required after merging, then it is split using `split_space()`.
* If the next block is not free then new block is allocated using `malloc()`. 
* The data is then copied from the old location to the new location using `copy_data()`.
* The pointer to the new location is returned.

### Main.c
 * Testing code to test all the functions implemented.
 * First two new variables are created and allocated space using `malloc()`.
 * Then the first varaible is freed and `malloc()` is called again to show that space can be reused.
 * Then `calloc()` is used to allocate an int array of size 5. Initially the values will be set to 0 by `calloc()`;
 * Then the array is resized to size 10 using `realloc()`.

P.S: Please go through the comments in the code for more techincal details on the functions.

## References
* [Linux Manual page - sbrk()](https://linux.die.net/man/2/sbrk)
* [Linux Manual page - brk()](https://man7.org/linux/man-pages/man2/brk.2.html)
* [GeeksforGeeks](https://www.geeksforgeeks.org/memory-layout-of-c-program/)
* [Malloc tutorial by Dan Luu]()
