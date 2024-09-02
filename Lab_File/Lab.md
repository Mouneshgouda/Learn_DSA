### 1.Implement Stack and its operations like push ,pop,peek,search,display


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
### Postfix Evaluation Algorithm

- Postfix Evaluation Algorithm
  Postfix evaluation algorithm is a simple algorithm that allows us to evaluate postfix expressions. The algorithm uses a stack to keep track of operands and 
  performs arithmetic operations when an operator is encountered. The algorithm can be summarized in the following steps:

- First of all, it will Create an empty stack.
- After that, it Scan the expression from left to right.
- If an operand is encountered, it push it onto the stack.
- If an operator is encountered, pop the top two operands from the stack, perform the operation, and push the result back onto the stack.
- After that, it Continue scanning the expression until all tokens have been processed.
- When the expression has been fully scanned, the result will be the top element of the stack.
- Example:
 Let's consider the expression "5 6 7 + * 8 -". We will evaluate this expression using the postfix evaluation algorithm.

### Example:

- Start scanning the expression from left to right.
- Push operand 5 onto the stack.
- Push operand 6 onto the stack.
- Push operand 7 onto the stack.
- Pop operands 7 and 6 from the stack, perform addition, and push the result (13) back onto the stack.
- Pop operands 13 and 5 from the stack, perform multiplication, and push the result (65) back onto the stack.
- Push operand 8 onto the stack.
- Pop operands 8 and 65 from the stack, perform subtraction, and push the result (57) back onto the stack.
- The final result is 57.
- 

# 1. Infix Expressions
- Infix expressions are the most usual type of expression. This notation is typically employed when writing arithmetic expressions by hand. Moreover, in the infix 
 expression, we place the operator between the two operands it operates on.

- For example, the operator “+” appears between the operands A and B in the expression “A + B”. The following figure depicts the example:

  ![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/3fe85874-89ba-4691-8b18-ab6ea7d35437)

- Furthermore, infix expressions can also include parentheses to indicate the order of operations. In this way, we should observe the operator precedence rules 
 and use parentheses to clarify the order of operations in expressions in infix notation.

- Operator precedence rules specify the operator evaluation order in an expression. So, in an expression, operators with higher precedence are evaluated before 
 operators with lower precedence.

### Some operator precedence rules follow:

- Parentheses: expressions inside parentheses are evaluated first
- Exponentiation: exponents are evaluated next
- Multiplication and division: multiplication and division are evaluated before addition and subtraction
- Addition and subtraction: finally, addition and subtraction are evaluated last
- However, if an expression has multiple operators with the same precedence, the evaluation of those operators occurs from left to right.

### 2. Prefix Expressions
- Prefix expressions, also known as Polish notation, place the operator before the operands.

- For example, in the expression “+ A B”,  we place the “+” operator before the operands A and B, as demonstrated in the image next:
- ![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/f89fa26b-8b81-4598-90a9-7ce561f7a763)
- We should consider that prefix expressions are evaluated from right to left. Thus, we apply each operator to its operands as it is encountered.

### Postfix Expressions
- Postfix expressions, also known as reverse Polish notation, where we place the operator after the operands.

- For instance, in the expression “A B +”, the “+” we place the operator after the operands A and B. The figure next depicts the example:
![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/7294a960-72fe-46e0-a4f2-7ee122e40e75)

- Hence, we can evaluate postfix expressions from left to right, with each operator being applied to its operands as encountered.


## Infix, Postfix, and Prefix Notations

| Infix                 | Postfix       | Prefix         | Notes                                                            |
|-----------------------|---------------|----------------|------------------------------------------------------------------|
| A * B + C / D         | A B * C D / + | + * A B / C D  | multiply A and B, divide C by D, add the results                  |
| A * (B + C) / D       | A B C + * D / | / * A + B C D  | add B and C, multiply by A, divide by D                          |
| A * (B + C / D)       | A B C D / + * | * A + B / C D  | divide C by D, add B, multiply by A                              |

### Algorithm for Evaluation of Postfix Expression
- Create an empty stack and start scanning the postfix expression from left to right. 

