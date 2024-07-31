# Tower of Hanoi

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/ed72cec0-e9e4-4c8d-94db-549a1b413128)

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/2e161bef-777e-4f86-a565-14fe684bea77)

### What is the game of Tower of Hanoi?
- Tower of Hanoi consists of three pegs or towers with n disks placed one over the other.

- The objective of the puzzle is to move the stack to another peg following these simple rules.

- 1.Only one disk can be moved at a time.
- 2.No disk can be placed on top of the smaller disk.

### Tower of Hanoi algorithm explained
- Let’s try to solve a puzzle – Tower of Hanoi using recursion.

- Take an example with 2 disks: Disk 1 on top of Disk 2 at peg A. The target is to move both these disks to peg B.

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/0c397f07-3107-44bd-b629-3c136998be39)


#### Looks simple, Right!

- Move Disk 1 from peg A to peg C. Then move disk 2 from peg A to peg B and, finally, move disk 1 from peg C to peg B.

- This solution takes 3 steps.

- You can easily move this stack from peg B to any other peg using these 3 steps.

- But what if we have 3 disks – 1,2, and 3 stacked in peg A.

- To move the stack to peg B you would have to expose disk 3 and to do that disk 1 and 2 have to be moved to peg C.

- So by ensuring that you do not break the rules, using the above subsets of 3 steps in the previous case, you would move disk 1 and 2 to peg C, leaving disk 3 
 exposed with no disk above it.

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/5b08adc9-f35e-485f-b00f-9803627d0513)

- How to solve the problem, recursively move disk 3 from peg A to peg B.

- Then disk 1 from peg C to peg A. After which disk 2 can be moved above disk 3 at peg B.

- The puzzle is finally completed by moving disk 1 from peg A over disk 2 and 3 at peg B.

### What if you have 4 disks?

- Recursively solve the problem of moving disk 1,2, and 3 from peg A to peg C
- Move disk 4 from A to C
- Recursively solve the problem of moving disk 1,2 and 3 from peg C to peg B
- Eventually, you figure out that there is some pattern to the puzzle and with each increment in disks, the pattern could be followed recursively.

- While the 3-disk puzzle required 7 steps. 4-disk requires 7+1+7 = 15 steps to be solved.

  ![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/b6b67761-6343-44d0-8fb5-a80b5a4a629d)


- Create a function Tower with int ‘a’ – for number of disks, char ‘from’ – for from peg, char ‘aux’ – for a secondary peg, char ‘to’ – for destination peg
 Put ‘if’ loop
- If (a=1) i.e. if number of disk = 1, move it from ‘initial peg’ to the ‘destination peg’
- Else, call function tower for ‘a-1’ i.e. the number of disk -1, recall function tower for n-1 disk and move it ‘from’ to ‘to’
- Recall function again using recursion until an or number of the disk is 1.


~~~c
#include <stdio.h>
#include <stdlib.h>

#define MAX 100

typedef struct {
    int items[MAX];
    int top;
} Stack;

void initStack(Stack* s) {
    s->top = -1;
}

int isFull(Stack* s) {
    return s->top == MAX - 1;
}

int isEmpty(Stack* s) {
    return s->top == -1;
}

void push(Stack* s, int value) {
    if (isFull(s)) {
        printf("Stack is full!\n");
    } else {
        s->items[++(s->top)] = value;
    }
}

int pop(Stack* s) {
    if (isEmpty(s)) {
        printf("Stack is empty!\n");
        return -1;
    } else {
        return s->items[(s->top)--];
    }
}

void moveDisk(Stack* src, Stack* dest, char s, char d) {
    int disk = pop(src);
    push(dest, disk);
    printf("Move disk %d from %c to %c\n", disk, s, d);
}

void towerOfHanoi(int n, Stack* src, Stack* dest, Stack* aux, char s, char d, char a) {
    if (n == 1) {
        moveDisk(src, dest, s, d);
        return;
    }
    towerOfHanoi(n - 1, src, aux, dest, s, a, d);
    moveDisk(src, dest, s, d);
    towerOfHanoi(n - 1, aux, dest, src, a, d, s);
}

int main() {
    int n = 3; // Number of disks
    Stack src, dest, aux;

    initStack(&src);
    initStack(&dest);
    initStack(&aux);

    // Push disks to source stack in descending order
    for (int i = n; i >= 1; i--) {
        push(&src, i);
    }

    // Perform the Tower of Hanoi operation
    towerOfHanoi(n, &src, &dest, &aux, 'A', 'C', 'B');

    return 0;
}


~~~

