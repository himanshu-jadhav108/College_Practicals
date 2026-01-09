#include <stdio.h> 
 
// Function to display the array 
void display(float arr[], int n) { 
    int i; 
    for (i = 0; i < n; i++) 
        printf("%.2f ", arr[i]); 
    printf("\n"); 
} 
 
// Bubble Sort 
void bubbleSort(float arr[], int n) { 
    int i, j; 
    float temp; 
    for (i = 0; i < n - 1; i++) { 
        for (j = 0; j < n - i - 1; j++) { 
            if (arr[j] > arr[j + 1]) { 
                temp = arr[j]; 
                arr[j] = arr[j + 1]; 
                arr[j + 1] = temp; 
            } 
        } 
    } 
} 
 
// Selection Sort 
void selectionSort(float arr[], int n) { 
    int i, j, minIndex; 
    float temp; 
    for (i = 0; i < n - 1; i++) { 
        minIndex = i; 
        for (j = i + 1; j < n; j++) { 
            if (arr[j] < arr[minIndex]) 
                minIndex = j; 
        } 
        temp = arr[i]; 
        arr[i] = arr[minIndex]; 
        arr[minIndex] = temp; 
    } 
} 
 
// Insertion Sort 
void insertionSort(float arr[], int n) { 
    int i, j; 
    float key; 
    for (i = 1; i < n; i++) { 
        key = arr[i]; 
        j = i - 1; 
        while (j >= 0 && arr[j] > key) { 
            arr[j + 1] = arr[j]; 
            j--; 
        } 
        arr[j + 1] = key; 
    } 
} 
 
// Main Function 
int main() { 
    float prices[100], arr[100]; 
    int n, choice, i; 
 
    printf("Enter number of products: "); 
    scanf("%d", &n); 
 
    printf("Enter the prices of %d products:\n", n); 
    for (i = 0; i < n; i++) { 
        scanf("%f", &prices[i]); 
    } 
 
    printf("\nChoose Sorting Technique:\n"); 
    printf("1. Bubble Sort\n"); 
    printf("2. Selection Sort\n"); 
    printf("3. Insertion Sort\n"); 
    printf("Enter your choice: "); 
    scanf("%d", &choice); 
 
    // Copy prices to arr to avoid modifying original 
    for (i = 0; i < n; i++) 
        arr[i] = prices[i]; 
 
    switch (choice) { 
        case 1: 
            bubbleSort(arr, n); 
            printf("\nPrices sorted using Bubble Sort:\n"); 
            display(arr, n); 
            break; 
 
        case 2: 
            selectionSort(arr, n); 
            printf("\nPrices sorted using Selection Sort:\n"); 
            display(arr, n); 
            break; 
 
        case 3: 
            insertionSort(arr, n); 
            printf("\nPrices sorted using Insertion Sort:\n"); 
            display(arr, n); 
            break; 
 
        default: 
            printf("\nInvalid choice! Please select between 1–3.\n"); 
    } 
 
    return 0; 
}