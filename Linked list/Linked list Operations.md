### Linkedlist Creation ,Insertion and Display
```c
#include<stdio.h>
#include<stdlib.h>

struct Node
{
  int data;
  struct Node *next;
};

void insertStart (struct Node **head, int data)
{

  struct Node *newNode = (struct Node *) malloc (sizeof (struct Node));

  newNode->data = data;
  newNode->next = *head;

  //changing the new head to this freshly entered node
  *head = newNode;
}

void display (struct Node *node)
{

  //as linked list will end when Node is Null
  while (node != NULL)
    {
      printf ("%d ", node->data);
      node = node->next;
    }
  printf ("\n");
}

int main ()
{

  //creating 4 pointers of type struct Node
  //So these can point to address of struct type variable
  struct Node *head = NULL;
  struct Node *node2 = NULL;
  struct Node *node3 = NULL;
  struct Node *node4 = NULL;

  // allocate 3 nodes in the heap 
  head = (struct Node *) malloc (sizeof (struct Node));
  node2 = (struct Node *) malloc (sizeof (struct Node));
  node3 = (struct Node *) malloc (sizeof (struct Node));
  node4 = (struct Node *) malloc (sizeof (struct Node));


  head->data = 15;		// data set for head node 
  head->next = node2;		// next pointer assigned to address of node2 

  node2->data = 10;
  node2->next = node3;

  node3->data = 12;
  node3->next = node4;

  node4->data = 3;
  node4->next = NULL;

  printf ("Linklist : ");
  display (head);

  // Need '&' i.e. address as we need to change head
  insertStart (&head, 25);

  printf ("\nAfter Inserting Element\n");
  printf ("\nLinklist : ");
  // no need for '&' as head need not be changed
  // only doing traversal
  display (head);
  return 0;
}
```

### LastInsertion
```c
#include<stdio.h>
#include<stdlib.h>

struct Node
{
  int data;
  struct Node *next;
};

void insertStart (struct Node **head, int data)
{

  struct Node *newNode = (struct Node *) malloc (sizeof (struct Node));

  newNode->data = data;
  newNode->next = *head;

  //changing the new head to this freshly entered node
  *head = newNode;
}

void insertLast (struct Node **head, int data)
{

  struct Node *newNode = (struct Node *) malloc (sizeof (struct Node));

  newNode->data = data;
  newNode->next = NULL;

  //need this if there is no node present in linked list at all
  if (*head == NULL)
    {
      *head = newNode;
      return;
    }

  struct Node *temp = *head;

  while (temp->next != NULL)
    temp = temp->next;

  temp->next = newNode;
}

void display (struct Node *node)
{

  //as linked list will end when Node is Null
  while (node != NULL)
    {
      printf ("%d ", node->data);
      node = node->next;
    }
  printf ("\n");
}

int main ()
{
  struct Node *head = NULL;

  // Need '&' i.e. address as we need to change head
  insertStart (&head, 12);
  insertStart (&head, 16);
  insertStart (&head, 20);

  insertLast (&head, 10);
  insertLast (&head, 14);
  insertLast (&head, 18);
  insertLast (&head, 11);

  // no need for '&' as head need not be changed
  // only doing traversal
  display (head);
  return 0;
}
```
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