- If the element is an operand, push it into the stack.
- If the element is an operator O, pop twice and get A and B respectively. Calculate BOA and push it back to the stack.
- When the expression is ended, the value in the stack is the final answer.
- Evaluation of a postfix expression using a stack is explained in below example:
https://github.com/Gurupatil0003/DSA_Tutorial/blob/master/Img/Evaluation-of-a-postfix-expression-using-a-stack.gif
# Postfix Evalution
```c
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

#define SIZE 40 // Define the maximum size of the stack

// Function prototypes
int pop();
void push(int);

// Global variables
char postfix[SIZE]; // Array to store the postfix expression
int stack[SIZE]; // Stack array
int top = -1; // Index of the top of the stack

int main()
{
    int i, a, b, result;
    char ch;

    // Prompt the user to enter a postfix expression
    printf("Enter a postfix expression: ");
    scanf("%s", postfix); // Read the postfix expression, e.g., "89+9-8/"

    // Process each character in the postfix expression
    for(i = 0; postfix[i] != '\0'; i++)
    {
        ch = postfix[i]; // Get the current character

        // If the character is a digit, push it onto the stack
        if(isdigit(ch))
        {
            push(ch - '0'); // Convert char to int and push onto the stack
        }
        // If the character is an operator, pop two elements and apply the operator
        else if(ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == '%')
        {
            b = pop(); // Pop the top element
            a = pop(); // Pop the next top element

            // Perform the operation based on the operator
            switch(ch)
            {
                case '+': result = a + b; break;
                case '-': result = a - b; break;
                case '*': result = a * b; break;
                case '/': result = a / b; break;
                case '%': result = a % b; break;
                default: 
                    printf("Invalid operator encountered!\n");
                    exit(-1);
            }
            
            // Push the result back onto the stack
            push(result);
        }
        else
        {
            printf("Invalid character encountered in expression!\n");
            exit(-1);
        }
    }

    // Pop the final result from the stack
    result = pop();

    // Print the result of the postfix evaluation
    printf("The postfix evaluation is: %d\n", result);
    
    return 0;
}






```
### Implementation Of Infix to Postfix

```c

#include <stdio.h>      // Include standard input-output library
#include <ctype.h>      // Include ctype library for character functions

#define SIZE 40         // Define the maximum size of the stack and expression

char stack[SIZE];       // Declare stack array to store characters
int top = -1;           // Initialize top of stack to -1 indicating an empty stack

// Function to push a character onto the stack
void push(char c) {
    
    stack[++top] = c;        // Increment top and push character onto stack
}

// Function to pop a character from the stack
char pop() {
 
      return stack[top--]; // Return top character and decrement top
    }


// Function to determine precedence of operators
int precedence(char op) {
    if (op == '+' || op == '-')       // Lowest precedence
        return 1;
    if (op == '*' || op == '/' || op == '%')   // Medium precedence
        return 2;
    if (op == '^')                   // Highest precedence
        return 3;
    return 0;                        // Non-operator characters
}

// Function to convert infix expression to postfix
void infixToPostfix(char* infix, char* postfix) {
    int i = 0, j = 0;    // Initialize indices for infix and postfix arrays
    char ch, popped;

    // Process each character in the infix expression
    while ((ch = infix[i++]) != '\0') {
        if (isdigit(ch) || isalpha(ch)) {   // If operand, add to postfix
            postfix[j++] = ch;
        } else if (ch == '(') {             // If '(', push to stack
            push(ch);
        } else if (ch == ')') {             // If ')', pop until '('
            while (top != -1 && (popped = pop()) != '(') {
                postfix[j++] = popped;
            }
        } else {                            // If operator
            while (top != -1 && precedence(stack[top]) >= precedence(ch)) {
                postfix[j++] = pop();       // Pop higher or equal precedence operators
            }
            push(ch);                       // Push current operator onto stack
        }
    }

    // Pop remaining operators from the stack
    while (top != -1) {
        postfix[j++] = pop();
    }

    postfix[j] = '\0';    // Null-terminate the postfix expression
}

int main() {
    char infix[SIZE], postfix[SIZE];  // Declare arrays for infix and postfix expressions

    printf("Enter an infix expression: ");
    scanf("%s", infix);               // Read infix expression from user

    infixToPostfix(infix, postfix);   // Convert infix to postfix

    printf("Postfix expression: %s\n", postfix);  // Output the postfix expression

    return 0;                         // Exit program
}
```
```c

#include <stdio.h>
#include <stdlib.h> // header for using exit and return function

#define max 5 // symbolic constant

int rear = -1, front = -1; // global variables
int queue[max];

void enqueue();
int dequeue();
void display();
void search();

int main() {
    int w, num;
    while (1) {
        printf("\n1. enqueue");
        printf("\n2. dequeue");
        printf("\n3. Display");
        printf("\n4. Search");
        printf("\n5. EXIT");
        printf("\nEnter What you want: ");
        scanf("%d", &w);
        switch (w) {
            case 1:
                enqueue();
                break;
            case 2:
                num = dequeue();
                break;
            case 3:
                display();
                break;
            case 4:
                search();
                break;
            case 5:
                exit(1);
            default:
                printf("\nInvalid Choice!!");
        }
    }

    return 0;
}

void enqueue() {
    int num;
    if (rear == max - 1) {
        printf("\nQueue is Full!\n");
        return;
    }
    printf("\nEnter a number to insert: ");
    scanf("%d", &num);
    
    if (front == -1) {
        front = 0;  // Adjust front only if the queue is initially empty
    }
    
    rear = rear + 1;
    queue[rear] = num;
}

int dequeue() {
    int num;
    if (front == -1 || front == rear + 1) {
        printf("\nQueue is Empty!\n");
        return 0;
    }
    num = queue[front];
    printf("\n%d was deleted!\n", num);
    front = front + 1;
    return num;
}
```



