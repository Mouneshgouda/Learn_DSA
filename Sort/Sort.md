# Selection sort
- Selection sort is a sorting algorithm that selects the smallest element from an unsorted list in each iteration and places that element at the beginning of the unsorted list.

## Working of Selection Sort
- 1.Set the first element as minimum.

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/1f36a83f-4ed6-412d-8405-3965a06c6aa1)

- 2.Compare minimum with the second element. If the second element is smaller than minimum, assign the second element as minimum.

 Compare minimum with the third element. Again, if the third element is smaller, then assign minimum to the third element otherwise do nothing. The process goes on until the last element.

 ![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/9f6364e6-bf28-481e-b175-4ee6c10ba773)

- 3.After each iteration, minimum is placed in the front of the unsorted list.

  ![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/79c4568a-45cb-4dc3-b2f2-87e14102ab0e)

- 4.For each iteration, indexing starts from the first unsorted element. Step 1 to 3 are repeated until all the elements are placed at their correct positions.

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/5a658dd6-a17b-4645-af02-8bbe5f2f1620)

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/47d7ad5e-1b2d-4c15-9825-70d384f0bdda)

![image](https://github.com/Gurupatil0003/DSA_Tutorial/assets/110026505/9eaccbb4-c564-4d1c-bdcf-ce931d0d4d3a)



## Selection Sort Algorithm
```c
selectionSort(array, size)
repeat (size - 1) times
set the first unsorted element as the minimum
for each of the unsorted elements
if element < currentMinimum
set element as new minimum
swap minimum with first unsorted position
end selectionSort
```

## Selection sort in C
```c
// Selection sort in C

#include <stdio.h>

// function to swap the the position of two elements
void swap(int *a, int *b) {
int temp = *a;
*a = *b;
*b = temp;
}

void selectionSort(int array[], int size) {
for (int step = 0; step < size - 1; step++) {
int min_idx = step;
for (int i = step + 1; i < size; i++) {

// To sort in descending order, change > to < in this line.
// Select the minimum element in each loop.
if (array[i] < array[min_idx])
min_idx = i;
}

// put min at the correct position
swap(&array[min_idx], &array[step]);
}
}

// function to print an array
void printArray(int array[], int size) {
for (int i = 0; i < size; ++i) {
printf("%d  ", array[i]);
}
printf("\n");
}

// driver code
int main() {
int data[] = {20, 12, 10, 15, 2};
int size = sizeof(data) / sizeof(data[0]);
selectionSort(data, size);
printf("Sorted array in Acsending Order:\n");
printArray(data, size);
}
```
## Selection Sort Complexity

| Selection Sort Complexity | Time Complexity | Space Complexity | Stability |
|---------------------------|-----------------|------------------|-----------|
| Best                      | O(n^2)          | O(1)             | No        |
| Worst                     | O(n^2)          |                  |           |
| Average                   | O(n^2)          |                  |           |
