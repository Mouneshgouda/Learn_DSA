# Union
![Uploading image.png…]()


# Union

- Unions are conceptually similar to structures in C. The syntax to declare/define a union is also similar to that of a structure. **The only differences is in terms of storage**. In structure each member has its own storage location, whereas all members of union uses a single shared memory location which is equal to the size of its largest data member


### What is the Major Difference between Structure and Union
![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/499ed234-f0bb-4154-99f3-2d35d2174a87)

## Union in C Programming
A union is a data type. C Language provides us a special type of data type called union by which it can store many types of data types in the same memory location but it has the same value in the variable of data types at the same time. But the Union can use the same memory location in many types through Union All members of the Union use only one memory location and their size can be as much as the member with the largest size.

## Defining a Union
Let's use the union keyword to define unions. This is similar to defining the structure.

**The basic syntax of Unions:-**
```c
union union_name
{
  data_type var1;
  data_type var2;
  ...
  ...
  data_type varn;
}u1.u2,….un;
```
First of all, union defines keyword and union name. Then before we define variables in curly brackets {}. Then let's create before union variables of curly brackets {}.
```
union in-put
{
  int a;
  float b;
}in;
```
Now it is of in variable input type and it can store an integer value or it can store a float value. We cannot store value in both its variables simultaneously.


## Sizeof Union
```c
#include <stdio.h>
union letter{  
int a;  
char b;  
float c;  
double d;  
};  

int main()  
{  
  printf("The size of union letter is %d", sizeof(union letter));  
  return 0;  
}
```
```c
We already know that the size of:

int data type is 4
char data type is 1
float data type is 4
double data type is 8
Since the double variable d requires the largest memory space among the four variables, a total of 8 bytes is allocated in the memory for the union letter.
```

## Accessing Union Member Variables
Union members also access the same way structure members access. First of all, we write the name of the union. Then before dot (.) An operator is written and the member's name is written. We can assign the value of union members with this type.
```
in.a = 10;
```
If we want to print this union member then we can do with these types.
printf(“%d”,in.a);

### For Example:-
```c
#include<stdio.h>

/* Declaring input union */
union input
{
  int a;
  float b;
}in; /* Union variable */
int main()
{
  in.a = 15;
  in.b = 20;
  /* Will print a garbage value */
  printf(“Value of a is : %dn”,in.a);

  /* Will print 20 */
  printf(“Value of b is : %f”,in.b);
return 0;
}
```
### Output
```
Value of a is: 1101345
Value of b is: 20.00000
```
# Example Of Union
```c

#include <stdio.h>

union Data {
   int i;
   float f;
};

int main() {
   union Data data;

   data.i = 10;
   printf("data.i : %d\n", data.i);

   data.f = 220.5;
   printf("data.f : %f\n", data.f);

   return 0;
}
```
```c
#include <stdio.h>
#include <string.h>

// Define a union to store different types of car information
union CarInfo {
    int id;
    char color[20];
    char model[20];
    char name[20];
};

int main() {
    // Create an instance of the CarInfo union
    union CarInfo carInfo;

    // Assign and access values using the union
    carInfo.id = 1;

    strcpy(carInfo.color, "Blue");

    strcpy(carInfo.model, "SUV");

    strcpy(carInfo.name, "Honda");
    
    printf("Union - ID: %d\n", carInfo.id);
    printf("Union - Color: %s\n", carInfo.color);
    printf("Union - Model: %s\n", carInfo.model);

    printf("Union - Name: %s\n", carInfo.name);

    // Note: Accessing a different member of the union will overwrite the previous value.
    // Only one member of the union can store a value at any given time.

    return 0;
}


```
- output:-
```c
Union - ID: 1684959048
Union - Color: Honda
Union - Model: Honda
Union - Name: Honda

```
		

I hope that you all liked this tutorial, if you want to read these tutorials more then stay connected with me.


Originaly posted on - [Union in C Programming](https://alimammiya.hashnode.dev/union-in-c-programming)


## Is sizeof for a struct equal to the sum of sizeof of each member?

- The sizeof for a struct is not always equal to the sum of sizeof of each individual member. This is because of the padding added by the compiler to avoid 
 alignment issues. Padding is only added when a structure member is followed by a member with a larger size or at the end of the structure.

- Different compilers might have different alignment constraints as C standards state that alignment of structure totally depends on the implementation.

- Let’s take a look at the following examples for better understanding:
```c
// C program to illustrate 
// size of struct 
#include <stdio.h> 

int main() 
{ 

	struct A { 

		// sizeof(int) = 4 
		int x; 
		// Padding of 4 bytes 

		// sizeof(double) = 8 
		double z; 

		// sizeof(short int) = 2 
		short int y; 
		// Padding of 6 bytes 
	}; 

	printf("Size of struct: %ld", sizeof(struct A)); 

	return 0; 
} 
```
```c
Size of struct: 24
```

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/ee63d966-b1e9-4541-bb41-ddaae3a47a47)

- The red portion represents the padding added for data alignment and the green portion represents the struct members. In this case, x (int) is followed by z 
 (double), which is larger in size as compared to x. Hence padding is added after x. Also, padding is needed at the end for data alignment.


```c
// C program to illustrate 
// size of struct 
#include <stdio.h> 

int main() 
{ 

	struct B { 
		// sizeof(double) = 8 
		double z; 

		// sizeof(int) = 4 
		int x; 

		// sizeof(short int) = 2 
		short int y; 
		// Padding of 2 bytes 
	}; 

	printf("Size of struct: %ld", sizeof(struct B)); 

	return 0; 
} 
```
```c
output:-
Size of struct: 16
```

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/2853ac39-614d-4962-929e-ea11f33effb5)


In this case, the members of the structure are sorted in decreasing order of their sizes. Hence padding is required only at the end.

### Case 3:
```c
// C program to illustrate 
// size of struct 
#include <stdio.h> 
  
int main() 
{ 
  
    struct C { 
        // sizeof(double) = 8 
        double z; 
  
        // sizeof(short int) = 2 
        short int y; 
        // Padding of 2 bytes 
  
        // sizeof(int) = 4 
        int x; 
    }; 
  
    printf("Size of struct: %ld", sizeof(struct C)); 
  
    return 0; 
}
```

```c
Output:-
Size of struct: 16
```
![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/ff66b681-c2ba-4717-87b7-f0c0477eadf1)

- In this case, y (short int) is followed by x (int) and hence padding is required after y. No padding is needed at the end in this case for data alignment.

- C language doesn’t allow the compilers to reorder the struct members to reduce the amount of padding. In order to minimize the amount of padding, the struct 
 members must be sorted in a descending order (similar to the case 2).
