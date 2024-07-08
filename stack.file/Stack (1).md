# Stack
- In fact, Stack is more of behaviour of structure than being a structure itself. We can turn a regular array (either static or dynamic) into a stack with simple modification. Stack is an Abstract Data Type (ADT) they may have different implementations:

- A stack is a linear data structure that follows the principle of Last In First Out (LIFO). This means the last element inserted inside the stack is removed first.

- You can think of the stack data structure as the pile of plates on top of another.

- Let’s take an exmaple

- Let’s say you have a stack of plates in this order: purple, red, orange, blue, pink. So the purple plate in the bottom and the pink on the top.
 You have to start from the top if you want to remove a plate. so if you need to remove the purple plate, you have to remove the pink, blue, orange, red then the 
 purple.

- ![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/44ee27db-25df-486a-92ec-c16b7ed7ff8c)

- So finally, we can say. A stack is a way to store data where the last item added is the first one that can be removed. You can only add or remove items from the 
 top of the stack.
- Obviously! The first element you put in a stack is the last one to come out. The “Last In, First Out” (LIFO) rule governs this. Similarly, the last thing you 
 put in is the first thing you may take out.
- As a result, in a stack, element insertion and deletion always occur at the top. You can add new components to the top of the stack and delete elements from the 
 top of the stack. The remainder of the components under the top are unaffected.
- A stack data structure is distinguished by its Last In First Out behaviour and the ability to insert and delete components only from the top.

## There are two common ways to implement a stack
### 1. Statically using an array

- You allocate a fixed-size array to contain the stack components in this procedure.
- The array acts as the stack’s underlying data structure.
- To keep track of the top element and the number of elements in the stack, you use the variable “top.”
- By incrementing the top variable and saving the new element at that position, you may push (add) elements to the stack.
- Similarly, you may pop (remove) elements from the stack by accessing the top element and decrementing the top variable.
- The stack size is constant and cannot be adjusted dynamically, which is one disadvantage of this strategy.

### 2. Dynamically using a linked list.

- To implement the stack in this approach, you utilise a linked list.
- Each node in the linked list represents a stack element and contains the actual data as well as a reference to the next node.
- The linked list’s head represents the top of the stack.
- To push an element, you build a new node, assign it a data value, and make it the linked list’s new head.
- Popping an element involves removing the head node and updating the head pointer to the next node in the list.
- The advantage of this strategy is that the stack may dynamically increase or decrease depending on the number of items.

- This table should draw the boundaries between Abstract Data Types (ADT) and Concrete Data Types, and keep in mind that Abstract Data Types are built upon 
 Concrete Data Types.Here, you can:

- Put a new plate on top
- Remove the top plate
- And, if you want the plate at the bottom, you must first remove all the plates on top. This is exactly how the stack data structure works.

## LIFO Principle of Stack
- In programming terms, putting an item on top of the stack is called push and removing an item is called pop.

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/2398ab90-c65d-440d-a1c9-2ee940b4b5a2)

- In the above image, although item 3 was kept last, it was removed first. This is exactly how the LIFO (Last In First Out) Principle works.

- We can implement a stack in any programming language like C, C++, Java, Python or C#, but the specification is pretty much the same.

## Working of Stack Data Structure
- The operations work as follows:

- A pointer called TOP is used to keep track of the top element in the stack.
- When initializing the stack, we set its value to -1 so that we can check if the stack is empty by comparing TOP == -1.
- On pushing an element, we increase the value of TOP and place the new element in the position pointed to by TOP.
- On popping an element, we return the element pointed to by TOP and reduce its value.
- Before pushing, we check if the stack is already full
- Before popping, we check if the stack is already empty

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/8a4ff325-fb71-411a-8597-92917bc3f4b1)



| Abstract Data Type (ADT) | Possible Implementations |
|--------------------------|--------------------------|
| Stack                    | Array or Linked List     |
| Queue                    | Array or Linked List     |


