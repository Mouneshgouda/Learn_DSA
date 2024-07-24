# Merge Sort

#### Merge Sort’s Divide and Conquer Algorithm Design
- Divide and conquer is a popular algorithm design technique where a huge or cumbersome problem is broken down into simpler, solvable subproblems. The solutions of 
 the subproblems are combined to solve the original problem.

- Let us see how this logic is applied in Merge Sort!

![image](https://github.com/user-attachments/assets/8640e936-f26f-4d50-8a06-f1d2e3b36102)

- You would have come across Merge Sort examples in the following way:
```c
Mergesort (A[0..n-1])
//Input: An array A[0..n-1]
//Output: Array A[0..n-1] sorted in increasing order

//If the array contains just one element, or if it is empty, it is already sorted
If n < 2
	return
else
    //copy first half of the array A to an array B
    copy A[0..floor(n/2) - 1] to B[0..floor(n/2) - 1] 
    //copy second half of the array A to an array C
    copy A[floor(n/2)..n - 1] to C[0..floor(n/2) - 1]
    //recursively divide array B until base case is reached 
    Mergesort(B[0..floor(n/2) - 1)
    //recursively divide array C until base case is reached
    Mergesort(C[0..floor(n/2) - 1)
    //Merge sorted arrays B and C back into A 
    Merge (B,C,A)
```

- In Merge Sort, you must keep splitting the array until you reach the base case. That is, until you have only one item. One item is considered to be a sorted 
 array.

- An empty array also falls under the base case. It is sorted.

### Recursion
- Merge Sort has a recursive function that splits the array recursively until the base case is reached.

### Merge subroutine
- It also has a merge subroutine that compares each element in two arrays, at every level of division, sorts, and then merges them.

- Notice the operation ‘floor’ in the pseudocode. This is to make sure that Merge Sort works for an odd number of input sizes as well. (Ex: floor(5.4) = 5)

![image](https://github.com/user-attachments/assets/1349428f-886f-460b-8d12-442d29914dbc)

![image](https://github.com/user-attachments/assets/56d84a87-60e6-4b47-a1e9-f40771399b94)

![image](https://github.com/user-attachments/assets/47e403e2-bf98-4265-b4da-0efaa0a03793)

![image](https://github.com/user-attachments/assets/eedc386e-5778-4b6d-a521-79430259bd87)

![image](https://github.com/user-attachments/assets/83b86e33-4059-46a9-9ae1-27dd5521adea)

![image](https://github.com/user-attachments/assets/b79b4848-69a2-4346-9695-9ed329676fe2)

![image](https://github.com/user-attachments/assets/6d639f72-42a1-4b49-b566-5bb301e430aa)

### Time Complexity Analysis of Merge Sort
- How does Merge Sort have Θ(n*logn) time complexity?

- Firstly, Merge Sort makes n - 1 comparisons during sorting. For example, consider two arrays
```c
[1, 3] and [2, 4]

Compare 1 with 2. 1 < 2, hence 1 is added into the array.

Compare 3 with 2. 2 < 3, hence 2 is added into the array.

Compare 3 with 4. 3 < 4, hence 3 is added into the array.

4 is the only element left, it is added into the array.

Now, you  have n - 1 comparisons.

Consider an input of size n = 8
```

![image](https://github.com/user-attachments/assets/aa9a702c-9472-48ea-95fb-d9cb0f7e840a)

```c
The figure above demonstrates that for an input size of 8, three levels of division are needed. Thus the number of levels of division is log2(8) = 3

Writing log as a function of n, we get log2(n).

For n = 2k if you keep dividing further, at each level, you can generalize the above calculations as  ∑  2k[n/2k-1] with lower bound as k = 0 and upper bound as log(n) - 1

It results in  Θ(n*logn)

Worst case: Assume for the sake of simplicity, that n is a power of 2. Let C(n) be the number of key comparisons made. The equation below defines the amount of work that needs to be done to divide and merge the arrays.

C(n) = 2C(n/2) + Cmerge  (n)

C(n/2) is the number of comparisons at each left and right split.

C(1) = 0 (For just one element no comparisons are made)

Cmerge  (n) represents the number of comparisons made while merging.

At each step, exactly one comparison is made, after which, the total number of elements in the two arrays still needed to be compared is reduced by one.

In the worst case, neither of the two arrays becomes empty, before the other one contains just one element.

Hence, for the worst case, Cmerge  (n) is n - 1

An example of an array that would be the worst case scenario for Merge Sort is [1, 9, 5, 13, 3, 11, 7, 15]..

Cworst(n) = 2Cworst(n/2) + n - 1

Using master’s theorem, you can conclude that

Cworst(n) = nlog2n + n - 1

Best case: In the best case scenario, the array is already sorted, but we still have to split and recombine it back.
```


![image](https://github.com/user-attachments/assets/e0e45c82-ba2c-4fb9-810b-97ebc12717e9)


![image](https://github.com/user-attachments/assets/4c035c5c-03f0-4531-9e72-e31b72d5abef)

![image](https://github.com/user-attachments/assets/d4e9470d-6f28-4285-b84b-8437638bb497)

- Here's a simple way to visualize Merge Sort:

- Divide: Split your array of data in half, again and again, until each piece can't be divided further (you'll end up with arrays of just one element).
- Conquer: Now, with each piece being sorted (since it's just one element), you start combining them.
- Merge: As you combine these pieces, you sort them along the way. Think of merging two small stacks of cards where each stack is already in order.

- This process continues until all the small, sorted pieces are merged back into a single, sorted array.


### Algorithm
- Step 1: Create two pointers, one for each sorted half.

- Step 2: Initialize an empty temporary array to hold the merged result.

- Step 3: Compare the elements at the pointers of the two halves:

- Copy the smaller element into the temporary array.

- Move the pointer of the sublist with the smaller element forward.

- Step 4: Repeat step 3 until one of the sublists is empty.

- Step 5: Copy the remaining elements from the non-empty sublist to the temporary array.

- Step 6: Copy the elements back from the temporary array to the original list.


![image](https://github.com/user-attachments/assets/8b2c71c2-8c60-4f44-94f1-ed5e27dacdef)


