Implement Stack and its operations like push and pop
# Push Operation
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
# Push and Pop Operation

```c
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

#define SIZE 40

char stack[SIZE];
int top = -1;

void push(char c) {
    stack[++top] = c;
}

char pop() {
    if (top == -1)
        return '\0';
    else
        return stack[top--];
}

int precedence(char op) {
    if (op == '+' || op == '-')
        return 1;
    if (op == '*' || op == '/' || op == '%')
        return 2;
    return 0;
}

void infixToPostfix(char* infix, char* postfix) {
    int i = 0, j = 0;
    char ch, popped;

    while ((ch = infix[i++]) != '\0') {
        if (isdigit(ch)) {
            postfix[j++] = ch;
        }
        else if (ch == '(') {
            push(ch);
        }
        else if (ch == ')') {
            while ((popped = pop()) != '(')
                postfix[j++] = popped;
        }
        else {
            while (top != -1 && precedence(stack[top]) >= precedence(ch))
                postfix[j++] = pop();
            push(ch);
        }
    }

    while (top != -1)
        postfix[j++] = pop();

    postfix[j] = '\0';
}

int main() {
    char infix[SIZE], postfix[SIZE];

    printf("Enter an infix expression: ");
    scanf("%s", infix);

    infixToPostfix(infix, postfix);

    printf("Postfix expression: %s\n", postfix);

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
```c
#include <stdio.h>
#include <stdlib.h>

// Define the structure of a Node for doubly linked list
struct Node {
    int data; // The data part of the node
    struct Node *prev; // Pointer to the previous node in the list
    struct Node *next; // Pointer to the next node in the list
};

// Function to insert a node at the beginning of the doubly linked list
void insertStart(struct Node **head, int data) {
    // Allocate memory for the new node
    struct Node *newNode = (struct Node *) malloc(sizeof(struct Node));
    newNode->data = data; // Assign data to the new node
    newNode->prev = NULL; // Previous of new node is NULL
    newNode->next = *head; // Next of new node is current head

    if (*head != NULL)
        (*head)->prev = newNode; // Previous of current head is new node

    *head = newNode; // Update the head to point to the new node
}

// Function to delete a node with a specific key from doubly linked list
void deleteNode(struct Node **head, int key) {
    struct Node *temp = *head; // Temporary pointer to traverse the list

    // Find the node with the key to be deleted
    while (temp != NULL && temp->data != key) {
        temp = temp->next;
    }

    // If key was not found
    if (temp == NULL)
        return;

    // Adjust pointers for the node to be deleted
    if (temp->prev != NULL)
        temp->prev->next = temp->next;
    if (temp->next != NULL)
        temp->next->prev = temp->prev;

    // Update head if the node to be deleted is the head
    if (temp == *head)
        *head = temp->next;

    free(temp); // Free memory of the deleted node
}

// Function to search for a node with a specific key in doubly linked list
int searchNode(struct Node *head, int key) {
    struct Node *current = head; // Initialize current pointer to head
    while (current != NULL) { // Traverse the list until the end
        if (current->data == key) // If key is found
            return 1; // Return 1 indicating key is found
        current = current->next; // Move to the next node
    }
    return 0; // Return 0 indicating key is not found
}

// Function to reverse the doubly linked list
void reverseList(struct Node **head) {
    struct Node *temp = NULL;
    struct Node *current = *head;

    // Swap next and prev pointers for all nodes of the doubly linked list
    while (current != NULL) {
        temp = current->prev;
        current->prev = current->next;
        current->next = temp;
        current = current->prev; // Move to the next node
    }

    // Check if list is not empty and update head
    if (temp != NULL)
        *head = temp->prev;
}

// Function to display the doubly linked list
void display(struct Node *node) {
    struct Node *last = NULL;
    printf("\nForward Traversal: ");
    while (node != NULL) { // Traverse the list until the end
        printf("%d ", node->data); // Print the data of the current node
        last = node;
        node = node->next; // Move to the next node
    }

    printf("\nBackward Traversal: ");
    while (last != NULL) { // Traverse the list backwards
        printf("%d ", last->data); // Print the data of the current node
        last = last->prev; // Move to the previous node
    }
    printf("\n");
}

int main() {
    struct Node *head = NULL; // Initialize head pointer

    // Insert nodes at the beginning of the doubly linked list
    insertStart(&head, 15);
    insertStart(&head, 10);
    insertStart(&head, 12);
    insertStart(&head, 3);

    // Display the doubly linked list
    printf("Initial Doubly Linked List:");
    display(head);

    // Delete a node with the data value 10
    deleteNode(&head, 10);
    printf("\nAfter Deleting Element 10:\n");
    display(head);

    // Reverse the doubly linked list
    reverseList(&head);
    printf("\nAfter Reversing the List:\n");
    display(head);

    // Search for a node with the data value 12
    int key = 12;
    if (searchNode(head, key))
        printf("\nElement %d found in the list.\n", key);
    else
        printf("\nElement %d not found in the list.\n", key);

    // Search for a node with the data value 10
    key = 10;
    if (searchNode(head, key))
        printf("Element %d found in the list.\n", key);
    else
        printf("Element %d not found in the list.\n", key);

    return 0;
}
```