### Stack Array Implementation:
- A Stack is a Data Structure that implements the LIFO (last in first out) way of getting the data in and out. So, we insert on top and get from top. Exactly the same way as we would stack books. We can’t get a 
 book that is not on the top, without getting the others on top of it before. We define a stack again as a struct that has to have:

- an static Array that contains the Stack Data the top index of the Stack Array, where the last Item sits We could also include capacity, if we make it pseudodynamic.

-To keep it simple I will only talk about Integer Arrays. So, an struct of an Stack will look like this:

```c
#define MAX_SIZE 100 // Maximum size of the stack

// Structure to represent the stack
typedef struct {
    int data[MAX_SIZE]; // Array to hold the stack elements
    int top; // Index of the top element
} Stack;
```

### Operation Operation 

| Operation      | Description                                          |
|----------------|------------------------------------------------------|
| Push           | Add an element to the top of the stack.              |
| Pop            | Remove and return the top element from the stack.    |
| Peek/Top       | Return the top element without removing it.          |
| isEmpty        | Check if the stack is empty.                         |
| isFull         | Check if the stack is full (for fixed-size stacks).  |
| Initialize     | Initialize the stack to make it ready for use.       |

### Array Representation of a Stack
- 1.Define the Maximum Size: Set a maximum size for the stack.
 Initialize the Stack: Create a structure to hold the stack elements and the top index.
- 2.Operations:
  Push: Add an element to the top of the stack.
  Pop: Remove and return the top element of the stack.
  Peek: Return the top element without removing it.
  isEmpty: Check if the stack is empty.
  isFull: Check if the stack is full.
- 3.Display: Print all elements in the stack


### Opertation and Array represntation in stack
```c
#include <stdio.h>

void push();
void pop();
void peek();
void search();
void display();

int a[100], top = -1;

int main() {
    int x;
    while (1) {
        printf("\n0 or CTRL-C to Exit ");
        printf("\n1. Push");
        printf("\n2. Pop");
        printf("\n3. Peek");
        printf("\n4. Search");
        printf("\n5. Display");
        printf("\nEnter your choice? \n");
        scanf("%d", &x);
        switch (x) {
            case 0:
                return 0;
            case 1:
                push();
                break;
            case 2:
                pop();
                break;
            case 3:
                peek();
                break;
            case 4:
                search();
                break;
            case 5:
                display();
                break;
            default:
                printf("\nInvalid choice,\nPlease try again.\n");
        }
    }
    return 0;
}

// function for pushing the element
void push() {
    int n = 0;
    printf("\nEnter the value to be inserted: ");
    scanf("%d", &n);
    top += 1;
    a[top] = n;
}

// function for popping the element out
void pop() {
    if (top == -1) {
        printf("\nStack is empty");
    } else {
        int item;
        item = a[top];
        top -= 1;
        printf("\nPopped item is %d ", item);
    }
}

// function for peeking the element from top of the stack
void peek() {
    if (top >= 0)
        printf("\nThe top element is %d", a[top]);
    else
        printf("\nStack is empty");
}

// function to search for an element in the stack
void search() {
    int key, found = 0;
    printf("\nEnter the element to search: ");
    scanf("%d", &key);
    for (int i = top; i >= 0; i--) {
        if (a[i] == key) {
            printf("\nElement %d found at position %d from top.", key, top - i + 1);
            found = 1;
            break;
        }
    }
    if (!found)
        printf("\nElement %d not found in the stack.", key);
}

// function to view entire stack
void display() {
    if (top == -1) {
        printf("\nStack is empty");
    } else {
        printf("\nStack elements:\n");
        for (int i = top; i >= 0; i--) {
            printf("%d\n", a[i]);
        }
    }
}


```
### Time Complexity of Stack Operations
- The time complexity of the several stack operations are:

### Push Operation: O(1)
- The time complexity of the Pop operation would be O(1) as in this operation, we are inserting an element at the top of the stack only.

### Pop Operation: O(1)
- The time complexity of the Push operation would be O(1) as in this operation, we are removing and returning an element from the top of the stack only.

