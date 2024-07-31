# Tree

- To retrace our steps a bit, a tree data structure is a way of organizing data in a hierarchical manner. Just like in nature, trees in our computer world come in 
 many shapes and sizes. For our purposes, let’s visualize one that looks as follows:

![image](https://github.com/user-attachments/assets/a8b1207d-c663-4e72-887c-402a6fd0a99c)


- We see a bunch of circles and lines connecting each circle. Each circle in the tree is known as a node. The node plays an important role in a tree. It is 
 responsible - for storing data, and it is also responsible for linking to other nodes. The link (visualized as a line) between each node is known as an edge:

![image](https://github.com/user-attachments/assets/37747cea-6871-40d6-91a7-cb535a2c20a6)



# Trees in Data Structures     ![tree](https://github.com/user-attachments/assets/d0a72a05-e5bf-42ed-aae6-5bb0708268d9)

- A tree is a hierarchical data structure, which has one root node and multiple child nodes(branches). Unlike, Arrays, Linked Lists, Stacks or queues, a Tree is non 
  linear data structure.



## Classification of Trees   ![tree-1](https://github.com/user-attachments/assets/8bbf1b60-cf17-48dd-a61c-2288d0317c30)

- Trees are classified by the following types – 
```c
By Max number of branches – Binary, Ternary, n-ary
By Heights of subtree – Full, complete, perfect, balanced (Check this page)
The following diagram shows one example of each –

Binary Tree: A tree where each node can have a maximum of two child nodes
Ternary Tree: A tree where each node can have a maximum of three child nodes
n-ary Tree: A tree where each node can have a maximum of n child nodes
This n value is sometimes called as the degree of the tree.

```

## Why Trees?   ![architecture-and-city](https://github.com/user-attachments/assets/6fc0b239-ad32-40fd-a9b2-51a2d6f7d23d)

```c
Hierarchical approach
```
- One reason could be that we want to store information that follows, natural hierarchy, like how we store folders in a computer system.
```c
No Upper Limit
```
- Trees, unlike arrays, stacks, queues do not have an upper limit on how many nodes can be created, as they are created using pointers
```c
Quicker Search and Access
```
- Trees (BST) are able to do searching quicker than arrays, linked lists etc
```c
Moderate Insertion/Deletion
```
- Trees provide moderate insertion/deletion (Slower than Linked lists, quicker than arrays)
 Trees

### Technical Description of Trees  

- Trees can defined as a collection of  entities, that constitute it’s frame, known as nodes.
- Nodes are the basic building blocks of a tree structure that store some data/value .
- These are  ADT (Abstract Data Structures) which form a hierarchical layout comprising of a single root node followed by parent nodes and children nodes, which 
 are connected to each other via edges.

- Since trees are flexible and powerful data structures, they are multipurpose data structure that provide a wide range of applications to the user.

![introduction](https://github.com/user-attachments/assets/dcb9501b-6494-4cfe-9aa5-ab8f17027386)


## Components
```c
Root
Parent
Child nodes
Siblings
Leaves
Brach
Sub-Tree
Ancestor
Descendants
Null Nodes
```
## other Components
```c
Degree
Edges
Path
Depth
Level
Height
```

### 1. Root  


```c
The topmost node of  a tree is known as the root.
There exists only one root node per tree.
Taking the image above as reference, node ‘a’ is the root of the tree as shown here.

```
![image](https://github.com/user-attachments/assets/1056facf-9094-4ed5-8a9f-931101a38666)
### 2. Parent

```c
Any node which has an edge directed downwards to the child node is known as parent node.
Each parent can have one or more child node.
In the given image we can see, the node ‘a’ is the parent of the nodes ‘b’ and ‘c’.
```
 ![parent](https://github.com/user-attachments/assets/43b17fda-0b6d-47f3-ad93-62ef9bcd2645)
 
### 3. Child Node
```c
Any node which has an edge directed upwards to the parent node is known as child node.
Each child node has a single parent node.
In the given image we can see, the nodes ‘h’ and ‘i’ are the child nodes of the node ‘d’.
```
![child](https://github.com/user-attachments/assets/6e4ef546-794a-4065-bf55-b169dcd523f1)

### 4. Sibling
```c
A set of nodes that are extended from the same parent are known as the siblings.
In the given image, we can see that
the nodes ‘b’ and ‘c’ are sibling nodes. 
the nodes ‘h’ and ‘i’  are sibling nodes.
```
![sibling](https://github.com/user-attachments/assets/28e7cbc4-e3ea-42a6-8146-4a7b831b6969)

### 6. Leaf(external nodes)
```c
Any node that does not have any child node is known as the leaf node.
In the given image, the nodes ‘f’, ‘h’, ‘i’, ‘j’, ‘k’, ‘l’ and ‘m’ are leaf nodes since these nodes are terminal and have no further child nodes.
Total Number of leaf nodes in a Binary Tree = Total Number of nodes with 2 children + 1
```
![leaf](https://github.com/user-attachments/assets/e4e75d16-25d5-43e2-980e-2dd8b466f1d2)


### 6. Branch(internal nodes)
```c
Any node which has at least one child node is known as branch node.
In the given image, the nodes ‘b’ , ‘c’ , ‘d’ , ‘e’ , ‘g’ are branch nodes since each of these nodes extend further to their respective children.
branch
```
![branch](https://github.com/user-attachments/assets/f6df24e3-02df-4c3d-aa57-eaa972843924)


### 7. Sub-Tree
```
A sub tree of a tree is defined as a tree that consist of a node along with all it’s descendants.
In the image , we can see that a sub tree can be extended from node ‘b’ which will be termed as the left sub tree.
Similarly, a sub tree can be extended from the node ‘c’ which will be termed as the right sub tree. 
subtree
```
![subtree](https://github.com/user-attachments/assets/34d81ad5-b823-4b42-a29b-cffe17f95b47)

### 8. Ancestor
```c
Any predecessor of a node along with all the ancestors of the predecessor of that node is known is as the ancestor.
The root node has no ancestors.
In the given image, the ancestors of the node ‘h’ will be ‘d’, ‘b’ and ‘a’.

```
![ancestors](https://github.com/user-attachments/assets/7e0259ae-838a-4362-9edb-554adddc2bd8)

### 9. Descendant
```c
All the children of a node along with all the descendants of the children of a node is known as descendant.
A leaf node has no descendants.
In the given image, if we consider the node ‘c’, the descendants of node ‘c’ will be nodes ‘f’ , ‘g’ , ‘l’ and ‘m’ .
```
![decendant](https://github.com/user-attachments/assets/4f4e1eeb-a848-4776-8103-77dd0bf95869)

### 10. Null Nodes
```c
If in a binary tree, a node has only one child it is said to have a single null link.
Similarly if a node has no child node it is said to have two null links.
We can see in the image given the two cases of null links.
```
![null-link](https://github.com/user-attachments/assets/24116652-d620-41ec-be0c-88d3f385efac)

## Terminologies

## 1. Degree.
```c
1.The degree of a node can be defined as it’s number of sub trees.

2. A node with zero degree is a leaf node.

3.A node with maximum degree is the root node in the tree.
```
![degree](https://github.com/user-attachments/assets/a8a31bbd-7a4b-469d-80f5-b30b0963997a)

## 2. Edge
```c
1.An edge can be defined as a connection or a link from one node to another node.

2.In the given image, we have 3 edges from node ‘a’ to node ‘h’.

3.If we see the image, we can see clearly that we have a total of 13 nodes and 12 edges.

3.Thus, we can say that ,

No. of edges  =   No. of nodes  –  1
```
 
![edge](https://github.com/user-attachments/assets/dd63af67-83ad-4993-a42f-bedeba82c337)


## 3. Path
1.A course of nodes and edges for operations such as traversal,etc is known as a path.

2.Let us see with the help of an example taking the image as reference,

3.The path from node ‘a’ to the node ‘h’ is represented in red which consist of 4 nodes and 3 edges.

4.Similarly, the path from node ‘a’ to ‘l’ is represented in purple which consist of 4 nodes and 3 edges.

![path](https://github.com/user-attachments/assets/2d2c310e-5812-4892-86c5-0633f3812c12)


## 4. Depth
1.The number of edges that lie in between the path from a node to the root in a tree is defined as the depth of the tree. 

2.In the image given here, we can see the depth of each node. For instance the depth of the root node is zero.
![depth](https://github.com/user-attachments/assets/c8d296e9-5eac-4b02-a663-6a7155a79ffb)


## 5. Level
```c
1.Level of a node is symbolic of the generation of a given node. It is one greater than the level of it’s parent.

2.For instance, in the given image we can see, the level of the node ‘b’ and ‘c’ is one more than the level of their parent node ‘a’.

Note – Formula Max number of nodes at any given level for the tree would be

2L (If level Starts from 0)
2L-1 (If level Starts from 1)
Example (Considering level starts from 1) – 

Level 1 (Max nodes) =21-1 = 1
Level 2 (Max nodes) =22-1= 2
Level 3 (Max nodes) =23-1= 4
Level 4 (Max nodes) =24-1= 8
Thus max possible nodes in the tree for Level 4 would be

21-1 + 22-1 + 23-1 + 24-1 = 1 + 2 + 4 + 8 = 15
This above can be generalised to a formula as :

Maximum number of nodes (Considering Level Starts from 1) =

1 + 2 + 4 + 8 + … + 2L-1 = (2L – 1)
The above formula will change to (2L+1 – 1) (If level starts from 0)
```
![level](https://github.com/user-attachments/assets/dd8558b2-2519-4776-ac14-221306b90443)

### Formula summary
```c


Formula Max number of nodes at any given level for the tree would be:
2L (If level Starts from 0)
2L-1 (If level Starts from 1)

Formula Max number of nodes in the whole tree would be:
2L+1 -1 (If level Starts from 0)
2L - 1 (If level Starts from 1)
×Dismiss this alert.
```

## 6. Height
```c
1.Height of a node can be defined as the longest path downwards between the root node and a leaf.

2.For example in the given image, we can see that the height of the node ‘l’ is 3; since the distance between it and the root node is 3.

3.Height of a tree starts from 0

Formula –

Height of tree is h then Max nodes a Full Binary Tree will have

(2h+1 – 1)nodes  (if h starts from 0)
(2h – 1)nodes  (if h starts from 1)
Formula – Minimum number of nodes in a Binary Tree of height h would be

(h + 1) (if h starts from 0)
h (if h starts from 1)
Formula – In a Binary Tree with N nodes, minimum possible height

(Log2(N+1) – 1) (if h starts from 0)
Log2(N+1) (if h starts from 1)
```
![height](https://github.com/user-attachments/assets/00a717b8-f2e9-46a1-9cab-288e16c5351f)






