```c
1. What is a good code?
• A good code must be Readable & Scalable. Scalable in terms of Time/Speed & Space/Memory.

2. What is Big-O?
• Big-O allows us to give an idea of the scalability of code.
• It tells how long it takes to run an algorithm. 
• As the number of elements increases how the number of operation increases determines algorithmic efficiency.
• Big-O concerns with the number of operations taken to complete a task.

3. Time Complexities of some common siniipets:
-Big Os - https://www.bigocheatsheet.com/
• O(1) Constant- no loops - Constant time – No matter how much the number of input increases the number of operations remains the same.
• O(log N) Logarithmic- usually searching algorithms have log n if they are sorted (Binary Search) 
• O(n) Linear- for loops, while loops through n items 
• O(n log(n)) Log Linear- usually sorting operations 
• O(n^2) Quadratic- every element in a collection needs to be compared to ever other element. Two nested loops 
• O(2^n) Exponential- recursive algorithms that solves a problem of size N 
• O(n!) Factorial- you are adding a loop for every element 
• Iterating through half a collection is still O(n) 
• Two separate collections: O(a * b)
• If loops are nested we multiply the Big-O = O (n * n) = O(n^2) = Quadratic times.
• If 1 loop for each different array, then Big-O = O (a + b).
• If 2 different inputs are nested, then Big-O = O (a * b).
• If 3 different inputs are nested, then Big-O = O (a * b * c).
• If 3 same inputs are nested, then Big-O = O (n * n * n).


4. What can cause time in a function?
• Operations (+, -, *, /)
• Comparisons (, ==)
• Looping (for, while)
• Outside Function call (function())

5. Rules for calculating Time Complexity.
  a. Always consider for wrost case.
  b. Remove constants.
  c. Take care for differnt terms of inputs.
  4. Drop Non Dominants.

6. What causes Space complexity? 
• Variables
• Data Structures
• Function Call
• Allocations

7. Use of Heap & Stack
• When a program executes it has two ways to remember things - the heap and the stack.
• The heap usually where we store variables that we assign values to.
• The stack is usually where we keep track of our function calls.
• when it comes to space complexity is that when we talk about space complexity we're talking about additional space 
  so we don't include space taken up by the inputs. So we don't really care how big the input is.
```

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/7f88b311-141e-4465-a9a3-c7a994488c1f)

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/2c6b0b08-66f1-4386-af44-ec2a718cffaa)

