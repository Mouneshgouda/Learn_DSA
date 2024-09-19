

![image](https://github.com/user-attachments/assets/d2a359d8-0c1f-43f5-aa5b-5a38b1fd50d2)

# DFS Traversal

![image](https://github.com/user-attachments/assets/38ca2fda-76eb-47f8-924e-74f60a7b4b18)

![image](https://github.com/user-attachments/assets/0d91029e-9e24-4244-ae1f-52c33e8b1bd8)

# Depth-first, in action

- When it comes to both breadth-first search and depth-first search, there are only two major points to keep in mind when initiating a graph traversal: first, we can choose any arbitrary node 
 to start our traversal with, since there is no concept of a “root” nodes the way that there are in tree structures. And second, whatever we do, we want to ensure that we don’t repeat any 
 nodes; that is to say, once we “visit” a node, we don’t want to visit it again. Similar to what we did with the breadth-first search algorithm, we’ll mark every vertex we visit as “visited” 
 in order to ensure that we don’t repeat nodes in our traversal unnecessarily.

![image](https://github.com/user-attachments/assets/6605dd39-b470-4440-a18f-45abd029c384)

- So, let’s try to run a DFS algorithm on the directed graph above, which has seven nodes that we’ll end up needing to check, or “visit” in the course of our graph traversal.

- We can arbitrarily choose any node to start with, let’s choose node a as our starting “parent” node. Since we know that depth-first search is all about finding out whether a path exists 
 or not between two nodes, we’ll want to be sure that we can keep track of where we came from as we walk through our graph — in other words, we’ll need to keep some kind of trail of 
 “breadcrumbs” as we traverse.

![image](https://github.com/user-attachments/assets/a3f9e444-7c70-4a01-a36c-d82c44e2e3e4)

- or every node that we visit, we’ll keep track of where we came from and use that to both backtrack when we need to, and also as an easy way to keep track of the path that we’re 
 constructing through the graph. When we choose node a as our “parent” node, we’ll set a parent pointer reference, just like we did with our BFS algorithm. Since the “parent” vertex is the 
 first one we’re visiting in this algorithm, it doesn’t have a “parent” pointer, since we’re not coming from anywhere!

-So, we’ll set node a's parent pointer to NULL, and mark node a as “visited”. A simple way to keep track of which node we’re currently searching through is by employing a stack data 
 structure. The moment that we check node a, we can push it right on top of our stack. Since our stack is empty to start with, node a is the only element that’s actually in our stack. 
 We’ll mark it as “visited”.

- Next, we’ll want to (recursively) visit every single node that is reachable from node a. Just as it doesn’t matter which node we start with, it doesn’t really matter which neighboring 
 vertex we visit next — just as long as the vertex is reachable, and is one of the neighbors of a. For example, we could arbitrarily choose to visit node c next.

![image](https://github.com/user-attachments/assets/71daa192-4161-40c7-8229-dd32303fa2b4)

- We’d push it onto the stack, which now contains two elements — a reference to node a as well as a reference to node c—and we’ll visit the node that is currently on top of the stack. In 
 the process, we’ll set its parent pointer to the vertex that we just came from: node a.

![image](https://github.com/user-attachments/assets/ba01d24a-efa0-4596-b4fb-f3893f178aae)

- Now that we’ve visited node c, there’s only one thing left to do: lather, rinse, and repeat! Okay, okay — you can skip the first two. Really all we need to do here is just repeat the 
 process (suds optional, obviously).

- For example, since we can choose any node that is reachable from node c, we could choose node d as the next node we visit. We’ll add it to the top of the stack, mark it as “visited”, and 
 set its parent pointer.

- From node d, we’ll visit node e: add it to the stack, mark as “visited”, and finally, set its parent pointer to the node we just came from: node d.

- But now we have a problem: we can’t repeat this process because there’s simply nowhere to go from node e!

- We’ve gone as deep as we can down this particular path from the node that we started with, and we’ve hit a dead end; that is to say, we’ve reached a node with no reachable vertices!

- Given our conundrum, let’s pause for a moment and take a look at our stack of “visited” nodes, which has the following nodes on it: e, d, c, and a, in that order, from the top of the 
 stack to the bottom. Since there is nowhere to go from node e, we effectively have no other node to visit, which means that we have no other node to add to the top of the stack. At least, 
 given where we currently are, at node e. But, node d, the second element in the stack might have somewhere to go, right?

- And this is exactly where the backtracking and the idea of “breadcrumbs” comes into play — not to mention recursion! When we’ve gone as deep as possible down the graph, we can backtrack 
 one step (one vertex) at a time, and check to see if there are any other paths that we could possibly take.

- So, since we can’t search through any paths from vertex e (since none exist), we’ll pop vertex e off of the top of the stack once we’re finished with it. This leaves node d at the top of 
 the stack, so we’ll repeat the same process again — that is to say, we’ll check to see if any of node d's neighbors can be visited and if there is a path down the graph from that node.

![image](https://github.com/user-attachments/assets/41314bd3-e08d-4a84-bfc1-d848c9bbe91e)

- Once we backtrack from node e to d, we’ll notice that there’s only one direction for us to go; there is only one node to check, which is node f. We’ll add it to the top of the stack, 
 mark it as visited, and check to see if it has any children that we an visit.

- We’ll notice that, after we backtracked and changed which node we were checking, looking at, or “visiting”, the top of the stack changed. We popped off some nodes, and added on others, 
 but the main parent node remained the same. We repeated the same steps again and again, with each node that was added to the top of the stack — and those steps were the same things we 
 checked for the parent node, vertex a, when we added it to the stack when we first started out! This is recursion coming into play.

![image](https://github.com/user-attachments/assets/3731d5b1-073d-4994-a94b-9558c546f868)


