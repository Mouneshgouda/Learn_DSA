![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/d4ba7f31-68fd-410d-b69c-454e775c3000)

🔰 Hello Everyone....In This Article we will See How the Data and the Variables with Two Different Approach are stored in RAM when we Compile & Run The Code.
🔰 We will Learn about what is Static Memory & Heap Memory and How the Memory is allocated in Each of the Part.
🔰 For Implementation of This Practical we will use Visual Studio Code which you can Open by Clicking Here
🔰 Let's Begin.

✅ Types of Memory Allocations : 
- 🔹 We have Two Types of Memory Allocations :
Static Memory Allocation
Dynamic Memory Allocation
- 🔹 Let's First Look at Static Memory Allocation. 
---------------------------------------------------------------------------------------------------------------
✅ Static Memory Allocations : 
- 🔹 In Simple Words Take Static as Constant i.e it Can't be Change once Declared/Allocated. So, The Memory which is Allocated to the RAM when we Compile the Code 
  is Known as Static Memory.
- 🔹 In Stack Memory, You have to Enter and Delete Elements From the Top of the Stack which is also known as LIFO (Last In First Out).
- 🔹 So when we Allocate Data in Static Memory, It is Fixed and can not be Increased or Decreased During The Run Time of Code
- 🔹 For Example : 
![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/e3989ea8-9dd8-42fe-969f-ec53accdb12d)

- 🔹 In the Above, as you can see the array size is fixed and we can't enter more than 5 elements otherwise it will give error During Compile Time.
- 🔹 Since we have an Idea about how Static Memory Allocation Works, Let's Look at the Drawbacks for This.
---------------------------------------------------------------------------------------------------------------
### ✅ Problem's in Static Memory Allocations : 
- 🔹 When you Declare any Variable with fixed Size, Obviously we can't Increase the Size of Respective During Run Time which is the 1st Drawback.
- 🔹 The Second Drawback is If the Values Stored in The Array are less than the Size Specified to the Respective array. Then it will be Pure Wastage of memory - 
  Example : If Your array Size is for 5 elements & You Store only 4 elements, then 1 memory space will be wasted. 
- 🔹 Similarly If the Values Stored in The Array are more than the Size Specified to the Respective array. Then the Program may misbehave.
---------------------------------------------------------------------------------------------------------------
- 🔰 So This is all about Static Memory Allocation but, Looking at these Drawbacks we need someone to Rescue and here the Dynamic Memory Allocation Some's into 
 Use.
- 🔰 So Let us Now Discuss more about Dynamic Memory Allocation.
---------------------------------------------------------------------------------------------------------------
### ✅ Dynamic Memory Allocations : 
- 🔹To Opposite of Static Memory Allocation, The Process in which we allocate the Memory During Run Time/Execution of Program is known as Dynamic Memory 
 Allocation. So we have the flexibility to Allocate Memory according to the Needs.
- 🔹 Here the Memory is Allocated in The Heap Memory of the RAM :

- 🔹 In this Rough RAM Diagram, you can see the Heap Memory where the Dynamic Memory Allocation Takes Place.
- 🔹 In Stack Memory, we can't allocate or Remove the Data once Assigned to the RAM, In Heap Memory we can Randomly Access the Data & Do the Operation as per our 
 needs.
- ![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/40aaba9e-0a71-4125-accb-e637aa353ec7)

- 🔹 In Stack as we know everything is Well Ordered and well Defined, The allocation & Deallocation takes place in Defined Order Only. So in Heap we Don't have 
 such restrictions since the allocation/Deallocation can be done without any Order. 
- 🔹 But what is the Way through which we can Specify How much memory we want to Allocate ?...For This, these are some Built-in Functions That can help to do this 
 during Run Time. & to use these Function, Pointers Play a very Import Role in Dynamic Memory Allocation.
---------------------------------------------------------------------------------------------------------------
### ✅ Role of Pointers (*) in Dynamic Memory Allocations : 
- 🔹 When we Allocate Memory Dynamically, The only way through which we can access this memory is through Pointers. The Pointer will Point to the memory Address 
 of First byte of the Memory which we allocate.
- 🔹 Refer the Image Below to see the use case of Pointers :
![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/b05a0ffd-dc4a-4130-be2e-bbc403959e7a)

### ✅ Built-in Functions for Dynamic Memory Allocations : 
- 🔹 As The Process in which we allocate the Memory During Run Time/Execution of Program is known as Dynamic Memory Allocation. For this Process, 
- 🔹 The Functions are :
- 1.malloc()
- 2.calloc()
- 3.realloc()
- 4.free()

# 🔹 Let's Start with malloc().
---------------------------------------------------------------------------------------------------------------
### ✅ Malloc() Function : 
- 🔹 Malloc Stands For Memory Allocation and we know Memory Allocations are of two Types, Static and Dynamic and the memory is allocated in the Stack and Heap 
 Memory of the RAM Respectively.
- 🔹 This malloc() Function is Declared in Standard Library which is knows/used in program by,
 syntax : #include <stdlib.h>
 - 🔹 The malloc() Function takes one argument which is the Size of Memory to be Allocated.
 ![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/6921e18a-b6dc-4412-8678-6f022401e72c)

- 🔹 Suppose we give 10 bytes of Memory Space, Then this will allocate 10 bytes of memory in HEAP and will Return the Base Address to the Pointer. and This Base 
 address (pointer) points to the First Byte in The Memory Allocated.

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/b9dec398-c1ca-46b5-99ce-56b2f74c54c2)
