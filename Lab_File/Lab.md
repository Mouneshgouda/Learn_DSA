Implement Stack and its operations like push and pop
# Push Operation
```c
#include <stdio.h>

void push();
void display();

int a[100], top = -1;

int main() {
    int x;
    while (1) {
        printf("\n0 or CTRL-C to Exit ");
        printf("\n1. Push");
        printf("\n5. Display");
        printf("\nEnter your choice? \n");
        scanf("%d", &x);
        switch (x) {
            case 0:
                return 0;
            case 1:
                push();
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
# Push and Pop Operation

```c
#include <stdio.h>
#include <stdlib.h>

#define MAX 100 // Maximum size of the stack

// Define the stack structure
typedef struct {
    int items[MAX];
    int top;
} Stack;

// Initialize the stack
void initStack(Stack *s) {
    s->top = -1;
}

// Check if the stack is full
int isFull(Stack *s) {
    return s->top == MAX - 1;
}

// Check if the stack is empty
int isEmpty(Stack *s) {
    return s->top == -1;
}

// Push an element onto the stack
void push(Stack *s, int item) {
    if (isFull(s)) {
        printf("Stack overflow\n");
        return;
    }
    s->items[++(s->top)] = item;
    printf("%d pushed to stack\n", item);
}

// Pop an element from the stack
int pop(Stack *s) {
    if (isEmpty(s)) {
        printf("Stack underflow\n");
        return -1;
    }
    return s->items[(s->top)--];
}

int main() {
    Stack s;
    initStack(&s);

    // Push elements onto the stack
    push(&s, 10);
    push(&s, 20);
    push(&s, 30);

    // Pop elements from the stack
    printf("%d popped from stack\n", pop(&s));
    printf("%d popped from stack\n", pop(&s));
    printf("%d popped from stack\n", pop(&s));

    return 0;
}
```

# peek and Search
```c
#include <stdio.h>

// Define the maximum size of the stack
#define MAX 100

// Define a stack structure
struct Stack {
    int arr[MAX];
    int top;
};

// Function to initialize the stack
void initialize(struct Stack* stack) {
    stack->top = -1;
}

// Function to push an element onto the stack
void push(struct Stack* stack, int value) {
    if (stack->top < MAX - 1) {
        stack->arr[++(stack->top)] = value;
    } else {
        printf("Stack overflow. Cannot push %d\n", value);
    }
}

// Function to peek the top element of the stack
int peek(struct Stack* stack) {
    if (stack->top == -1) {
        printf("Stack is empty\n");
        return -1;
    }
    return stack->arr[stack->top];
}

// Function to search for an element in the stack
int search(struct Stack* stack, int value) {
    if (stack->top == -1) {
        printf("Stack is empty\n");
        return -1;
    }
    for (int i = stack->top; i >= 0; i--) {
        if (stack->arr[i] == value) {
            return i; // Return the index of the found element
        }
    }
    return -1; // Return -1 if element not found
}

int main() {
    struct Stack myStack;
    initialize(&myStack);

    // Push elements onto the stack
    push(&myStack, 10);
    push(&myStack, 20);
    push(&myStack, 30);
    push(&myStack, 40);
    push(&myStack, 50);

    // Peek the top element
    int topElement = peek(&myStack);
    if (topElement != -1) {
        printf("Top element: %d\n", topElement);
    }

    // Search for an element
    int searchElement = 20;
    int index = search(&myStack, searchElement);
    if (index != -1) {
        printf("Element %d found at index %d\n", searchElement, index);
    } else {
        printf("Element %d not found in the stack\n", searchElement);
    }

    return 0;
}
```

# Final Code 
```c
#include <stdio.h>
#include <stdlib.h>

#define MAX 100 // Define the maximum size of the stack

typedef struct Stack {
    int data[MAX];
    int top;
} Stack;

void createStack(Stack *s) {
    s->top = -1; // Initialize top to -1 indicating the stack is empty
}

void push(Stack *s, int value) {
    if (s->top == MAX - 1) {
        printf("Stack Overflow!\n");
        return;
    }
    s->data[++(s->top)] = value; // Increment top and add value
}

int pop(Stack *s) {
    if (s->top == -1) {
        printf("Stack Underflow!\n");
        return -1; // Return -1 if stack is empty
    }
    return s->data[(s->top)--]; // Return the top value and decrement top
}

void traverse(Stack *s) {
    if (s->top == -1) {
        printf("Stack is empty!\n");
        return;
    }
    for (int i = 0; i <= s->top; i++) {
        printf("%d ", s->data[i]);
    }
    printf("\n");
}

int peek(Stack *s) {
    if (s->top == -1) {
        printf("Stack is empty!\n");
        return -1;
    }
    return s->data[s->top];
}

int search(Stack *s, int value) {
    for (int i = 0; i <= s->top; i++) {
        if (s->data[i] == value) {
            return i; // Return the index of the value if found
        }
    }
    return -1; // Return -1 if value is not found
}

int main() {
    Stack s;
    createStack(&s);
    
    push(&s, 10);
    push(&s, 20);
    push(&s, 30);
    
    printf("Stack after pushing 10, 20, 30:\n");
    traverse(&s);
    
    printf("Top element is %d\n", peek(&s));
    
    printf("Popping top element: %d\n", pop(&s));
    printf("Stack after popping:\n");
    traverse(&s);
    
    int value = 20;
    int index = search(&s, value);
    if (index != -1) {
        printf("Element %d found at index %d\n", value, index);
    } else {
        printf("Element %d not found\n", value);
    }
    
    return 0;
}
```
