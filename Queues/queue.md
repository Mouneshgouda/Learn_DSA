# Queue
- A queue is a useful data structure in programming. It is similar to the ticket queue outside a cinema hall, where the first person entering the queue is the 
 first person who gets the ticket.

- Queue follows the First In First Out (FIFO) rule - the item that goes in first is the item that comes out first.

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/f2877ada-21e4-4634-9071-9135e932432e)

- In the above image, since 1 was kept in the queue before 2, it is the first to be removed from the queue as well. It follows the FIFO rule.

- In programming terms, putting items in the queue is called enqueue, and removing items from the queue is called dequeue.

- We can implement the queue in any programming language like C, C++, Java, Python or C#, but the specification is pretty much the same.

### Queue Operations

| Operation | Description                                                                                      |
|-----------|--------------------------------------------------------------------------------------------------|
| Enqueue   | Adds an element to the rear or end of the queue.                                                  |
| Dequeue   | Removes and returns the element from the front of the queue, maintaining FIFO order.              |
| Peek      | Allows viewing the element at the front of the queue without removing it.                         |
| isEmpty   | Checks if the queue is empty. Returns true if the queue contains no elements, false otherwise.    |
| isFull    | Checks if the queue is full. Returns true if the queue is at maximum capacity, false otherwise.  |


## Working of Queue
### Queue operations work as follows:

- 1.two pointers FRONT and REAR
- 2.FRONT track the first element of the queue
- 3.REAR track the last element of the queue
- 4.initially, set value of FRONT and REAR to -1

## Enqueue Operation
- 1.check if the queue is full
- 2.for the first element, set the value of FRONT to 0
- 3.increase the REAR index by 1
- 4.add the new element in the position pointed to by REAR
## Dequeue Operation
- 1.check if the queue is empty
- 2.return the value pointed by FRONT
- 3.increase the FRONT index by 1
- 4.for the last element, reset the values of FRONT and REAR to -1

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/35e1637d-0dcf-440c-953a-be572fdbcd32)

## Example
```c
// Queue implementation in C

#include <stdio.h>
#define SIZE 5

void enQueue(int);
void deQueue();
void display();

int items[SIZE], front = -1, rear = -1;

int main() {
//deQueue is not possible on empty queue
deQueue();

//enQueue 5 elements
enQueue(1);
enQueue(2);
enQueue(3);
enQueue(4);
enQueue(5);

// 6th element can't be added to because the queue is full
enQueue(6);

display();

//deQueue removes element entered first i.e. 1
deQueue();

//Now we have just 4 elements
display();

return 0;
}

void enQueue(int value) {
if (rear == SIZE - 1)
printf("\nQueue is Full!!");
else {
if (front == -1)
front = 0;
rear++;
items[rear] = value;
printf("\nInserted -> %d", value);
}
}

void deQueue() {
if (front == -1)
printf("\nQueue is Empty!!");
else {
printf("\nDeleted : %d", items[front]);
front++;
if (front > rear)
front = rear = -1;
}
}

// Function to print the queue
void display() {
if (rear == -1)
printf("\nQueue is Empty!!!");
else {
int i;
printf("\nQueue elements are:\n");
for (i = front; i <= rear; i++)
printf("%d  ", items[i]);
}
printf("\n");
}
```
## Limitations of Queue
- As you can see in the image below, after a bit of enqueuing and dequeuing, the size of the queue has been reduced.
![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/c7f8e7c9-5511-429b-9ed4-9a22a8134a24)
- And we can only add indexes 0 and 1 only when the queue is reset (when all the elements have been dequeued).
- After REAR reaches the last index, if we can store extra elements in the empty spaces (0 and 1), we can make use of the empty spaces. This is implemented by a 
 modified queue called the circular queue.

## Complexity Analysis
- The complexity of enqueue and dequeue operations in a queue using an array is O(1). If you use pop(N) in python code, then the complexity might be O(n) 
 depending on the position of the item to be popped.

## Applications of Queue
- CPU scheduling, Disk Scheduling
- When data is transferred asynchronously between two processes.The queue is used for synchronization. For example: IO Buffers, pipes, file IO, etc
  Handling of interrupts in real-time systems.