```c
#include <stdio.h>
#include <stdlib.h> // for exit()

struct Node {
    int data;
    struct Node* next;
};

struct Node* rear = NULL;
struct Node* front = NULL;

void enqueue(int num);
int dequeue();
void display();
void search();

int main() {
    int w, num;
    while (1) {
        printf("\n1. Enqueue");
        printf("\n2. Dequeue");
        printf("\n3. Display");
        printf("\n4. Search");
        printf("\n5. EXIT");
        printf("\nEnter your choice: ");
        scanf("%d", &w);
        switch (w) {
            case 1:
                printf("\nEnter a number to insert: ");
                scanf("%d", &num);
                enqueue(num);
                break;
            case 2:
                num = dequeue();
                if (num != -1) {
                    printf("\n%d was deleted!\n", num);
                }
                break;
            case 3:
                display();
                break;
            case 4:
                search();
                break;
            case 5:
                exit(0);
            default:
                printf("\nInvalid Choice!!\n");
        }
    }

    return 0;
}

void enqueue(int num) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = num;
    newNode->next = NULL;
    
    if (rear == NULL) {
        rear = newNode;
        front = newNode;
    } else {
        rear->next = newNode;
        rear = newNode;
    }
}

int dequeue() {
    if (front == NULL) {
        printf("\nQueue is Empty!\n");
        return -1;
    }
    
    int num = front->data;
    struct Node* temp = front;
    front = front->next;
    free(temp);
    
    if (front == NULL) {
        rear = NULL; // Reset rear when queue becomes empty
    }
    
    return num;
}

void display() {
    if (front == NULL) {
        printf("\nQueue is Empty! Nothing to display!\n");
        return;
    }
    
    printf("\nQueue elements:\n");
    struct Node* current = front;
    while (current != NULL) {
        printf("%d\t", current->data);
        current = current->next;
    }
    printf("\n");
}


```

