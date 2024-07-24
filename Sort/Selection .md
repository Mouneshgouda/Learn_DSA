# Selection Sort
![image](https://github.com/user-attachments/assets/092d4f7d-2d3a-4105-85c0-faec33464a8a)


## What is Selection Sort?
- Selection sort, also known as in-place comparison sort, is a simple sorting algorithm. It works on the idea of repeatedly finding the smallest element and 
 placing it at its correct sorted position.

- Selection sort works by dividing the list into two sublists:

- 1.Sorted sublist – that is built on the left end of the list from left to right.
- 2.Unsorted sublist – that is the rest of the unsorted list, on the right end.

## Flowchart of the Selection Sort
- A flowchart for the Selection Sort algorithm could be described as follows:

- 1.Start: Begin the process.
- 2.Input List: Obtain the list or array to be sorted.
- 3.Initialize: Set the current index as the starting index. This represents the beginning of the unsorted portion of the list.
- 4.Find Minimum: Traverse the rest of the unsorted portion to find the smallest element.
- 5.Swap: Swap the smallest element found with the element at the current index.
- 6.Increment Index: Increase the current index by one, moving the boundary of the sorted and unsorted portions of the list.
- 7.Check: Check if the current index is less than the length of the list - 1. If it is, go back to the "Find Minimum" step. If it's not, all elements have been 
 sorted.
- 8.End: End the process. The list is now sorted in ascending order.
  
 ![image](https://github.com/user-attachments/assets/3137ddfd-13a2-48e8-94fe-212dbfddeba4)


 ![image](https://github.com/user-attachments/assets/10d36253-a74c-49c3-bd0b-f6180fdddc31)

```c
#include <stdio.h>

// Function to perform Selection Sort on an array
void selectionSort(int arr[], int n) {
    int i, j, minIndex, temp;

    // Outer loop: iterate over each element of the array
    for (i = 0; i < n-1; i++) {
        // Assume the current element is the minimum
        minIndex = i;

        // Inner loop: find the smallest element in the remaining unsorted array
        for (j = i+1; j < n; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;  // Update minIndex if a smaller element is found
            }
        }

        // Swap the found minimum element with the first element of the unsorted part
        temp = arr[minIndex];
        arr[minIndex] = arr[i];
        arr[i] = temp;
    }
}

// Function to print the elements of an array
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

// Main function to test the selectionSort function
int main() {
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr)/sizeof(arr[0]);

    printf("Unsorted array: \n");
    printArray(arr, n);

    selectionSort(arr, n);

    printf("Sorted array: \n");
    printArray(arr, n);

    return 0;
}
```