- Call Center phone systems use Queues to hold people calling them in order.

```c
#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 5

typedef struct {
    int items[MAX_SIZE];
    int front;
    int rear;
} Queue;

void initializeQueue(Queue *queue) {
    queue->front = -1;
    queue->rear = -1;
}

int isEmpty(Queue *queue) {
    return (queue->front == -1 && queue->rear == -1);
}

int isFull(Queue *queue) {
    return (queue->rear + 1) % MAX_SIZE == queue->front ? 1 : 0;
}

void enqueue(Queue *queue, int value) {
    if (isFull(queue)) {
        printf("Queue is full. Cannot enqueue.\n");
        return;
    } else if (isEmpty(queue)) {
        queue->front = 0;
    }
    queue->rear = (queue->rear + 1) % MAX_SIZE;
    queue->items[queue->rear] = value;
    printf("Enqueued: %d\n", value);
}

int dequeue(Queue *queue) {
    if (isEmpty(queue)) {
        printf("Queue is empty. Cannot dequeue.\n");
        return -1;
    } else if (queue->front == queue->rear) {
        int value = queue->items[queue->front];
        queue->front = -1;
        queue->rear = -1;
        printf("Dequeued: %d\n", value);
        return value;
    } else {
        int value = queue->items[queue->front];
        queue->front = (queue->front + 1) % MAX_SIZE;
        printf("Dequeued: %d\n", value);
        return value;
    }
}

int peek(Queue *queue) {
    if (isEmpty(queue)) {
        printf("Queue is empty. Cannot peek.\n");
        return -1;
    } else {
        printf("Front element: %d\n", queue->items[queue->front]);
        return queue->items[queue->front];
    }
}

int main() {
    Queue myQueue;
    initializeQueue(&myQueue);

    enqueue(&myQueue, 10);
    enqueue(&myQueue, 20);
    enqueue(&myQueue, 30);

    peek(&myQueue);

    dequeue(&myQueue);
    peek(&myQueue);

    enqueue(&myQueue, 40);

    return 0;
}
```

### Array Representation:
- Using an array to represent a queue is one of the simplest ways to implement it. In this approach, we use a fixed-size array to store the elements of the queue. 
 Two pointers, front and rear, are used to keep 
 track of the front and rear of the queue, respectively.

##Operations:
### Enqueue Operation (enqueue):
```c
- When an element is inserted into the queue, it is added to the rear end.
 We increment the rear pointer to the next available position in the array and place the new element there.
 If the queue is empty initially, both front and rear are set to 0.
```


### Dequeue Operation (dequeue):
```c

When an element is removed from the queue, it is always removed from the front end.
We increment the front pointer to point to the next element to be dequeued.
If the queue becomes empty after dequeuing, both front and rear are reset to -1 to indicate an empty queue.
```

### Empty and Full Checks (isEmpty and isFull):
```c
isEmpty checks if the queue is empty by inspecting the value of front.
isFull checks if the queue is full by inspecting the value of rear in relation to the maximum capacity of the array.
```
### Implementation:
- We use a fixed-size array to hold the elements of the queue.
- Two pointers, front and rear, are used to maintain the position of the front and rear elements.
- enqueue adds elements to the rear and updates rear.
- dequeue removes elements from the front and updates front.
- isEmpty and isFull check if the queue is empty or full, respectively.
- If the rear pointer reaches the end of the array, it can either wrap around (circular queue) or resize the array.