#### Single Linked List Operatins Insertation Deletation Searching Display,Reverse
```c
#include <stdio.h>
#include <stdlib.h>

// Define the structure of a Node
struct Node {
    int data; // The data part of the node
    struct Node *next; // Pointer to the next node in the list
};

// Function to insert a node at the beginning of the linked list
void insertStart(struct Node **head, int data) {
    // Allocate memory for the new node
    struct Node *newNode = (struct Node *) malloc(sizeof(struct Node));
    newNode->data = data; // Assign data to the new node
    newNode->next = *head; // Point the new node to the current head
    *head = newNode; // Update the head to point to the new node
}

// Function to delete a node with a specific key
void deleteNode(struct Node **head, int key) {
    struct Node *temp = *head; // Temporary pointer to traverse the list
    struct Node *prev = NULL; // Pointer to keep track of the previous node

    // If the head node itself holds the key to be deleted
    if (temp != NULL && temp->data == key) {
        *head = temp->next; // Update the head to the next node
        free(temp); // Free memory of the old head
        return;
    }

    // Traverse the list to find the key
    while (temp != NULL && temp->data != key) {
        prev = temp; // Update previous node
        temp = temp->next; // Move to the next node
    }

    // If the key was not present in the list
    if (temp == NULL) return;

    // Unlink the node from the list
    prev->next = temp->next;

    free(temp); // Free memory of the deleted node
}

// Function to search for a node with a specific key
int searchNode(struct Node *head, int key) {
    struct Node *current = head; // Initialize current pointer to head
    while (current != NULL) { // Traverse the list until the end
        if (current->data == key) // If key is found
            return 1; // Return 1 indicating key is found
        current = current->next; // Move to the next node
    }
    return 0; // Return 0 indicating key is not found
}

// Function to reverse the linked list
void reverseList(struct Node **head) {
    struct Node *prev = NULL;
    struct Node *current = *head;
    struct Node *next = NULL;

    while (current != NULL) {
        next = current->next; // Store next node
        current->next = prev; // Reverse current node's pointer
        prev = current; // Move pointers one position ahead
        current = next;
    }

    *head = prev; // Update head to point to the new first node (prev)
}

// Function to display the linked list
void display(struct Node *node) {
    while (node != NULL) { // Traverse the list until the end
        printf("%d ", node->data); // Print the data of the current node
        node = node->next; // Move to the next node
    }
    printf("\n");
}

int main() {
    struct Node *head = NULL; // Initialize head pointer
    struct Node *node2 = NULL; // Initialize node2 pointer
    struct Node *node3 = NULL; // Initialize node3 pointer
    struct Node *node4 = NULL; // Initialize node4 pointer

    // Allocate memory for the nodes
    head = (struct Node *) malloc(sizeof(struct Node));
    node2 = (struct Node *) malloc(sizeof(struct Node));
    node3 = (struct Node *) malloc(sizeof(struct Node));
    node4 = (struct Node *) malloc(sizeof(struct Node));

    // Assign data to the nodes and link them
    head->data = 15; // Data for head node
    head->next = node2; // Link head to node2

    node2->data = 10; // Data for node2
    node2->next = node3; // Link node2 to node3

    node3->data = 12; // Data for node3
    node3->next = node4; // Link node3 to node4

    node4->data = 3; // Data for node4
    node4->next = NULL; // Last node, so next is NULL

    // Display the initial linked list
    printf("Linklist: ");
    display(head);

    // Insert a new node at the beginning
    insertStart(&head, 25);

    // Display the linked list after insertion
    printf("\nAfter Inserting Element\n");
    printf("Linklist: ");
    display(head);

    // Delete a node with the data value 10
    deleteNode(&head, 10);

    // Display the linked list after deletion
    printf("\nAfter Deleting Element\n");
    printf("Linklist: ");
    display(head);

    // Reverse the linked list
    reverseList(&head);

    // Display the linked list after reversal
    printf("\nAfter Reversing the List\n");
    printf("Linklist: ");
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
#### Doubly Linked List Operatins Insertation Deletation Searching Display,Reverse

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

    if (*head != NULL) {
        (*head)->prev = newNode; // Previous of current head is new node
    }

    *head = newNode; // Update head to point to the new node
}

// Function to delete a node with a specific key from doubly linked list
void deleteNode(struct Node **head, int key) {
    struct Node *temp = *head; // Temporary pointer to traverse the list

    // Find the node with the key to be deleted
    while (temp != NULL && temp->data != key) {
        temp = temp->next; // Move to the next node
    }

    if (temp == NULL) return; // Key not found, return

    // Adjust pointers to unlink the node from the list
    if (temp->prev != NULL) {
        temp->prev->next = temp->next; // Link previous node to next node
    }
    if (temp->next != NULL) {
        temp->next->prev = temp->prev; // Link next node to previous node
    }

    if (temp == *head) {
        *head = temp->next; // Update head if deleting the first node
    }

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

    // Check if the list is empty or has only one node
    if (temp != NULL) {
        *head = temp->prev; // Update head to point to the new first node
    }
}

// Function to display the doubly linked list
void display(struct Node *head) {
    struct Node *last;

    // Forward traversal
    printf("Forward: ");
    while (head != NULL) { // Traverse the list until the end
        printf("%d ", head->data); // Print the data of the current node
        last = head; // Store the current node as last
        head = head->next; // Move to the next node
    }
    printf("\n");

    // Backward traversal
    printf("Backward: ");
    while (last != NULL) { // Traverse the list backwards using the 'last' pointer
        printf("%d ", last->data); // Print the data of the current node
        last = last->prev; // Move to the previous node
    }
    printf("\n");
}

int main() {
    // Initialize pointers to nodes
    struct Node *head = NULL;
    struct Node *node2 = NULL;
    struct Node *node3 = NULL;
    struct Node *node4 = NULL;

    // Allocate memory for each node
    head = (struct Node *) malloc(sizeof(struct Node));
    node2 = (struct Node *) malloc(sizeof(struct Node));
    node3 = (struct Node *) malloc(sizeof(struct Node));
    node4 = (struct Node *) malloc(sizeof(struct Node));

    // Assign data to each node
    head->data = 15;
    node2->data = 10;
    node3->data = 12;
    node4->data = 3;

    // Link the nodes together
    head->prev = NULL;
    head->next = node2;

    node2->prev = head;
    node2->next = node3;

    node3->prev = node2;
    node3->next = node4;

    node4->prev = node3;
    node4->next = NULL;

    // Display the doubly linked list
    printf("Doubly Linked List:\n");
    display(head);

    // Delete a node with the data value 10
    deleteNode(&head, 10);

    // Display the doubly linked list after deletion
    printf("\nAfter Deleting Element\n");
    display(head);

    // Reverse the doubly linked list
    reverseList(&head);

    // Display the doubly linked list after reversal
    printf("\nAfter Reversing the List\n");
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

BST With Creating Insertation Deletation Traversal 
```c


