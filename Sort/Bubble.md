# Bubble Sort
![image](https://github.com/user-attachments/assets/a6e88f76-ebe8-468b-a046-d791ef9010cf)


### Bubble Sort
```c
#include <stdio.h>

// Function to perform Bubble Sort on an array
void bubbleSort(int arr[], int n) {
    int i, j, temp;
    
    // Outer loop: runs n-1 times
    for (i = 0; i < n-1; i++) {
        // Inner loop: compare adjacent elements
        for (j = 0; j < n-i-1; j++) {
            // If the current element is greater than the next, swap them
            if (arr[j] > arr[j+1]) {
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

// Function to print the elements of an array
void printArray(int arr[], int size) {
    int i;
    // Loop through the array and print each element
    for (i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n"); // Print a new line after printing all elements
}

// Main function to test the bubbleSort function
int main() {
    // Define an array of integers
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    // Calculate the number of elements in the array
    int n = sizeof(arr)/sizeof(arr[0]);
    
    // Print the unsorted array
    printf("Unsorted array: \n");
    printArray(arr, n);
    
    // Call the bubbleSort function to sort the array
    bubbleSort(arr, n);
    
    // Print the sorted array
    printf("Sorted array: \n");
    printArray(arr, n);
    
    return 0; // Return 0 to indicate successful execution
}
```