### Implementation
```c
#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100

// Structure to represent a queue
struct Queue {
    int items[MAX_SIZE];
    int front;
    int rear;
};

// Function to create a new queue
struct Queue* createQueue() {
    struct Queue* queue = (struct Queue*)malloc(sizeof(struct Queue));
    queue->front = -1;
    queue->rear = -1;
    return queue;
}

// Function to check if the queue is full
int isFull(struct Queue* queue) {
    return queue->rear == MAX_SIZE - 1;
}

// Function to check if the queue is empty
int isEmpty(struct Queue* queue) {
    return queue->front == -1;
}

// Function to add an element to the queue
void enqueue(struct Queue* queue, int value) {
    if (isFull(queue)) {
        printf("Queue is full\n");
        return;
    }
    if (isEmpty(queue)) {
        queue->front = 0;
    }
    queue->rear++;
    queue->items[queue->rear] = value;
}

// Function to remove an element from the queue
int dequeue(struct Queue* queue) {
    int item;
    if (isEmpty(queue)) {
        printf("Queue is empty\n");
        return -1;
    }
    item = queue->items[queue->front];
    if (queue->front >= queue->rear) {
        queue->front = -1;
        queue->rear = -1;
    } else {
        queue->front++;
    }
    return item;
}

// Function to display the elements of the queue
void display(struct Queue* queue) {
    int i;
    if (isEmpty(queue)) {
        printf("Queue is empty\n");
        return;
    }
    printf("Queue elements are:\n");
    for (i = queue->front; i <= queue->rear; i++) {
        printf("%d ", queue->items[i]);
    }
    printf("\n");
}

int main() {
    struct Queue* queue = createQueue();

    enqueue(queue, 1);
    enqueue(queue, 2);
    enqueue(queue, 3);
    enqueue(queue, 4);

    display(queue);

    printf("Dequeuing element: %d\n", dequeue(queue));
    printf("Dequeuing element: %d\n", dequeue(queue));

    display(queue);

    enqueue(queue, 5);
    enqueue(queue, 6);

    display(queue);

    return 0;
}
```
- A queue is a useful data structure in programming. It is similar to the ticket queue outside a cinema hall, where the first person entering the queue is the 
 first person who gets the ticket.

### There are four different types of queues:

- 1.Simple Queue
- 2.Circular Queue
- 3.Priority Queue
- 4.Double Ended Queue

## Simple Queue
- In a simple queue, insertion takes place at the rear and removal occurs at the front. It strictly follows the FIFO (First in First out) rule.

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/a1f6e08f-12e6-49bc-9bee-46504eb34939)

## Circular Queue
- In a circular queue, the last element points to the first element making a circular link.
![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/93b6c4ea-25ec-4212-970e-502b7fcbb9d3)

- The main advantage of a circular queue over a simple queue is better memory utilization. If the last position is full and the first position is empty, we can 
 insert an element in the first position. This action is not possible in a simple queue.

## Priority Queue
- A priority queue is a special type of queue in which each element is associated with a priority and is served according to its priority. If elements with the 
 same priority occur, they are served according to their order in the queue.

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/dfda1f41-4028-4426-ae68-bc131fa4b4c7)
- Insertion occurs based on the arrival of the values and removal occurs based on priority.
 
## Deque (Double Ended Queue)
- In a double ended queue, insertion and removal of elements can be performed from either from the front or rear. Thus, it does not follow the FIFO (First In 
 First Out) rule.
![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/f35689ed-44ed-4550-8e2b-f9f5c2a6a967)


![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/1d0eed57-169f-40eb-84f6-79c877c53def)

# circular queue
- A circular queue is the extended version of a regular queue where the last element is connected to the first element. Thus forming a circle-like structure.
![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/eba731f6-bd0b-4ab3-8759-8529dbadf2cd)

- The circular queue solves the major limitation of the normal queue. In a normal queue, after a bit of insertion and deletion, there will be non-usable empty 
 space.

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/b718bb30-d724-4443-bdad-c6b196d481bc)
- Here, indexes 0 and 1 can only be used after resetting the queue (deletion of all elements). This reduces the actual size of the queue.

### How Circular Queue Works
- Circular Queue works by the process of circular increment i.e. when we try to increment the pointer and we reach the end of the queue, we start from the 
 beginning of the queue.

- Here, the circular increment is performed by modulo division with the queue size. That is,

```c
if REAR + 1 == 5 (overflow!), REAR = (REAR + 1)%5 = 0 (start of queue)
```

## Circular Queue Operations
- The circular queue work as follows:

- 1.two pointers FRONT and REAR
- 2.FRONT track the first element of the queue
- 3.REAR track the last elements of the queue
- 4.initially, set value of FRONT and REAR to -1

