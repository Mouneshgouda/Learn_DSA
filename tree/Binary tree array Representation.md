### Array Representation of Binary Tree with Example

- For the array representation of binary tree, we will form an array of size 2*n+1 size where n is the number of nodes the binary tree. Now we will move step by step 
 for the array representation of binary tree.

1.First, suppose we have a binary tree with seven nodes

 ![image](https://github.com/user-attachments/assets/0e69b452-8a28-40ee-b957-b2483bd14517)

2.Now, for the array representation of binary tree, we have to give numbering to the corresponding nodes. The standard form of numbering the nodes is to start from 
 the root node and move from left to right at every level .After numbering the tree and nodes will look like this:

![image](https://github.com/user-attachments/assets/b8c52aad-a9ad-47ec-be78-95d56baf4096)

3.Now as we have numbered from zero you can simply place the corresponding number in the matching index of an array then the array will look like this:
![image](https://github.com/user-attachments/assets/b7309853-b895-4d2f-9371-cdca62ec4a90)

4.That is the array representation of binary tree but this is the easy case as every node has two child so what about other cases? We will discuss other cases below.

5.In these cases, we will discuss the scenarios for the array representation of binary tree where there the lead node is not always on the last level.

6.So consider the binary tree given below:

![image](https://github.com/user-attachments/assets/f5961f25-8776-452b-84c6-b61c4914bcaf)

7.While giving a number you are stuck with the cases where you encounter a leaf node so just make the child node of the leaf nodes as NULL then the tree will look like this:

![image](https://github.com/user-attachments/assets/f86d298f-2bbb-4254-a4e4-0bcc547c6082)

8.Now just number the nodes as done above for the array representation of binary tree after that the tree will look like this:

![image](https://github.com/user-attachments/assets/4b055df0-f9eb-49c9-ac88-5448f2909732)

9.Now we have the number on each node we can easily use the tree for array representation of binary tree and the array will look like this:

![image](https://github.com/user-attachments/assets/aecaa1ec-de01-4f0c-b8dd-078f8df39c1c)



