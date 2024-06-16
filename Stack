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

### Array implementation
- Determining the size of the stack prior to the program run is very important.
- In the array implementation of a stack, inserting an element is known as “pushing” an element onto the stack. When you push an element, it gets added to the 
 stack’s top. This signifies that the element will be placed at the index indicated by the “top” variable at the time.
- Assume we have an array-based stack with the entries [5, 8, 12, 3]. The variable “top” originally points to index 3, which has the value 3. Now we want to add 
 element 10 to the stack. We raise the “top” variable and add the new element to the freshly updated index. After pushing 10, the stack looks like this: [5, 8, 
 12, 3, 10]. The variable “top” now points to index 4, which has a value of 10.
- When you push an element into the stack, all of the current elements retain their places, but the “top” variable is modified to reflect the new topmost element.


![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/28e6d1da-1853-43e3-ab11-23fb14a793a4)

## Algorithm for pushing

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/98c8a408-fa99-4d9c-916c-36d0f3a2d405)

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
## Basic Operations of Stack
- There are some basic operations that allow us to perform different actions on a stack.

- Push: Add an element to the top of a stack
- Pop: Remove an element from the top of a stack
- IsEmpty: Check if the stack is empty
- IsFull: Check if the stack is full
- Peek: Get the value of the top element without removing it

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

```c
// Stack implementation in C

#include <stdio.h>
#include <stdlib.h>

#define MAX 10

int count = 0;

// Creating a stack
struct stack {
int items[MAX];
int top;
};
typedef struct stack st;

void createEmptyStack(st *s) {
s->top = -1;
}

// Check if the stack is full
int isfull(st *s) {
if (s->top == MAX - 1)
return 1;
else
return 0;
}

// Check if the stack is empty
int isempty(st *s) {
if (s->top == -1)
return 1;
else
return 0;
}

// Add elements into stack
void push(st *s, int newitem) {
if (isfull(s)) {
printf("STACK FULL");
} else {
s->top++;
s->items[s->top] = newitem;
}
count++;
}

// Remove element from stack
void pop(st *s) {
if (isempty(s)) {
printf("\n STACK EMPTY \n");
} else {
printf("Item popped= %d", s->items[s->top]);
s->top--;
}
count--;
printf("\n");
}

// Print elements of stack
void printStack(st *s) {
printf("Stack: ");
for (int i = 0; i < count; i++) {
printf("%d ", s->items[i]);
}
printf("\n");
}

// Driver code
int main() {
int ch;
st *s = (st *)malloc(sizeof(st));

createEmptyStack(s);

push(s, 1);
push(s, 2);
push(s, 3);
push(s, 4);

printStack(s);

pop(s);

printf("\nAfter popping out\n");
printStack(s);
}

```
Output:-
```c
Stack: 1 2 3 4 
Item popped= 4

After popping out
Stack: 1 2 3
```

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
#include <stdlib.h>

#define MAX 100  // Maximum size of the stack

typedef struct {
    int data[MAX];
    int top;
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
    return s->top == MAX - 1;
}

// Function to push an element onto the stack
void push(Stack *s, int value) {
    if (isFull(s)) {
        printf("Stack overflow\n");
        return;
    }
    s->data[++(s->top)] = value;
}

// Function to pop an element from the stack
int pop(Stack *s) {
    if (isEmpty(s)) {
        printf("Stack underflow\n");
        return -1;
    }
    return s->data[(s->top)--];
}

// Function to peek the top element of the stack
int peek(Stack *s) {
    if (isEmpty(s)) {
        printf("Stack is empty\n");
        return -1;
    }
    return s->data[s->top];
}

// Function to display the elements of the stack
void display(Stack *s) {
    if (isEmpty(s)) {
        printf("Stack is empty\n");
        return;
    }
    for (int i = 0; i <= s->top; i++) {
        printf("%d ", s->data[i]);
    }
    printf("\n");
}

int main() {
    Stack stack;
    initStack(&stack);

    push(&stack, 10);
    push(&stack, 20);
    push(&stack, 30);

    printf("Stack elements: ");
    display(&stack);

    printf("Top element: %d\n", peek(&stack));

    printf("Popped element: %d\n", pop(&stack));

    printf("Stack elements after pop: ");
    display(&stack);

    return 0;
}

```
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
```c


```
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


### recursive
- A function that calls itself is known as a recursive function. And, this technique is known as recursion.
- Recursion is a powerful programming technique where a function calls itself to solve smaller instances of a problem until it reaches a base case. Here are 
  implementations of some common recursive algorithms:

### How recursion works?
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
# Fibonacci Sequence
- The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.
```c
#include <stdio.h>

// Recursive function to calculate Fibonacci number
int fibonacci(int n) {
    if (n <= 1)
        return n;
    else
        return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    int n = 7;
    printf("Fibonacci sequence up to %d terms: ", n);
    for (int i = 0; i < n; i++) {
        printf("%d ", fibonacci(i));
    }
    printf("\n");
    return 0;
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