## 1. Enqueue Operation
- 1.check if the queue is full
- 2.for the first element, set value of FRONT to 0
- 3.circularly increase the REAR index by 1 (i.e. if the rear reaches the end, next it would be at the start of the queue)
- 4.add the new element in the position pointed to by REAR

## 2. Dequeue Operation
- 1.check if the queue is empty
- 2.return the value pointed by FRONT
- 3.circularly increase the FRONT index by 1
- 4.for the last element, reset the values of FRONT and REAR to -1

- However, the check for full queue has a new additional case:

- 1. Case 1: FRONT = 0 && REAR == SIZE - 1
- 2.Case 2: FRONT = REAR + 1
- The second case happens when REAR starts from 0 due to circular increment and when its value is just 1 less than FRONT, the queue is full.

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/41e1f663-d225-4262-9676-cb6e18cab136)

```c
// Circular Queue implementation in C

#include <stdio.h>

#define SIZE 5

int items[SIZE];
int front = -1, rear = -1;

// Check if the queue is full
int isFull() {
if ((front == rear + 1) || (front == 0 && rear == SIZE - 1)) return 1;
return 0;
}

// Check if the queue is empty
int isEmpty() {
if (front == -1) return 1;
return 0;
}

// Adding an element
void enQueue(int element) {
if (isFull())
printf("\n Queue is full!! \n");
else {
if (front == -1) front = 0;
rear = (rear + 1) % SIZE;
items[rear] = element;
printf("\n Inserted -> %d", element);
}
}

// Removing an element
int deQueue() {
int element;
if (isEmpty()) {
printf("\n Queue is empty !! \n");
return (-1);
} else {
element = items[front];
if (front == rear) {
front = -1;
rear = -1;
} 
// Q has only one element, so we reset the 
// queue after dequeing it. ?
else {
front = (front + 1) % SIZE;
}
printf("\n Deleted element -> %d \n", element);
return (element);
}
}

// Display the queue
void display() {
int i;
if (isEmpty())
printf(" \n Empty Queue\n");
else {
printf("\n Front -> %d ", front);
printf("\n Items -> ");
for (i = front; i != rear; i = (i + 1) % SIZE) {
printf("%d ", items[i]);
}
printf("%d ", items[i]);
printf("\n Rear -> %d \n", rear);
}
}

int main() {
// Fails because front = -1
deQueue();

enQueue(1);
enQueue(2);
enQueue(3);
enQueue(4);
enQueue(5);

// Fails to enqueue because front == 0 && rear == SIZE - 1
enQueue(6);

display();
deQueue();

display();

enQueue(7);
display();

// Fails to enqueue because front == rear + 1
enQueue(8);

return 0;
}

```

output:-
```c
Queue is empty !! 

 Inserted -> 1
 Inserted -> 2
 Inserted -> 3
 Inserted -> 4
 Inserted -> 5
 Queue is full!! 

 Front -> 0 
 Items -> 1 2 3 4 5 
 Rear -> 4 

 Deleted element -> 1 

 Front -> 1 
 Items -> 2 3 4 5 
 Rear -> 4 

 Inserted -> 7
 Front -> 1 
 Items -> 2 3 4 5 7 
 Rear -> 0 

 Queue is full!! 

```
### Circular Queue Complexity Analysis
- The complexity of the enqueue and dequeue operations of a circular queue is O(1) for (array implementations).

### Applications of Circular Queue
- 1.CPU scheduling
- 2.Memory management
- 3.Traffic Management

# Priority Queue
- 1.A priority queue is a special type of queue in which each element is associated with a priority value. And, elements are served on the basis of their priority. That is, higher priority elements are served first.

- 2.However, if elements with the same priority occur, they are served according to their order in the queue.

## Assigning Priority Value

- 1.Generally, the value of the element itself is considered for assigning the priority. For example,

- 2.The element with the highest value is considered the highest priority element. However, in other cases, we can assume the element with the lowest value as the 
  highest priority element.

