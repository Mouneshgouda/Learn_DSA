![image](https://github.com/user-attachments/assets/7934b4a9-9af6-4d3b-b792-996e68591e74)

- A binary search tree is balanced if any two sibling subtrees do not differ in height by more than one level. In other words, any two leaves should not have a 
  difference in depth that is more than one level. We’ll remember that every binary search tree recursively contains subtrees within it, which in turn contain 
  subtrees within them. In order for a BST to truly be balanced, it’s two outermost parent subtrees must be balanced, as should every internal subtree withing the 
  structure, as well.

- Okay, so what’s the deal with a “height-balanced” tree? Well, the height of a tree is the number of nodes on the longest path from the root node to a leaf. Given 
  that definition, a height-balanced tree is one whose leaves are balanced relative to one another, and relative to other subtrees within the larger tree.
```
  - An easy way to remember what makes for a height-balanced tree is this golden rule: in a height-balanced tree, no single leaf should have a significantly longer 
   path from the root node than any other leaf on the tree.
```

- For example, the two trees shown in the illustration here look awfully similar at first glance. However, the first one is balanced, while the second is not.
![image](https://github.com/user-attachments/assets/8d4667c6-d99e-43aa-b978-3c7295049bf9)

- In the first tree, the difference between the left and right subtrees does not differ by more than one level. The left subtree’s nodes extend to the second 
 level, while the right subtree’s nodes extend to the third level.

- If we compare this to the bottom tree, we can see an immediate difference: the bottom tree’s subtrees differ by more than one level in height. The bottom tree’s 
 left subtree extends only to the first level, while its right subtree extends to the third level.

- Remember our golden rule of height-balanced trees?

- No single leaf should have a significantly longer path from the root node than any other leaf on the tree.

- In the top (balanced) tree, the longest path is only one node longer/one level deeper than other nodes on it’s comparative sibling subtree. But in the bottom 
 (unbalanced) tree, the longest path is two nodes/two levels deeper than the other node on its sibling subtree.

# Weighing the AVL scales:

- Now that we understand the rules and reason behind AVL trees, let’s see if we can distinguish and convert between AVL trees when we need to!

- In the tree drawn below, there are 6 nodes (including the root) and a left and right subtree.

  ![image](https://github.com/user-attachments/assets/d1446a5d-7cc4-4fde-9246-05b65fd9af76)

- The height of the entire tree is 4, since the path from the root to the longest leaf e is 4 nodes. The height of the left subtree is 2, since the root node, a, 
 of the left subtree has only one leaf, meaning that the longest path from a to b is 2 nodes. Similarly, the height of the right subtree is 3, since the longest 
 path from the right subtree’s root d to e, is 3 nodes.

- The children of node d have heights that differ by more than one level; node f’s height is 2, while its sibling, the left subtree of node d, is empty, with a 
 height of 0. Since node d’s subtrees differ in height by more than one level, this is certainly not an AVL tree, as it violates one of the key rules of an AVL.

- Okay, so this is not an AVL tree; but, we know that an AVL tree would be super useful, right? So, how can we turn this tree into an AVL tree?

- Well, since we know the rules for an AVL tree, and we know how to make it a height-balanced tree, we could potentially try to rearrange these nodes in such a way 
 that this currently unbalanced tree will quickly become height-balanced.

![image](https://github.com/user-attachments/assets/13cb88dc-5be6-41b7-a974-b8ad7b21950a)

- If we rearrange node d and its descendants, we can reformat the exact same BST we were just dealing with into an AVL tree, which is balanced. All we’ve done, 
 really, is shifted around the right subtree. Where the right subtree once had a root node of d, it now has a root node of e, with two children beneath it.

- The logic for how we rearranged those nodes stems from the balancing formula that every AVL tree will adhere to: if the subtrees of a node has heights h1 and h2, 
 then the absolute value of the difference of those two heights must be less than or equal to (≤) 1. In other words, the difference between the heights of two 
 subtrees in an AVL tree should never exceed 1 level.

![image](https://github.com/user-attachments/assets/0f90a7a8-4599-4bf5-ae76-f1b829add058)

# Avl Tree Rotations:
- We can think of AVL trees as a super clever set of scales, which can just magically balance themselves out evenly, no matter what you put on them. And, what’s 
 more, no matter what you choose to be the center point of the data, the AVL “scales” will reconfigure itself so that the data is reorganized to be as balanced as 
 possible.

- For example, in the unbalanced BST we initially looked at, our input data was ordered and inserted in a descending manner, which made our AVL “scales” look very 
 lopsided. In order to self-balance this tree the way that an AVL tree would do, we’d need this tree to be even on both sides of the “scales”, so that no matter 
 what the root node is, the scales and subtrees would balance out correctly.

![image](https://github.com/user-attachments/assets/d327f1d2-9109-4147-9516-79c007d03b47)

- Except, of course, that AVL trees aren’t doing this work of balancing themselves magically. Rather, they’re employing a lot of logic under the hood, which 
 perhaps makes them seem magical (and a tad bit intimidating, I’ll admit)!

- So what exactly is this logic? Well, to be totally honest, it really is nothing more than some fancy node swapping! If you’re feeling like you’ve heard of this 
 before, it’s because you have. We dealt with node swapping back when we were learning about heaps; in order to maintain the structure of a heap, we had to swap 
 nodes in order to keep both the correct order of nodes as well as the correct heap structure.

- In the context of height-balancing trees, the correct term for this kind of “glorified node swapping” is “rotations”. When it comes to AVL trees, there are two 
 main types of rotations to use in order to rearrange nodes in a tree and do the hard work of self-balancing: single rotations and double rotations.

# Single rotations:
- Single rotations are by far the simplest way to rebalance an unbalanced tree. There are two types of single rotations: a left rotation and a right rotation. A - 
 left rotation is useful if a node is inserted into the right subtree of another, higher up node’s right subtree, and that insertion or a deletion causes a tree to 
 become unbalanced.

In the image shown here, a left rotation is performed on an unbalanced tree, with a root node of 1, and a right subtree with a node of 2, with its own right subtree/node of 3.

![image](https://github.com/user-attachments/assets/ac34dd4d-1e84-448c-9b9d-2b159a3e6e36)

- Since this tree is currently unbalanced, we swap the right subtree and perform a left rotation to make node 1 the left subtree of 2. This not only maintains the 
 numerical order/structure of the elements as one would expect for a BST, but it also balances the tree so that both 1 and 3are in their correct locations 
 relative to the new root node, 2.

- As you might have already guessed, a right rotation is the exact opposite of this scenario. If a node is inserted into the left subtree of another child node’s 
 left subtree (and the tree becomes unbalanced as a result), then we can perform a left rotation on the tree, so that 9, the former left subtree of the root node 
 10, becomes the new root node, and 8 and 10 become its respective left and right subtrees.

- Sometimes, however, a single rotation just won’t cut it. In those scenarios, desperate times call for double rotations: namely, either a left-right rotation, or 
 a right-left rotation. And yes, they probably are implemented in exactly the way that you expect they would be.

#Double Rotation:

![image](https://github.com/user-attachments/assets/3e61525a-20e9-442d-8f9e-45d6a231c10f)

- A left-right rotation is a combination of a left rotation, followed by a right rotation. In the examples shown here, we perform a left-right double rotation on 
 the tree with a root node 3, a left subtree with a node 1, with its own right subtree and a node of 2. Once we perform a left rotation on the left subtree, our 
 tree is a little easier to deal with. Our tree has transformed from 3–1–2 into 3–2–1. We’re back to something familiar: a left subtree of a left subtree. Since 
 we already know how to handle those kinds of trees, we can easily perform a right rotation on the left subtree, so that 2 is now the new root nodes, and 1 and 3 
 are its children.

- Conversely, a right-left rotation is the exact same thing, but in the reverse order. A right-left rotation is a combination of a right rotation followed by a 
 left rotation.

- And thus, with some super fancy swapping, these clever trees do some very important and smart work: they make sure that we can leverage the awesomeness of 
 binary search trees and their efficient runtime. AVL trees are amazingly helpful in ensuring that, no matter what we add or remove from an AVL tree, our 
 structures are smart and flexible enough to rebalance themselves and handle whatever we throw their way! And for that, I am deeply grateful that someone else was 
 around to ask these tough questions (and come up with an elegant solution) over half a century ago, before you or I even could.

#Avl Tree Operations:

https://www.cs.usfca.edu/~galles/visualization/AVLtree.html