### Peek Operation: O(1)
- The time complexity of the Peek operation would be O(1) as in this operation, we are returning only the topmost element of the stack.

### IsEmpty Operation: O(1)- The time complexity of the IsEmpty operation would be O(1) as in this operation, we are checking whether the topmost element is null or not.

### IsFull Operation: O(1)
- The time complexity of the IsFull operation would be O(1) as in this operation, we are checking whether the topmost element is at the maximum position or not.
- 
## Stacks using Dynamic Arrays
- Array in C is static in nature, so its size should be known at compile time and we can’t change the size of the array after its declaration. Due to this, we may encounter situations where our array doesn’t 
 have enough space left for required elements or we allotted more than the required memory leading to memory wastage. To solve this problem, dynamic arrays come into the picture.

- A Dynamic Array is allocated memory at runtime and its size can be changed later in the program.

- We can create a dynamic array in C by using the following methods:
- 1.Using malloc() Function
- 2.Using calloc() Function
- 3.Resizing Array Using realloc() Function
- 4.Using Variable Length Arrays(VLAs)
- 5.Using Flexible Array Members
- 6.free

# Example for Stack using Dynamic Arrays
```c

#include <stdio.h>
#include <stdlib.h>

void push();
void pop();
void peek();
void search();
void display();

int *a = NULL;
int top = -1;
int capacity = 2; // Initial capacity

int main() {
    a = (int*)malloc(capacity * sizeof(int));
    if (a == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }

    int x;
    while (1) {
        printf("\n0 or CTRL-C to Exit ");
        printf("\n1. Push");
        printf("\n2. Pop");
        printf("\n3. Peek");
        printf("\n4. Search");
        printf("\n5. Display");
        printf("\nEnter your choice? \n");
        scanf("%d", &x);
        switch (x) {
            case 0:
                free(a); // Free the allocated memory before exiting
                return 0;
            case 1:
                push();
                break;
            case 2:
                pop();
                break;
            case 3:
                peek();
                break;
            case 4:
                search();
                break;
            case 5:
                display();
                break;
            default:
                printf("\nInvalid choice,\nPlease try again.\n");
        }
    }
    return 0;
}

// function for pushing the element
void push() {
    int n;
    printf("\nEnter the value to be inserted: ");
    scanf("%d", &n);
    
    // Check if the capacity needs to be increased
    if (top == capacity - 1) {
        capacity *= 2;
        int *temp = realloc(a, capacity * sizeof(int));
        if (temp == NULL) {
            printf("\nMemory allocation failed");
            free(a); // Free the existing memory before exiting
            exit(1);
        }
        a = temp;
    }
    
    a[++top] = n;
}

// function for popping the element out
void pop() {
    if (top == -1) {
        printf("\nStack is empty");
    } else {
        int item = a[top--];
        printf("\nPopped item is %d", item);
    }
}

// function for peeking the element from top of the stack
void peek() {
    if (top >= 0)
        printf("\nThe top element is %d", a[top]);
    else
        printf("\nStack is empty");
}

// function to search for an element in the stack
void search() {
    int key, found = 0;
    printf("\nEnter the element to search: ");
    scanf("%d", &key);
    for (int i = top; i >= 0; i--) {
        if (a[i] == key) {
            printf("\nElement %d found at position %d from top.", key, top - i + 1);
            found = 1;
            break;
        }
    }
    if (!found)
        printf("\nElement %d not found in the stack.", key);
}

// function to view entire stack
void display() {
    if (top == -1) {
        printf("\nStack is empty");
    } else {
        printf("\nStack elements:\n");
        for (int i = top; i >= 0; i--) {
            printf("%d\n", a[i]);
        }
    }
}



```

### Initial Setup
- Initial Memory Allocation:
- The initial capacity of the stack is set to 2.
- malloc allocates memory for 2 integers: a = (int*)malloc(capacity * sizeof(int));
- At this point, the memory allocated can hold 2 integers.
~~~c
capacity = 2;
top = -1;
a = [_, _]  // memory for 2 integers
~~~