- 3.We can also set priorities according to our needs.

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/9f9e12f9-6c0a-4807-940b-30c6b7bae2c1)

## Difference between Priority Queue and Normal Queue
- In a queue, the first-in-first-out rule is implemented whereas, in a priority queue, the values are removed on the basis of priority. The element with the 
 highest priority is removed first.

## Implementation of Priority Queue
- Priority queue can be implemented using an array, a linked list, a heap data structure, or a binary search tree. Among these data structures, heap data 
 structure provides an efficient implementation of priority queues.

- Hence, we will be using the heap data structure to implement the priority queue in this tutorial. A max-heap is implemented in the following operations. If you 
 want to learn more about it, please visit max-heap and min-heap.

- A comparative analysis of different implementations of priority queue is given below.

| Data Structure      | Peek     | Insert      | Delete      |
|---------------------|----------|-------------|-------------|
| Linked List         | O(1)     | O(n)        | O(1)        |
| Binary Heap         | O(1)     | O(log n)    | O(log n)    |
| Binary Search Tree  | O(1)     | O(log n)    | O(log n)    |

## Priority Queue Operations
- Basic operations of a priority queue are inserting, removing, and peeking elements.
```c
Note:-
Before studying the priority queue, please refer to the heap data structure for a better understanding of binary heap as it is used to implement the priority 
queue in this article.
```
## 1. Inserting an Element into the Priority Queue
- Inserting an element into a priority queue (max-heap) is done by the following steps.

- Insert the new element at the end of the tree

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/eedb392e-3157-4a54-a408-89da05ec94c6)

- heapify the tree

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/46c29357-58b1-4d8b-b834-40272381dca5)

- Algorithm for insertion of an element into priority queue (max-heap)
```c
If there is no node, 
create a newNode.
else (a node is already present)
insert the newNode at the end (last node from left to right.)
```

- heapify the array
- For Min Heap, the above algorithm is modified so that parentNode is always smaller than newNode.

## 2. Deleting an Element from the Priority Queue
- Deleting an element from a priority queue (max-heap) is done as follows:

- Select the element to be deleted.

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/088537d9-3c0f-4419-b9dc-9719a200fb8f)

-  it with the last element.

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/d3518a00-714f-4de5-bb2b-cd5006b05d7d)

- Remove the last element.

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/e8c9bc61-e6f3-4ec2-ae0d-cc3413a16a81)

- Heapify the tree.

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/454acae1-cd4e-4ab8-8866-5cf0ca3afdcb)


- Algorithm for deletion of an element in the priority queue (max-heap)
```c
If nodeToBeDeleted is the leafNode
remove the node
Else swap nodeToBeDeleted with the lastLeafNode
remove noteToBeDeleted

heapify the array
```
- For Min Heap, the above algorithm is modified so that the both childNodes are smaller than currentNode.

## 3. Peeking from the Priority Queue (Find max/min)
- Peek operation returns the maximum element from Max Heap or minimum element from Min Heap without deleting the node.

- For both Max heap and Min Heap
```c
return rootNode
```
## 4. Extract-Max/Min from the Priority Queue
  Extract-Max returns the node with maximum value after removing it from a Max Heap whereas Extract-Min returns the node with minimum value after removing it from 
  Min Heap

