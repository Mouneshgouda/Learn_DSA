# Meet the Binary Tree
- A binary tree, on the surface, looks just like a boring regular tree that allows us to store data in a hierarchical manner. Below is an example of what a binary tree looks like:

- ![image](https://github.com/user-attachments/assets/0eb55c4b-6359-4628-b129-d00b46ca799c)

- 1.What makes binary trees different is that, unlike regular trees where anything goes, we have three strict rules our tree must adhere to in order to be classified as a binary tree. The rules are:

- 2.Each node can only have 0, 1, or 2 children

- 3.The tree can only have a single root node

-4.There can be only one path to a node from the root

-5.Let's dive a bit deeper into these rules, for they are important to understand. They will help explain why the binary tree works the way it does, and it sets us up for learning about other tree variants, such as the binary search tree next.

### Rules Explained
- The first rule is that each node in a binary tree can only have 0, 1, or 2 children. If a node happens to have more than two children, that’s a problem:

![image](https://github.com/user-attachments/assets/2d3c4446-12eb-482d-8bef-c204c22379a6)

The second rule is that a binary tree must have only a single root node:

![image](https://github.com/user-attachments/assets/e46ae128-de9b-468c-a2fc-f40e4c04436f)

In this example, we have both the A node and the AA node competing for who gets to be the primary root. While multiple root nodes is acceptable in certain other tree-based data structures, they aren’t allowed for binary trees.

Now, we get to the last rule. The last rule is that there can be only one path from the root to any node in the tree:

![image](https://github.com/user-attachments/assets/4b11fcf8-d7b7-4a1c-9941-a91c0bedd839)


## Binary Tree Variants
- Binary trees, even with their stricter rules, appear in a handful of popular variants. These variants play a large role in how well our friendly binary tree performs at common data operations, how much space it takes up, and more. For now, we’ll avoid the math and focus on the high-level details.

## Full Binary Tree
- The full binary tree, sometimes referred to as either a strict binary tree or proper binary tree, is a tree where all non-leaf nodes have their full two children:

![image](https://github.com/user-attachments/assets/5c4f78ca-9cb1-4dd6-803e-ac6e25fd2194)

- In this example, we can see that the non-leaf nodes A, B, and E all have two children.

## Complete Binary Tree
- A complete binary tree is one where all rows of the nodes are filled (where each parent has two children) except for the last row of nodes:

  ![image](https://github.com/user-attachments/assets/b126e048-2296-4c23-8ede-2a0b72c78483)

- For this last row, there are some rules on how the nodes should appear. If the last row has any nodes, those nodes need to be filled continuously, starting from the left with no gaps. This wouldn’t be acceptable, for example:

- ![image](https://github.com/user-attachments/assets/9bfddfe8-2cb7-4acd-aa47-76310d7507d6)

- There is a gap where the D node is missing its right child, so we weren’t continuously filling in the last row of nodes from the left.

## Perfect Binary Tree
- A perfect binary tree is a binary tree where every level of the tree is fully filled with nodes:

![image](https://github.com/user-attachments/assets/1aae2e7c-daea-4b4c-bcb1-6e1acce644e1)

- As a consequence of that requirement, all the leaf nodes are also at the same level.

## Balanced Binary Tree
- A balanced binary tree is a binary tree in which the height of the left and right subtrees of each node is not more than one apart. Below is an example of a balanced binary tree:

- ![image](https://github.com/user-attachments/assets/5577b7c9-73f6-4999-985a-1bc91170325b)

## Degenerate Binary Tree
- In a degenerate binary tree, each parent node has only one child node:
![image](https://github.com/user-attachments/assets/294b0ff0-0157-4c73-98ba-51a0c5033807)



- This means that the tree is essentially a linear data structure, like an array, with all nodes connected in a single path. Any advantages a tree-like structure provides are lost here, hence the degenerate classifier.