### Pushing Elements
- Push 1st Element:
- Value: 10
- The top index is incremented from -1 to 0.
- The element is stored at index 0.
~~~c
top = 0;
a = [10, _]

~~~
### Push 2nd Element:
- Value: 20
- The top index is incremented from 0 to 1.
- The element is stored at index 1.
~~~c
top = 1;
a = [10, 20]
~~~
### Push 3rd Element:
Value: 30
- The top index is incremented from 1 to 2.
- The current capacity is 2 and top index is now equal to capacity - 1.
- realloc is called to double the capacity to 4.
- Memory is reallocated to hold 4 integers.
- The element is stored at index 2
~~~c
capacity = 4;
top = 2;
a = [10, 20, 30, _]  // memory for 4 integers
~~~
### Push 4th Element:
- Value: 40
- The top index is incremented from 2 to 3.
- The element is stored at index 3
~~~c
top = 3;
a = [10, 20, 30, 40]
~~~
### Push 5th Element:
- Value: 50
- The top index is incremented from 3 to 4.
- The current capacity is 4 and top index is now equal to capacity - 1.
- realloc is called to double the capacity to 8.
- Memory is reallocated to hold 8 integers.
- The element is stored at index 4
~~~c
capacity = 8;
top = 4;
a = [10, 20, 30, 40, 50, _, _, _]  // memory for 8 integers
~~~




### Reloc calculation how much block or byte it create

-To understand how realloc dynamically adjusts the memory allocation for the stack, let's go through the calculations    of memory blocks or bytes created during the process.

- Initial Setup
- Initial Memory Allocation:
~~~c
Initial capacity: 2
Each integer typically requires 4 bytes.
Initial memory allocated: capacity * sizeof(int) = 2 * 4 bytes = 8 bytes.
Dynamic Resizing
When we use realloc, the memory allocation follows this pattern: every time the stack is full, the capacity doubles.

Push Operations and Resizing
Initial Allocation:

capacity = 2
Memory allocated: 2 * sizeof(int) = 2 * 4 bytes = 8 bytes
a = [_, _] (8 bytes allocated)
Push 1st Element (10):

No resizing needed.
Memory remains 8 bytes.
Push 2nd Element (20):

No resizing needed.
Memory remains 8 bytes.
Push 3rd Element (30):

Stack is full. top is 1, capacity - 1 is 1.
Capacity doubles from 2 to 4.
realloc increases the memory:
New capacity: 4
Memory allocated: 4 * sizeof(int) = 4 * 4 bytes = 16 bytes
a = [10, 20, 30, _] (16 bytes allocated)
Push 4th Element (40):

No resizing needed.
Memory remains 16 bytes.
Push 5th Element (50):

Stack is full. top is 3, capacity - 1 is 3.
Capacity doubles from 4 to 8.
realloc increases the memory:
New capacity: 8
Memory allocated: 8 * sizeof(int) = 8 * 4 bytes = 32 bytes
a = [10, 20, 30, 40, 50, _, _, _] (32 bytes allocated)
~~~
### Stack Applications: Polish notation, Infix to postfix conversion, evaluation of postfix expression.

- Stacks are crucial in solving various problems, including arithmetic expression evaluation and conversion between different notations like infix, postfix, and 
 prefix. Here's how you can implement the stack applications you mentioned:

### Polish Notation (Prefix Notation)
- In Polish notation, also known as prefix notation, the operator precedes their operands.

- Example: + 2 3 is equivalent to 2 + 3

### Infix to Postfix Conversion
- Infix notation is the common arithmetic and logical formula notation, in which operators are written between operands.

- Example: 2 + 3 * 4 is in infix notation.

### Postfix notation, also known as Reverse Polish Notation (RPN), is where every operator follows all of its operands.

- Example: 2 3 4 * + is equivalent to 2 + 3 * 4.