## Priority Queue implementation in C
```c
  // Priority Queue implementation in C

#include <stdio.h>
int size = 0;
void swap(int *a, int *b) {
int temp = *b;
*b = *a;
*a = temp;
}

// Function to heapify the tree
void heapify(int array[], int size, int i) {
if (size == 1) {
printf("Single element in the heap");
} else {
// Find the largest among root, left child and right child
int largest = i;
int l = 2 * i + 1;
int r = 2 * i + 2;
if (l < size && array[l] > array[largest])
largest = l;
if (r < size && array[r] > array[largest])
largest = r;

// Swap and continue heapifying if root is not largest
if (largest != i) {
swap(&array[i], &array[largest]);
heapify(array, size, largest);
}
}
}

// Function to insert an element into the tree
void insert(int array[], int newNum) {
if (size == 0) {
array[0] = newNum;
size += 1;
} else {
array[size] = newNum;
size += 1;
for (int i = size / 2 - 1; i >= 0; i--) {
heapify(array, size, i);
}
}
}

// Function to delete an element from the tree
void deleteRoot(int array[], int num) {
int i;
for (i = 0; i < size; i++) {
if (num == array[i])
break;
}

swap(&array[i], &array[size - 1]);
size -= 1;
for (int i = size / 2 - 1; i >= 0; i--) {
heapify(array, size, i);
}
}

// Print the array
void printArray(int array[], int size) {
for (int i = 0; i < size; ++i)
printf("%d ", array[i]);
printf("\n");
}

// Driver code
int main() {
int array[10];

insert(array, 3);
insert(array, 4);
insert(array, 9);
insert(array, 5);
insert(array, 2);

printf("Max-Heap array: ");
printArray(array, size);

deleteRoot(array, 4);

printf("After deleting an element: ");

printArray(array, size);
}
```
# Deque Data Structure

- Deque or Double Ended Queue is a type of queue in which insertion and removal of elements can either be performed from the front or the rear. Thus, it does not 
 follow FIFO rule (First In First Out).

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/2d6f0cee-e303-4f9e-b53f-4e048e6891ad)

## Types of Deque
- 1.Input Restricted Deque
- 2.In this deque, input is restricted at a single end but allows deletion at both the ends.
- 3.Output Restricted Deque
- 4.In this deque, output is restricted at a single end but allows insertion at both the ends.

## Priority Queue Applications
- Some of the applications of a priority queue are:

- 1.Dijkstra's algorithm
- 2.for implementing stack
- 3.for load balancing and interrupt handling in an operating system
- 4.for data compression in Huffman code
## Operations on a Deque
- Below is the circular array implementation of deque. In a circular array, if the array is full, we start from the beginning.

- But in a linear array implementation, if the array is full, no more elements can be inserted. In each of the operations below, if the array is full, "overflow 
 message" is thrown.

- Before performing the following operations, these steps are followed.

- Take an array (deque) of size n.
 Set two pointers at the first position and set front = -1 and rear = 0.

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/b43093c1-a99d-4b13-aebc-aa94bf994ee1)

## 1. Insert at the Front
- This operation adds an element at the front.

- Check the position of front.

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/0194abc9-6062-4c2f-9c03-ec6e7ca6c706)

- 2.If front < 1, reinitialize front = n-1 (last index).
![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/5c0258b1-7872-4130-88b8-a551781d288f)

- 3.Else, decrease front by 1.
- 4.Add the new key 5 into array[front].

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/06a1a446-26d8-4ae5-9655-f5fbd5a26d19)

## 2. Insert at the Rear
- This operation adds an element to the rear.

- Check if the array is full

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/8581a281-5350-4f60-a484-2220e8806d05)

- 2.If the deque is full, reinitialize rear = 0.
- 3.Else, increase rear by 1.
![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/f16d433d-7067-43a4-9b10-90e5082a4b79)

- 4.Add the new key 5 into array[rear]
![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/19704d9c-c874-40ab-870d-3472efe35a02)

## 3. Delete from the Front
- The operation deletes an element from the front.

- 1.Check if the deque is empty.

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/21635786-aaf6-4c17-8983-1969d93d26e5)

- 2.If the deque is empty (i.e. front = -1), deletion cannot be performed (underflow condition).
- 3.If the deque has only one element (i.e. front = rear), set front = -1 and rear = -1.
- 4.Else if front is at the end (i.e. front = n - 1), set go to the front front = 0.
- 5.Else, front = front + 1

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/50baf933-6579-4f16-957a-40ba4aac9aec)

## 4. Delete from the Rear
- This operation deletes an element from the rear.

- 1.Check if the deque is empty.
![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/8392ce7f-f813-43a5-85af-38423b302c7a)

- 2.If the deque is empty (i.e. front = -1), deletion cannot be performed (underflow condition).
- 3.If the deque has only one element (i.e. front = rear), set front = -1 and rear = -1, else follow the steps below.
- 4.If rear is at the front (i.e. rear = 0), set go to the front rear = n - 1.
- 5.Else, rear = rear - 1.

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/c9fb9f28-c0cf-41b2-8d67-f4524dc4513e)

