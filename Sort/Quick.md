# A Look at How Quicksort Works

- A Simple Look
- To start things off, imagine that we have the following unsorted collection of numbers that we would like to sort:

<img src="https://github.com/user-attachments/assets/6bbddd0c-858b-4de3-9345-356e824d4a71" alt="Description of the image">


### We want to use quicksort to sort these numbers, and this is what quicksort does:

- 1.  Picks a midpoint value called the pivot
- 2.  Re-orders items based on how large they are relative to the pivot:
- 2.1 Items smaller than the pivot are moved to the left of the pivot
- 2.2 Items larger than the pivot are moved to the right of the pivot
- 2.3 Repeats steps i and ii on the partially sorted values
- 3.  At first glance, how these three steps help us sort some data may seem bizarre, but we are going to see shortly how all of this ties together.

- Starting at the top, because this is our first step, the region of values we are looking to sort is everything. The first thing we do is pick our pivot, the value at the middle position:

<img src="https://github.com/user-attachments/assets/54b6c63e-217a-4430-8bda-730fd4e726c8" alt="Description of the image" >


- We can pick our pivot from anywhere, but all the cool kids pick (for various good reasons) the pivot from the midpoint. Since we want to be cool as well, that's what we'll do. Quicksort uses the pivot value to order items in a very crude and basic way. From quicksort's point of view, all items to the left of the pivot value should be smaller, and all items to the right of the pivot value should be larger:

<img src="https://github.com/user-attachments/assets/bd777414-00a5-4dfa-b942-e23ecfef798b" alt="Description of the image">


- This is the equivalent of throwing things over the fence to the other side where the pivot value is the fence. When we do this rearranging, this is what we will see:

<img src="https://github.com/user-attachments/assets/4565c22f-c442-42e1-bbfa-7752ffbcbab1" alt="Description of the image"  height="300">



- There are a few things to notice here. First, notice that all items to the left of the pivot are smaller than the pivot. All items to the right of the pivot are larger than the pivot. Second, these items also aren't ordered. They are just smaller or larger relative to the pivot value, but they aren't placed in any ordered fashion. Once all of the values to the left and right of the pivot have been properly placed, our pivot value is considered to be sorted. What we just did is identify a single pivot and rearrange values to the left or right of it. The end result is that we have one sorted value. There are many more values to sort, so we repeat the steps we just saw on the unsorted regions.

- At this point, we now have two sections of data on either side of our initial pivot value that are partially sorted by whether they are less than or greater than our pivot value. What we do next is repeat all of this pivot picking and rearranging on each of these two unsorted sections:

<img src="https://github.com/user-attachments/assets/45e246bc-db4f-47b9-821d-ab4f996e635c" alt="Description of the image"  height="300">


- In each unsorted section, we pick our pivot value first. This will be the value at the midpoint of the values in the section. Once we have picked our pivot, it is time to do some rearranging:

<img src="https://github.com/user-attachments/assets/bf4b4a0a-48b5-4d3b-91ed-a9e470503cde" alt="Description of the image"  height="300">



- Notice that we moved values smaller than our pivot value to the left. Values greater than our pivot were thrown over the fence to the right. We now have a few more pivot values that are in their final sorted section, and we have a few more unsorted regions that need the good old quicksort treatment applied to them. If we sped things up a bit, here is how each step will ultimately play out:

- Notice that we moved values smaller than our pivot value to the left. Values greater than our pivot were thrown over the fence to the right. We now have a few more pivot values that are in their final sorted section, and we have a few more unsorted regions that need the good old quicksort treatment applied to them. If we sped things up a bit, here is how each step will ultimately play out:

<img src="https://github.com/user-attachments/assets/9eae6a88-a5ec-4f00-a2e8-aaff86d557cd" alt="Description of the image"  height="550">


- We keep repeating all of this pivoting and sorting on each of the sections until we get to the point where we don't have enough values to pick a pivot and divide from. Once we reach that point and can divide no further, guess what? We are done! Our initial collection of unordered data is now sorted from small to large, and we can see that if we read our pivot items from left to right:

- ![image](https://github.com/user-attachments/assets/9676c79d-12fd-437b-a66b-3b480933d8cd)


### Time Complexity 


<img src="https://github.com/user-attachments/assets/cb9d7598-ba75-4c12-a74e-7ec64f1c7c1c" alt="Description of the image" height="500">

 ## Sorted Array
 
![image](https://github.com/user-attachments/assets/c7497a04-4c02-45e0-b645-4fdee53e7bf8)
