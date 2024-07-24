# Insertion Sort 
```c
#include <stdio.h>

// Function to perform Insertion Sort on an array
void insertionSort(int arr[], int n) {
    int i, key, j;

    // Iterate from the second element to the last element
    for (i = 1; i < n; i++) {
        key = arr[i];  // The element to be inserted into the sorted part of the array
        j = i - 1;

        // Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;  // Place the key in its correct position
    }
}

// Function to print the elements of an array
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

// Main function to test the insertionSort function
int main() {
    int arr[] = {12, 11, 13, 5, 6};
    int n = sizeof(arr)/sizeof(arr[0]);

    printf("Unsorted array: \n");
    printArray(arr, n);

    insertionSort(arr, n);

```