## 5. Check Empty
- This operation checks if the deque is empty. If front = -1, the deque is empty.

## 6. Check Full
- This operation checks if the deque is full. If front = 0 and rear = n - 1 OR front = rear + 1, the deque is full.

##  Deque implementation in c
```c
// Deque implementation in C

#include <stdio.h>

#define MAX 10

void addFront(int *, int, int *, int *);
void addRear(int *, int, int *, int *);
int delFront(int *, int *, int *);
int delRear(int *, int *, int *);
void display(int *);
int count(int *);

int main() {
int arr[MAX];
int front, rear, i, n;

front = rear = -1;
for (i = 0; i < MAX; i++)
arr[i] = 0;

addRear(arr, 5, &front, &rear);
addFront(arr, 12, &front, &rear);
addRear(arr, 11, &front, &rear);
addFront(arr, 5, &front, &rear);
addRear(arr, 6, &front, &rear);
addFront(arr, 8, &front, &rear);

printf("\nElements in a deque: ");
display(arr);

i = delFront(arr, &front, &rear);
printf("\nremoved item: %d", i);

printf("\nElements in a deque after deletion: ");
display(arr);

addRear(arr, 16, &front, &rear);
addRear(arr, 7, &front, &rear);

printf("\nElements in a deque after addition: ");
display(arr);

i = delRear(arr, &front, &rear);
printf("\nremoved item: %d", i);

printf("\nElements in a deque after deletion: ");
display(arr);

n = count(arr);
printf("\nTotal number of elements in deque: %d", n);
}

void addFront(int *arr, int item, int *pfront, int *prear) {
int i, k, c;

if (*pfront == 0 && *prear == MAX - 1) {
printf("\nDeque is full.\n");
return;
}

if (*pfront == -1) {
*pfront = *prear = 0;
arr[*pfront] = item;
return;
}

if (*prear != MAX - 1) {
c = count(arr);
k = *prear + 1;
for (i = 1; i <= c; i++) {
arr[k] = arr[k - 1];
k--;
}
arr[k] = item;
*pfront = k;
(*prear)++;
} else {
(*pfront)--;
arr[*pfront] = item;
}
}

void addRear(int *arr, int item, int *pfront, int *prear) {
int i, k;

if (*pfront == 0 && *prear == MAX - 1) {
printf("\nDeque is full.\n");
return;
}

if (*pfront == -1) {
*prear = *pfront = 0;
arr[*prear] = item;
return;
}

if (*prear == MAX - 1) {
k = *pfront - 1;
for (i = *pfront - 1; i < *prear; i++) {
k = i;
if (k == MAX - 1)
arr[k] = 0;
else
arr[k] = arr[i + 1];
}
(*prear)--;
(*pfront)--;
}
(*prear)++;
arr[*prear] = item;
}

int delFront(int *arr, int *pfront, int *prear) {
int item;

if (*pfront == -1) {
printf("\nDeque is empty.\n");
return 0;
}

item = arr[*pfront];
arr[*pfront] = 0;

if (*pfront == *prear)
*pfront = *prear = -1;
else
(*pfront)++;

return item;
}

int delRear(int *arr, int *pfront, int *prear) {
int item;

if (*pfront == -1) {
printf("\nDeque is empty.\n");
return 0;
}

item = arr[*prear];
arr[*prear] = 0;
(*prear)--;
if (*prear == -1)
*pfront = -1;
return item;
}

void display(int *arr) {
int i;

printf("\n front:  ");
for (i = 0; i < MAX; i++)
printf("  %d", arr[i]);
printf("  :rear");
}

int count(int *arr) {
int c = 0, i;

for (i = 0; i < MAX; i++) {
if (arr[i] != 0)
c++;
}
return c;
}
```

## Time Complexity
- The time complexity of all the above operations is constant i.e. O(1).

## Applications of Deque Data Structure
- In undo operations on software.
- To store history in browsers.
- For implementing both stacks and queues.