### Evaluation of Postfix Expression
- To evaluate a postfix expression, you can use a stack to keep track of operands and apply operators when encountered.

```c
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>  // For isdigit()

#define MAX_SIZE 100

// Stack structure
typedef struct {
    int top;
    int items[MAX_SIZE];
} Stack;

// Function to initialize the stack
void initStack(Stack *s) {
    s->top = -1;
}

// Function to check if the stack is empty
int isEmpty(Stack *s) {
    return s->top == -1;
}

// Function to check if the stack is full
int isFull(Stack *s) {
    return s->top == MAX_SIZE - 1;
}

// Function to push an element onto the stack
void push(Stack *s, int value) {
    if (isFull(s)) {
        printf("Stack overflow\n");
        exit(1);
    }
    s->items[++(s->top)] = value;
}

// Function to pop an element from the stack
int pop(Stack *s) {
    if (isEmpty(s)) {
        printf("Stack underflow\n");
        exit(1);
    }
    return s->items[(s->top)--];
}

// Function to evaluate a postfix expression
int evaluatePostfix(char *exp) {
    Stack stack;
    initStack(&stack);

    for (int i = 0; exp[i] != '\0'; i++) {
        if (isdigit(exp[i])) {
            push(&stack, exp[i] - '0');
        } else {
            int operand2 = pop(&stack);
            int operand1 = pop(&stack);
            switch (exp[i]) {
                case '+':
                    push(&stack, operand1 + operand2);
                    break;
                case '-':
                    push(&stack, operand1 - operand2);
                    break;
                case '*':
                    push(&stack, operand1 * operand2);
                    break;
                case '/':
                    push(&stack, operand1 / operand2);
                    break;
                default:
                    printf("Invalid operator\n");
                    exit(1);
            }
        }
    }

    return pop(&stack);
}

int main() {
    char exp[] = "23*4+"; // Postfix expression: 2*3+4
    printf("Postfix expression: %s\n", exp);
    printf("Result: %d\n", evaluatePostfix(exp));
    return 0;
}
```

## Stack Time Complexity
- For the array-based implementation of a stack, the push and pop operations take constant time, i.e. O(1).

## Applications of Stack Data Structure
- Although stack is a simple data structure to implement, it is very powerful. The most common uses of a stack are:

- To reverse a word - Put all the letters in a stack and pop them out. Because of the LIFO order of stack, you will get the letters in reverse order.
 
- In compilers - Compilers use the stack to calculate the value of expressions like 2 + 4 / 5 * (7 - 9) by converting the expression to prefix or postfix form.
 In browsers - The back button in a browser saves all the URLs you have visited previously in a stack. Each time you visit a new page, it is added on top of the stack. When you press the back button, the current 
 URL is removed from the stack, and the previous URL is accessed.

### stack overflow
- A stack is a type of data structure that operates on the Last-In-First-Out (LIFO) principle. It’s usually done with an array or linked list. Elements are added 
 or taken from one end of a stack, which is generally referred to as the “top” of the stack.
- The maximum number of items that can be stored in static memory allocation in a stack is predetermined. Assume we have a stack with a capacity of 100 items.
 A stack overflow problem, often known as “stack full,” happens when the stack has reached its limit and no more components may be added. This signifies that 
 there is no room on the stack for additional components.
- In other words, attempting to push (insert) an element onto an already full stack would result in a stack overflow. The stack cannot accommodate the additional 
 element since it has surpassed its capacity.
- When a stack overflow occurs, it signals that the stack has reached its limit and that any further additions would result in an error. It is critical to handle 
 this scenario correctly to avoid data loss or program failures.


### This is the stack overflow😂


![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/3f490d8a-eae0-42b1-a89c-d5f266b8ef85)


### stack unoverflow
- A stack is a data structure that adheres to the Last-In-First-Out (LIFO) principle, in which components are added or deleted from one end of the stack, which is 
 generally referred to as the “top” of the stack.
