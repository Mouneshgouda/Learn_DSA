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
