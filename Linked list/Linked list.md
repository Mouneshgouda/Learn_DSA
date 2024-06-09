# Linked List
- A Linked List is a linear data structure consisting of connected nodes where each node has corresponding data and a pointer to the address of the next node. The first node of a linked list is called the Head, and it acts as an access point. On the other hand, the last node is called the Tail, and it marks the end of a linked list by pointing to a NULL value!

## Why Do We Need a Linked List?
```c
Imagine going to a movie theater along with a large group of friends, only to find out there's no way to book consecutive seats to accommodate all. However, there are plenty of disjoint empty seats for that particular screen. So, you all buy tickets and sit accordingly.

But there's a catch!

Since only you were buying popcorn for all, how would you distribute that to your friends? You can't remember where everyone sat, and it's dark inside the hall.

So, instead of you remembering where everyone sat, if everyone kept track of the next friend's seat, then such reference would help popcorn tubs to traverse up to a friend who's yet to get popcorn. This could be achieved by passing popcorn to the next friend starting from you!
```
![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/a1bfd12a-d4f9-4a7d-bf21-c251a22ed543)

- See how the linked list came in handy while keeping track of all these randomly distributed disjoint seats?

- In a computer, you can think of memory as a movie theatre, the virtual address space as the seats, and any particular memory address as a seat number.

- Note: The virtual address space refers to the address range on which a process relies in order to carry out its execution. Unlike seats, this address space is virtual and not real. It's a logical and abstracted mapping to a rather intricate physical memory.

- Now, if we had initiated booking in advance, we could have booked an entire row of consecutive seats much like an array does when we declare it with a fixed size in advance, like so:

- int seats[24];

- In our context of a movie theater, if more friends later decide to join the group to catch the movie. We cannot simply append them to the array of seats since there might be other audiences seating just after the last allocated seat.

- So either we find another larger empty row of consecutive seats so that all friends can sit together (much like dynamic array), or we rely on an approach similar to the linked list, in that we simply insert new friends in vacant spots but still have references to them should we require to pass popcorn and drinks.

- You see, arrays are suitable when we need fast access. Like who's seating at seat no. 13 can be answered in constant time! But arrays require you to declare a fixed size at the compile-time, due to which memory can be either wasted or fell short.

# linked list
- A linked list is a linear data structure that includes a series of connected nodes. Here, each node stores the data and the address of the next node. For example,

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/b59452f5-41d1-4e90-8c27-722d090c329a)

- You have to start somewhere, so we give the address of the first node a special name called HEAD. Also, the last node in the linked list can be identified 
 because its next portion points to NULL.

- Linked lists can be of multiple types: singly, doubly, and circular linked list. In this article, we will focus on the singly linked list. To learn about other - - types, visit Types of Linked List.
```c
Note: You might have played the game Treasure Hunt, where each clue includes the information about the next clue. That is how the linked list operates.
```

## Representation of Linked List
- Let's see how each node of the linked list is represented. Each node consists:

- 1.A data item
- 2.An address of another node
- We wrap both the data item and the next node reference in a struct as:
```c
struct node
{
int data;
struct node *next;
};
```
- Understanding the structure of a linked list node is the key to having a grasp on it.

- Each struct node has a data item and a pointer to another struct node. Let us create a simple Linked List with three items to understand how this works.
```c
/* Initialize nodes */
struct node *head;
struct node *one = NULL;
struct node *two = NULL;
struct node *three = NULL;

/* Allocate memory */
one = malloc(sizeof(struct node));
two = malloc(sizeof(struct node));
three = malloc(sizeof(struct node));

/* Assign data values */
one->data = 1;
two->data = 2;
three->data=3;

/* Connect nodes */
one->next = two;
two->next = three;
three->next = NULL;

/* Save address of first node in head */
head = one;
```

- If you didn't understand any of the lines above, all you need is a refresher on pointers and structs.

- In just a few steps, we have created a simple linked list with three nodes

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/52e897ef-d251-4486-bf2e-0c7c246b4cf4)

- The power of a linked list comes from the ability to break the chain and rejoin it. E.g. if you wanted to put an element 4 between 1 and 2, the steps would be:

- 1.Create a new struct node and allocate memory to it.
- 2.Add its data value as 4
- 3.Point its next pointer to the struct node containing 2 as the data value
- 4.Change the next pointer of "1" to the node we just created.
- 5.Doing something similar in an array would have required shifting the positions of all the subsequent elements.

- In python and Java, the linked list can be implemented using classes as shown in the codes below.

## Linked list implementation in C
```c
// Linked list implementation in C

#include <stdio.h>
#include <stdlib.h>

// Creating a node
struct node {
int value;
struct node *next;
};

// print the linked list value
void printLinkedlist(struct node *p) {
while (p != NULL) {
printf("%d ", p->value);
p = p->next;
}
}

int main() {
// Initialize nodes
struct node *head;
struct node *one = NULL;
struct node *two = NULL;
struct node *three = NULL;

// Allocate memory
one = malloc(sizeof(struct node));
two = malloc(sizeof(struct node));
three = malloc(sizeof(struct node));

// Assign value values
one->value = 1;
two->value = 2;
three->value = 3;

// Connect nodes
one->next = two;
two->next = three;
three->next = NULL;

// printing node-value
head = one;
printLinkedlist(head);
}
```
# Example 2
```c
// Linked list implementation in C

#include <stdio.h>
#include <stdlib.h>

// Creating a node
struct node {
    int value;
    struct node *next;
};

// Print the linked list values
void printLinkedlist(struct node *p) {
    while (p != NULL) {
        printf("%d ", p->value);
        p = p->next;
    }
}

int main() {
    // Initialize nodes
    struct node *head;
    struct node *one = NULL;
    struct node *two = NULL;
    struct node *three = NULL;
    struct node *newNode = NULL;

    // Allocate memory
    one = malloc(sizeof(struct node));
    two = malloc(sizeof(struct node));
    three = malloc(sizeof(struct node));
    newNode = malloc(sizeof(struct node));

    // Assign values
    one->value = 7;
    two->value = 4;
    three->value = 3;
    newNode->value = 4;

    // Connect nodes
    one->next = newNode;  // Connect one to newNode
    newNode->next = two;  // Connect newNode to two
    two->next = three;    // Connect two to three
    three->next = NULL;   // Last node points to NULL

    // Printing node values
    head = one;
    printLinkedlist(head);

    // Free allocated memory
    free(one);
    free(newNode);
    free(two);
    free(three);

    return 0;
}

```

## Linked List Operations: Traverse, Insert and Delete
- There are various linked list operations that allow us to perform different actions on linked lists. For example, the insertion operation adds a new element to 
 the linked list.

- Here's a list of basic linked list operations that we will cover in this article.

- 1.Traversal - access each element of the linked list
- 2.Insertion - adds a new element to the linked list
- 3.Deletion - removes the existing elements
- 4.Search - find a node in the linked list
- 5.Sort - sort the nodes of the linked list

## Things to Remember about Linked List
- head points to the first node of the linked list
- next pointer of the last node is NULL, so if the next current node is NULL, we have reached the end of the linked list.
- In all of the examples, we will assume that the linked list has three nodes 1 --->2 --->3 with node structure as below:
```c
struct node {
int data;
struct node *next;
};
```