- In the instance of stack underflow, it refers to the situation in which we attempt to conduct an action on the stack, such as displaying or deleting elements, 
 but there are no elements in the stack.
- Assume we have an empty stack and attempt to conduct a pop operation to remove an element from the stack. We cannot remove any components from the stack since 
 there are none, resulting in a stack underflow scenario.
- Similarly, attempting to display the items of an empty stack with no elements introduced results in a stack underflow condition.
- Stack underflow is so named because it implies that the stack lacks enough components to accomplish the intended action. It is critical to handle this 
- circumstance correctly in order to avoid mistakes or unexpected behaviour in the program.
### It’s like a boy is trying to drink an empty glass😂
 ![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/7ce0fb6f-5b68-4790-812f-bca9d33c903e)

### recursive
- A function that calls itself is known as a recursive function. And, this technique is known as recursion.
- Recursion is a powerful programming technique where a function calls itself to solve smaller instances of a problem until it reaches a base case. Here are 
  implementations of some common recursive algorithms:

### How recursion works?

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/1d67bb51-f2d5-4bb8-b386-583faac10704)

```c
void recurse()
{
    ... .. ...
    recurse();
    ... .. ...
}

int main()
{
    ... .. ...
    recurse();
    ... .. ...
}
```
![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/735f64dc-4e3e-47ce-a317-7483429e4a36)

## Factorial
- Factorial of a non-negative integer n, denoted as n!, is the product of all positive integers less than or equal to n.
```c
#include <stdio.h>

// Recursive function to calculate factorial
int factorial(int n) {
    if (n == 0 || n == 1)
        return 1;
    else
        return n * factorial(n - 1);
}

int main() {
    int n = 5;
    printf("Factorial of %d is %d\n", n, factorial(n));
    return 0;
}
```
## GCD (Greatest Common Divisor)
- The greatest common divisor (GCD) of two integers a and b is the largest positive integer that divides both a and b without leaving a remainder.
```c
#include <stdio.h>

// Recursive function to find GCD
int gcd(int a, int b) {
    if (b == 0)
        return a;
    else
        return gcd(b, a % b);
}

int main() {
    int a = 12, b = 18;
    printf("GCD of %d and %d is %d\n", a, b, gcd(a, b));
    return 0;
}
```
![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/2a4305f6-6d8a-4d69-af3c-fae9fe5bd45b)

# Fibonacci Sequence
- The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.
```c
#include <stdio.h>

// Function declaration
int fib(int);

// Main function
int main() {
    int i, n;
    
    printf("Enter the number of terms in Fibonacci series: ");
    scanf("%d", &n);
    
    printf("First %d numbers in Fibonacci series: ", n);
    for (i = 0; i < n; i++) {
        printf("%d ", fib(i));
    }
    
    // Wait for user to press Enter before exiting
    printf("\nPress Enter to exit...");
    getchar(); // Wait for a character input (Enter key)
    
    return 0;
}

// Recursive function to calculate Fibonacci number
int fib(int x) {
    if (x == 0) {
        return 0;
    } else if (x == 1) {
        return 1;
    } else {
        return (fib(x - 1) + fib(x - 2));
    }
}

```

## Tower of Hanoi
- The Tower of Hanoi is a mathematical puzzle where you have three pegs and a number of disks of different sizes which can be slid onto any peg. The puzzle starts 
 with the disks in a neat stack in ascending order of size on one peg, the smallest at the top.
```c
#include <stdio.h>

// Recursive function to solve Tower of Hanoi
void towerOfHanoi(int n, char from, char to, char aux) {
    if (n == 1) {
        printf("Move disk 1 from %c to %c\n", from, to);
        return;
    }
    towerOfHanoi(n - 1, from, aux, to);
    printf("Move disk %d from %c to %c\n", n, from, to);
    towerOfHanoi(n - 1, aux, to, from);
}

int main() {
    int n = 3; // Number of disks
    towerOfHanoi(n, 'A', 'C', 'B'); // A, B, and C are the names of the pegs
    return 0;
}
```