#include <stdio.h>
#include <stdlib.h>

// Definition of a TreeNode
typedef struct TreeNode {
    int value;
    struct TreeNode* left;
    struct TreeNode* right;
} TreeNode;

// Function to create a new node
TreeNode* createNode(int value) {
    TreeNode* newNode = (TreeNode*)malloc(sizeof(TreeNode));
    newNode->value = value;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

// Function to insert a value into the BST
TreeNode* insert(TreeNode* root, int value) {
    if (root == NULL) {
        return createNode(value);
    }
    if (value < root->value) {
        root->left = insert(root->left, value);
    } else {
        root->right = insert(root->right, value);
    }
    return root;
}

// Function to delete a node from the BST
TreeNode* deleteNode(TreeNode* root, int value) {
    if (root == NULL) {
        return root;
    }

    // Traverse the tree to find the node to delete
    if (value < root->value) {
        root->left = deleteNode(root->left, value);
    } else if (value > root->value) {
        root->right = deleteNode(root->right, value);
    } else {
        // Node with only one child or no child
        if (root->left == NULL) {
            TreeNode* temp = root->right;
            free(root);
            return temp;
        } else if (root->right == NULL) {
            TreeNode* temp = root->left;
            free(root);
            return temp;
        }

        // Node with two children: Find the minimum value node in the right subtree
        TreeNode* temp = root->right;
        while (temp && temp->left != NULL) {
            temp = temp->left;
        }

        // Copy the inorder successor's content to this node
        root->value = temp->value;

        // Delete the inorder successor
        root->right = deleteNode(root->right, temp->value);
    }
    return root;
}

// Function to perform in-order traversal
void inorderTraversal(TreeNode* root) {
    if (root != NULL) {
        inorderTraversal(root->left);
        printf("%d ", root->value);
        inorderTraversal(root->right);
    }
}

int main() {
    TreeNode* root = NULL;

    // Inserting values into the BST
    root = insert(root, 50);
    insert(root, 30);
    insert(root, 70);
    insert(root, 20);
    insert(root, 40);
    insert(root, 60);
    insert(root, 80);

    // Performing in-order traversal
    printf("In-order traversal before deletion: ");
    inorderTraversal(root);
    printf("\n");

    // Deleting a node
    root = deleteNode(root, 70);

    // Performing in-order traversal after deletion
    printf("In-order traversal after deletion of 70: ");
    inorderTraversal(root);
    printf("\n");

    // Note: You will need to manually free the tree memory or use a different approach 
    // to handle memory management without the `freeTree` function.

    return 0;
}


```







### performing in-order, pre-order, and post-order traversals using bst
```c
#include <stdio.h>
#include <stdlib.h>

// Define the structure of a tree node
typedef struct TreeNode {
    int value;
    struct TreeNode* left;
    struct TreeNode* right;
} TreeNode;

// Function to create a new tree node
TreeNode* createNode(int value) {
    TreeNode* newNode = (TreeNode*)malloc(sizeof(TreeNode));
    newNode->value = value;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

// In-order Traversal
void inorderTraversal(TreeNode* root) {
    if (root != NULL) {
        inorderTraversal(root->left);
        printf("%d ", root->value);
        inorderTraversal(root->right);
    }
}

// Pre-order Traversal
void preorderTraversal(TreeNode* root) {
    if (root != NULL) {
        printf("%d ", root->value);
        preorderTraversal(root->left);
        preorderTraversal(root->right);
    }
}

// Post-order Traversal
void postorderTraversal(TreeNode* root) {
    if (root != NULL) {
        postorderTraversal(root->left);
        postorderTraversal(root->right);
        printf("%d ", root->value);
    }
}

int main() {
    // Example usage
    TreeNode* root = createNode(50);
    root->left = createNode(30);
    root->right = createNode(70);
    root->left->left = createNode(20);
    root->left->right = createNode(40);
    root->right->left = createNode(60);
    root->right->right = createNode(80);

    printf("In-order Traversal: ");
    inorderTraversal(root);
    printf("\n");

    printf("Pre-order Traversal: ");
    preorderTraversal(root);
    printf("\n");

    printf("Post-order Traversal: ");
    postorderTraversal(root);
    printf("\n");

    return 0;
}
```

#Binary Search
```c

// C program to implement iterative Binary Search
#include <stdio.h>

// An iterative binary search function.
int binarySearch(int arr[], int low, int high, int x)
{
    while (low <= high) {
        int mid = low + (high - low) / 2;

        // Check if x is present at mid
        if (arr[mid] == x)
            return mid;

        // If x greater, ignore left half
        if (arr[mid] < x)
            low = mid + 1;

        // If x is smaller, ignore right half
        else
            high = mid - 1;
    }

    // If we reach here, then element was not present
    return -1;
}

// Driver code
int main(void)
{
    int arr[] = { 2, 3, 4, 10, 40 };
    int n = sizeof(arr) / sizeof(arr[0]);
    int x = 10;
    int result = binarySearch(arr, 0, n - 1, x);
   if(result == -1) 
   printf("Element is not present in array");
   else
   printf("Element is present at index %d",result);

}
```
# Interpolation Search
```c

#include <stdio.h>

// Recursive function to perform interpolation search
int interpolationSearch(int arr[], int lo, int hi, int x) {
    int pos;

    // Check if the element is within the bounds of the array
    if (lo <= hi && x >= arr[lo] && x <= arr[hi]) {
        // Compute the position using interpolation formula
        pos = lo + (((double)(hi - lo) / (arr[hi] - arr[lo])) * (x - arr[lo]));

        // Check if the element at position pos is the target
        if (arr[pos] == x)
            return pos;

        // If x is larger, search in the right subarray
        if (arr[pos] < x)
            return interpolationSearch(arr, pos + 1, hi, x);

        // If x is smaller, search in the left subarray
        if (arr[pos] > x)
            return interpolationSearch(arr, lo, pos - 1, x);
    }
    // Element not found
    return -1;
}

// Driver code
int main() {
    // Array of items on which search will be conducted
    int arr[] = {10, 12, 13, 16, 18, 19, 20, 21,
                 22, 23, 24, 33, 35, 42, 47};
    int n = sizeof(arr) / sizeof(arr[0]);

    int x = 18; // Element to be searched
    int index = interpolationSearch(arr, 0, n - 1, x);

    // If element was found
    if (index != -1)
        printf("Element found at index %d\n", index);
    else
        printf("Element not found.\n");

    return 0;
}
```
