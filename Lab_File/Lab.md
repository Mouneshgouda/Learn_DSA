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
