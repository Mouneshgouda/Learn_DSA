### LinkedList

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/cdea48f5-71e4-4e14-93a3-c5324a91ac8f)

- A Singly Linked List is a specialized case of a generic linked list. In a singly linked list, each node links to only the next node in the sequence, i.e. if we start traversing from the first node of the list, we can only move in one direction(pun intended).

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/d57a5354-8856-41f1-8607-f98e638774a7)


- The Node of the singly linked list, apart from the data, stores the address of only the next element, as shown below. The following is the JAVA representation of a node.

```c
struct Node {
    int data;
    struct Node *next;
};

```
- For a linked list we maintain a special pointer known s HEAD. This pointer stores the address of the first node of the list. Also, the last node can no longer have the next element. Hence we indicate the end of the linked list by assigning NULL to its next.

- ![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/782bda42-0b3e-4853-9f02-79ae748e37ca)

- Whereas linked list shines when we need to modify existing data by insertion and deletion because it doesn't have a fixed size. So, our memory consumption is determined at run time as the linked list shrinks and grows dynamically in constant time.

- Later on, we will explore these linked list operations in-depth but first, let's discuss the types of linked lists.

### Types of Linked List
- There are mainly three types of linked lists:

- Singly Linked List
  Here, we can only traverse in one direction (not the band ) due to the linking of every node to its next nod

  ![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/49421b17-6aca-4789-9d04-d64a34090d07)

 ### Doubly Linked List
 - Here, we can traverse in both directions as every node contains an additional prev pointer that points to the previous node. 
![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/742bc0d4-2c90-42de-a8be-79d5d3960d21)

### Circular Linked List
- Here, we can keep traversing forever and ever until the program crashes as the tail node's next pointer points to the head node instead of a NULL.
![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/6cff17f9-0987-4d56-94c8-5d1eb21221ec)

### Operations of Linked List
- Keeping the above Node's blueprint in mind, let's now discuss some trivial operations on a linked list of size 'k':

### Traversal
- We can traverse the entire linked list starting from the head node. If there are n nodes then the time complexity for traversal becomes O(n) as we hop through 
  each and every node.
 ![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/7bc55947-3172-4c71-b0d8-51ab54277d84)

### Insertion
- Inserting a new node at a given position is achieved by manipulating at most 2 next pointers like so; consider two pointers, prevNode, and newNode set newNode's 
 next pointer to the prevNode's next pointer and set prevNode's next pointer to the newNode where prevNode denotes a pointer to the node after which newNode is to 
 be inserted.
- And since only a constant number of pointers gets changed irrespective of the size of the linked list, the complexity should have been O(1).

- However, to get access at any given position, we have to traverse starting from the head till prevNode. Thus, the worst case for insertion could be expressed as; 
 Traversal O(n) + Just the insertion O(1) = Insertion O(n). However, the best case would be to insert in the beginning and hence the time complexity becomes Ω(1).
 Notice that the order of execution does matter in case of insertion. If we interchange the steps i.e. first set prevNode's next pointer to the newNode then we 
 lose the reference to the remaining of the linked list previously occurring after the prevNode. Something to keep in mind!
 ![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/764c244d-ac92-40ee-a6c9-19c79b2e7957)

### Deletion
- We can delete a node located at a specified index by manipulating at most 2 next pointers like so; consider two pointers, prevNode, and targetNode set prevNode's 
 next pointer to the targetNode's next pointer and set targetNode's next pointer to NULL
 where prevNode denotes a pointer to the node after which targetNode is to be deleted. Following the same reasoning as insertion, the best case and the worst case 
 time complexity stands at Ω(1) and O(n) respectively.

- Again just like insertion, the order is important. It's important to realize that setting targetNode's next pointer to NULL as the first step would cost us the 
 reference to the remaining of the linked list (if the targetNode wasn't the Tail).
![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/bf233428-2ed3-4673-b2ed-c78e374ae70f)

### Search
- Given a particular key (data), we need to search for a node whose data matches the key. In the best-case scenario, the head would be the node we are looking for, 
 whereas in the worst-case the required node would be the tail. In terms of time complexity the best case, the average case, and the worst case of searching are 
 denoted as Ω(1), Θ(n), and O(n) respectively.
### Implementation of LinkedList Operation
```c
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>  // For boolean type

// Define the structure of a node in the linked list
struct Node {
    int data;
    struct Node* next;
};

// Function to create a new node
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    if (newNode == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Function to traverse and print the linked list
void traversal(struct Node* head) {
    struct Node* itr = head;
    while (itr != NULL) {
        printf("%d\n", itr->data);
        itr = itr->next;
    }
}

// Function to insert a new node after a given previous node
void insertion(struct Node* prevNode, struct Node* newNode) {
    if (prevNode == NULL) {
        fprintf(stderr, "Previous node cannot be NULL\n");
        return;
    }
    newNode->next = prevNode->next;
    prevNode->next = newNode;
}

// Function to delete a node after a given previous node
void deletion(struct Node* prevNode, struct Node* targetNode) {
    if (prevNode == NULL || targetNode == NULL) {
        fprintf(stderr, "Invalid deletion operation\n");
        return;
    }
    prevNode->next = targetNode->next;
    free(targetNode);
}

// Function to search for a node with a given key
bool search(struct Node* head, int key) {
    struct Node* itr = head;
    while (itr != NULL) {
        if (itr->data == key) {
            return true;
        }
        itr = itr->next;
    }
    return false;  // Key not found
}

// Function to free memory allocated for the linked list nodes
void freeLinkedList(struct Node* head) {
    struct Node* current = head;
    struct Node* next;

    while (current != NULL) {
        next = current->next;
        free(current);
        current = next;
    }
}

int main() {
    struct Node* head = NULL;
    struct Node* node1 = createNode(1);
    struct Node* node2 = createNode(2);
    struct Node* node3 = createNode(3);

    head = node1;
    node1->next = node2;
    node2->next = node3;

    // Print the linked list
    printf("Linked List:\n");
    traversal(head);

    // Insert a new node (4) after node2
    struct Node* node4 = createNode(4);
    insertion(node2, node4);

    // Print the modified linked list
    printf("\nLinked List after insertion:\n");
    traversal(head);

    // Delete node3 from the list
    deletion(node2, node3);

    // Print the modified linked list
    printf("\nLinked List after deletion:\n");
    traversal(head);

    // Search for a node with data 2
    int key = 2;
    if (search(head, key)) {
        printf("\nNode with data %d found\n", key);
    } else {
        printf("\nNode with data %d not found\n", key);
    }

    // Free memory allocated for the linked list
    freeLinkedList(head);

    return 0;
}
```

```c
cd "c:\Users\LENOVO\Downloads\Music-Player-Using-LinkedList-in-C-main\Music-Player-Using-LinkedList-in-C-main\"

```
```c
gcc music_player.c -o music_player.exe
```
```c
music_player.exe
```
