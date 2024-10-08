# Representation of Graphs:
### There are two ways to store a graph:
 1. Sequential representation (or) Adjacency matrix representation)
 2. Linked list representation (or) Adjacency list representation)

### 1.Adjacency Matrix/ Sequential representation:

- In this method, the graph is stored in the form of the 2D matrix where rows and columns denote vertices. Each entry in the matrix represents  the weight of the 
 edge between those vertices.

![image](https://github.com/user-attachments/assets/1710f727-5bfe-4708-9bd0-24aa2e42991f)

### Code For  Adjacency matrix representation
```c
#include <stdio.h>

#define MAX_NODES 5

// Function to add an edge to the adjacency matrix
void addEdge(int graph[MAX_NODES][MAX_NODES], int start, int end) {
    graph[start][end] = 1;
    graph[end][start] = 1; // Because it's an undirected graph
}

// Function to print the adjacency matrix
void printMatrix(int graph[MAX_NODES][MAX_NODES], int nodes) {
    printf("Adjacency Matrix:\n");
    for (int i = 0; i < nodes; i++) {
        for (int j = 0; j < nodes; j++) {
            printf("%d ", graph[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int graph[MAX_NODES][MAX_NODES] = {0}; // Initialize the matrix with zeros
    int nodes = 5;

    // Adding edges
    addEdge(graph, 0, 1);
    addEdge(graph, 0, 4);
    addEdge(graph, 1, 2);
    addEdge(graph, 1, 3);
    addEdge(graph, 2, 3);
    addEdge(graph, 3, 4);

    // Print the adjacency matrix
    printMatrix(graph, nodes);

    return 0;
}

```

# Adjacency List/ Linked list representation:
- This graph is represented as a collection of linked lists. There is an array of pointer which points to the edges connected to that vertex.

![image](https://github.com/user-attachments/assets/79b4946d-e721-4d0e-8fdc-f03137fbf20d)

### Adjacency List Code
```c
#include <stdio.h>
#include <stdlib.h>

// Structure to represent a node in the adjacency list
typedef struct Node {
    int vertex;
    struct Node* next;
} Node;

// Structure to represent the graph
typedef struct Graph {
    int numVertices;
    Node** adjLists;
} Graph;

// Function to create a new node
Node* createNode(int vertex) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->vertex = vertex;
    newNode->next = NULL;
    return newNode;
}

// Function to create a graph with 'vertices' number of vertices
Graph* createGraph(int vertices) {
    Graph* graph = (Graph*)malloc(sizeof(Graph));
    graph->numVertices = vertices;
    graph->adjLists = (Node**)malloc(vertices * sizeof(Node*));

    for (int i = 0; i < vertices; i++) {
        graph->adjLists[i] = NULL; // Initialize each adjacency list to NULL
    }

    return graph;
}

// Function to add an edge to the graph
void addEdge(Graph* graph, int src, int dest) {
    // Add an edge from src to dest
    Node* newNode = createNode(dest);
    newNode->next = graph->adjLists[src];
    graph->adjLists[src] = newNode;

    // Add an edge from dest to src (for undirected graph)
    newNode = createNode(src);
    newNode->next = graph->adjLists[dest];
    graph->adjLists[dest] = newNode;
}

// Function to print the adjacency list of the graph
void printGraph(Graph* graph) {
    for (int i = 0; i < graph->numVertices; i++) {
        Node* temp = graph->adjLists[i];
        printf("Vertex %d:", i);
        while (temp) {
            printf(" -> %d", temp->vertex);
            temp = temp->next;
        }
        printf("\n");
    }
}

// Main function to demonstrate adjacency list operations
int main() {
    int vertices = 4; // Number of vertices
    Graph* graph = createGraph(vertices);

    // Adding edges
    addEdge(graph, 0, 1);
    addEdge(graph, 0, 2);
    addEdge(graph, 1, 2);
    addEdge(graph, 2, 3);

    // Printing the adjacency list
    printGraph(graph);

    // Freeing allocated memory
    for (int i = 0; i < vertices; i++) {
        Node* temp = graph->adjLists[i];
        while (temp) {
            Node* next = temp->next;
            free(temp);
            temp = next;
        }
    }
    free(graph->adjLists);
    free(graph);

    return 0;
}
```c
