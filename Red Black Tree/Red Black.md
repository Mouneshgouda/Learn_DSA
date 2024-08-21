# Red Black Tree:

![image](https://github.com/user-attachments/assets/2273e0e5-dd7b-4b2d-9806-55e993b047c9)

![image](https://github.com/user-attachments/assets/43d2fefa-3de8-4ba2-93e3-80db1d70ec5e)

- A red-black tree is a type of self-balancing binary search tree, very similar to other self-balancing trees, such as AVL trees. However, a red-black tree is a 
 structure that has to adhere to a very strict set of rules in order to make sure that it stays balanced; the rules of a red-black tree are exactly what enables it 
 to maintain a guaranteed logarithmic time complexity.

- On the most basic level, a red-black tree must follow four rules, no matter what. In every aspect of building and shrinking (inserting or deleting from) this tree, 
  these four rules have to be followed; otherwise, the data structure cannot be considered a red-black tree.

  Property Of Red Black Tree:

![image](https://github.com/user-attachments/assets/a2960036-7571-4524-91ac-8c5d7350a6b1)

Generally speaking, the four rules of a red-black tree are always presented in the same order, as follows:

- 1.Every single node in the tree must be either red or black.
- 2.The root node of the tree must always be black.
- 3.Two red nodes can never appear consecutively, one after another; a red node must always be preceded by a black node (it must have a black parent node), and a 
 red node must always have black children nodes.
- 4.Every branch path — the path from a root node to an empty (null) leaf node — must pass through the exact same number of black nodes. A branch path from the root to an empty leaf node is also known as an unsuccessful search path, since it represents the path we would take if we were to search for a node that didn’t exist within the tree.
- These rules start to make a lot more sense when we see them in action, so let’s take a look at some red-black trees (and non-trees) to try to understand what’s 
going on.

In the example shown here, the first tree has three black nodes. Notice that the two children nodes each have pointers to null leaf nodes. It might be obvious, but it’s work remembering this:

- 5.a null leaf node is always considered to be a black node, not red.

  ![image](https://github.com/user-attachments/assets/cc830408-9e77-417d-b86c-2a611a228ee1)

- The first red-black tree adheres to all four rules:

1.every node is red or black,
2.the root node is black,
3.no two red nodes appear consecutively,
4.and, finally, the path from the root node to all four null leaf nodes passes through two black nodes (either 2 and then 1, or 2 and then 3) on the way to the null leaves.

- Interestingly, the second example is also a valid red-black tree. The main difference here is that the child nodes, 1 and 3 are both red. However, neither of the 
 two red nodes appear consecutively, so this tree still doesn’t violate the third rule. Also, the branch paths from the root to all the null leaf nodes pass 
 through the same number of nodes in this case, too — we pass through just one black node, the root, on the path from the root to a null node. So, we’re not 
 violating the fourth rule, either.

- At first, it might seem as though following these four rules is pretty easy to do; we created two red-black trees just now without violating any rules, right? 
 Well, as we’re about to discover, these rules are super strict and very easy to break.

- The best way to demonstrate this is with an example of three chained nodes.

- In the illustration shown here, we have four potential different options for how we could create a red-black tree with three nodes, 1, 2, 3. In fact, we probably 
 have more options, but let’s assume that we’re not going to consider making a tree that doesn’t have red and black nodes, and a root node that is black.

![image](https://github.com/user-attachments/assets/f8325d28-0660-4d4f-ab1e-73fc00e88088)

- In tree a, we have a black root, and two consecutive red nodes. We can tell from just looking at this tree that this is a problem; we’re violating rule three!

- In tree b, we have a black root, a black child node, and a red grandchild. This might seem fine, but…remember rule four? The path from the root node to every 
 null leaf nodes should pass through the same number of black nodes, no matter which branch path we take. The path from 1 to it’s left null child passes through 
 only one black node, while the path to 2's left child passes through two black nodes. Well, that totally breaks the fourth rule!

- The same problem occurs for trees c and d; the path from the root node to each null node passes through a slightly different number of black nodes, which means 
 that none of these trees are actually valid red-black trees!

- As it turns out, there is a well-known proof in the realm of red-black trees that proves exactly what we just saw:

 A chain of three nodes cannot possibly every be a valid red-black tree.

- These rules are turning out to deceptively more strict than they first seemed, right? Well, even though they might seem like a total pain to follow, they’re 
 pretty important — not to mention powerful. Let’s try to unpack why!

Red Black Tree Rotations:
![image](https://github.com/user-attachments/assets/6d31c9b6-f5d0-40ab-af67-205cce2b6546)

- Another handy trick for handling rule violations is one that we encountered earlier in this series: rotations! We learned about rotations (or “glorified swaps” 
 as I like to think of them) when we explored AVL trees.

- We can do something similar when it comes to red-black trees, too. In the drawing shown here, we have a red-black tree that is unbalanced; ignoring the colors of 
 the nodes for a moment, let’s say that we need to rotate and re-balance this tree.

- In the first drawing, we are left-rotating on the root node, 4, so that it’s right child, 11, becomes the new parent. This is called a left-rotation. Similarly, 
 if we right-rotate on the new parent node, 11, and shift it down so that it once again becomes the right child of 11, we’re performing a right-rotation.

- Notice how the structure of the tree changes as we rotate in both of these cases; in our left-rotation, the subtree of 9-5-10 moved from the right subtree to the 
 left. Conversely, in our right-rotation, the same subtree of 9-5-10 moved from the left subtree back to the right. Rotations tend to move around and restructure 
the subtrees of a larger red-black tree, which can also be helpful in preventing any rule violations.

![image](https://github.com/user-attachments/assets/a3ab7ce7-0ccd-4b66-85e0-afae87d0c01f)

- Let’s look at one more example of how recoloring and rotation can help us in inserting nodes into a red-black tree.

- Remember: it’s easiest to start off by always inserting a red node, and then recoloring and rotation as necessary, afterwards.

- We’ll start with a single root node of 21, which will be red. But, since this is the root node, and one of our rules is that the root node must always be black, 
 we can recolor node 21 to be black. Now, no rules are violated!

- Next, we’ll insert a node with a value of 8 into the tree, as the left child of the root. We can insert it as a red node and not violate any rules in the 
  process!

- Next, we’ll insert a node with a value of 3. Inserting this node as the left child of 8 violates rule three, since we’ll have two consecutive red nodes. In 
 order to fix this, we’ll need to rotate the grandparent node (the root) and then recolor.
![image](https://github.com/user-attachments/assets/d2107864-da83-42c0-8fdb-fcf67472676d)

- If we right-rotate the root node, and shift 21 down to become the right child of 8, we’ve taken one step to fixing our problem. The node 8 is our new root node, 
 with two children, 3 and 21.

- However, now we’re violating our root node rule yet again!

- Not to worry — we can just recolor our original parent node of the newly-inserted node (which is now the right child), 21, and the root node, 8. If we recolor 8 
  and 21, our root node is back to being black, and our two child nodes are both red.

- And, most important of all, no rules are violated, and we have a perfectly-balanced red-black tree!

  Operation Red Black Tree:

  https://www.cs.usfca.edu/~galles/visualization/RedBlack.html



