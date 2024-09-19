# DFS and BFS: different, but equal

- One of the best ways to understand what breadth-first search (BFS) is, exactly, is by understanding what it is not. That is to say, if we compare BFS to DFS, it’ll be much easier for us to 
  keep them straight in our heads. So, let’s refresh our memory of depth-first search before we go any further.

- We know that depth-first search is the process of traversing down through one branch of a tree until we get to a leaf, and then working our way back to the “trunk” of the tree. In other 
  words, implementing a DFS means traversing down through the subtrees of a binary search tree.
![image](https://github.com/user-attachments/assets/c2c2bf2a-057f-4028-8a21-e00f55dbe800)

![image](https://github.com/user-attachments/assets/0867014a-12b6-4b14-a6f6-52db048df269)

# BFS

- So, we should be able to use a stack structure and do something similar with our BFS implementation…right? Well, I don’t know if it will work, but I think it’ll be helpful to at
- least start 
 - off by drawing out the algorithm we want to implement, and seeing how far we can get with it.

![image](https://github.com/user-attachments/assets/ae67b6d9-cf56-4705-8b50-c4fe2fb94973)

- Okay, so we have a graph to the left that we implemented DFS on last week. How might we use a BFS algorithm on it, instead?

- Well, to start, we know that we want to check the root node first. That’s the only node we’ll have access to initially, and so we’ll be “pointing” to node f.

- Alright, now we’ll have to check the children of this root node.

- We want to check one child after another, so let’s go to the left child first — node d is the node we’re “pointing” to now (and the only node we have access to).

- Next, we’ll want to go to the right child node.

- Uh oh. Wait, the root node isn’t even available to us anymore! And we can’t move in reverse, because binary trees don’t have reverse links! How are we going to get to the right child 
 node? And…oh no, the left child node d and the right child node k aren’t linked at all. So, that means it’s impossible for us to jump from one child to another because we don’t have 
 access to anything except for node d’s children.

- Oh dear. We didn’t get very far, did we? We’ll have to figure out a different method of solving this problem. We need to figure out some way of implementing a tree traversal that will 
 let us walk the tree in level order. The most important thing we need to keep in mind is this:

- We need to keep a reference to all the children nodes of every node that we visit. Otherwise, we’ll never be able to go back to them later and visit them!

- The more that I think about it, the more I feel like it’s as though we want to keep a list of all the nodes we still need to check, isn’t it? And the moment I want to keep a list of 
 something, my mind immediately jumps to one data structure in particular: a queue, of course!

# Let’s see if queues can help us out with our BFS implementation.

- Queues to the rescue!
 As it turns out, a major difference in depth-first search and breadth-first search is the data structure used to implement both of these very different algorithms.

- While DFS uses a stack data structure, BFS leans on the queue data structure. The nice thing about using queues is that it solves the very problem we discovered earlier: it allows us to 
 keep a reference to nodes that we want to come back to, even though we haven’t checked/visited them yet.

- We add nodes that we have discovered — but not yet visited — to our queue, and come back to them later.

- A common term for nodes that we add to our queue is discovered nodes; a discovered node is one that we add to our queue, whose location we know, but we have yet to actually visit. In 
 fact, this is exactly what makes a queue the perfect structure for solving the BFS problem.

![image](https://github.com/user-attachments/assets/4ee0da67-0d39-4984-bfd3-3207c6e8adb1)

- In the graph to the left, we start off by adding the root node to our queue, since that’s the only node we ever have access to (at least, initially) in a tree. This means that the root 
 node is the only discovered node to start.

- Once we have at least one node enqueued, we can start the process of visiting nodes, and adding references to their children nodes into our queue.

- Okay, so this all might sound a little bit confusing. And that’s okay! I think it’ll be a lot easier to grasp if we break it down into simpler steps.

- For every node in our queue — always starting with the root node — we’ll want to do three things:

- Visit the node, which usually just means printing out its value.
- Add the node’s left child to our queue.
- Add the node’s right child to our queue.
- Once we do these three things, we can remove the node from our queue, because we don’t need it anymore! We basically need to keep doing this repeatedly until we get to the point where 
 our queue is empty.

- Okay, let’s look at this in action!

- In the graph below, we start off with the root node, node f, as the only discovered node. Remember our three steps? Let’s do them now:

- We’ll visit node f and print out its value.
- We’ll enqueue a reference to its left child, node d.
- We’ll enqueue a reference to its right child, node k.
- And then, we’ll remove node f from our queue!

 ![image](https://github.com/user-attachments/assets/9e059b90-f667-4fd0-bd2c-d20629f9a14f)





