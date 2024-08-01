### What is a Threaded Binary tree? 

- In a Threaded Binary Tree, the nodes will store the in-order predecessor/successor instead of storing NULL in the left/right child pointers. 

- So the basic idea of a threaded binary tree is that for the nodes whose right pointer is null, we store the in-order successor of the node (if-exists), and for 
 the nodes whose left pointer is null, we store the in-order predecessor of the node(if-exists). 

- One thing to note is that the leftmost and the rightmost child pointer of a tree always points to null as their in-order predecessor and successor do not exist. 

- To understand this, let’s look at an example of a Threaded Binary Tree.

 ![image](https://github.com/user-attachments/assets/aaf3f006-96f4-426d-9be5-e86910149091)

- In the above-given figure, the right pointer of node value 6 points to 9. 

- Now, we will check the left pointer of node 9, and if it is NULL, then we modify the reference to the predecessor of the node, which is 6.
 Then, we will check for the right pointer, and if it is also NULL, we will point it to the successor node, which is 10. Thus, it will point to 10.
 We point to in-order predecessors/successors in left/right pointers using threads (denoted by dotted lines) as shown in the figure above, and that is why it is 
 known as a Threaded Binary Tree. 
 Since the leftmost pointer of this tree is the left pointer of node value 5 and the rightmost pointer of this tree is the right pointer of node value 20, they 
 both point to NULL.
 
- The main idea behind setting such a structure is to make the inorder and preorder traversal of a binary tree faster without using any additional Data structure 
 (e.g. auxiliary stack) or memory for its traversal.


### Types of Threaded Binary tree

# There are two types of Threaded Binary Trees:

- One-way Threaded Binary Tree
- Two-way Threaded Binary Tree

- 1. One-way Threaded Binary Tree 
 In this type, if a node has a right null pointer, then this right pointer is threaded towards the in-order successor’s node if it exists. 

- The following diagram depicts an example of a Single-Threaded Binary Tree. Dotted lines represent threads.
 ![image](https://github.com/user-attachments/assets/b815f29e-9967-41d7-ba4b-24a0b80d68db)

- In the figure given above, you can observe the node value 20 does not have any child nodes. So, the right pointer of node value 20 is null and therefore, it is 
 pointing to its in-order successor (node value 30) through a thread. Similarly, the other nodes of this tree containing a right null pointer refer to their in- 
 order successor, as shown.

### 2. Two-way Threaded Binary Tree
- In this type, the left null pointer of a node is made to point towards the in-order predecessor node and the right null pointer is made to point towards the in- 
  order successor node. 

- Here, the leftThread and rightThread boolean variables help us to differentiate whether the left/right pointer stores the in-order predecessor/successor or left 
 child/right child.

- Let’s look at an example to understand this.

![image](https://github.com/user-attachments/assets/78c11a68-86e9-4e6e-9a93-a70104962e52)

- This is how a Double-Threaded Binary Tree looks like. You can observe here that node value 40 have no left and right child. So, its left pointer points to its 
 in- order predecessor (node value 30) and it's right pointer points towards its in-order successor (node value 50). Similarly, the other nodes of this tree with a 
 left/right null pointer refers to their in-order predecessor/successor using threads. 
