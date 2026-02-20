#include <stdio.h> 
#define MAX 5   // Maximum number of parcels (stack size) 
 
int stack[MAX]; 
int top = -1; 
 
// Function to push a parcel 
void push() { 
    int item; 
    if (top == MAX - 1) { 
        printf("\nStack Overflow! No more parcels can be added.\n"); 
    } else { 
        printf("Enter parcel ID to add: "); 
        scanf("%d", &item); 
        top++; 
        stack[top] = item; 
        printf("Parcel %d added successfully.\n", item); 
    } 
} 
 
// Function to pop a parcel 
void pop() { 
    if (top == -1) { 
        printf("\nStack Underflow! No parcels left to remove.\n"); 
    } else { 
        printf("Parcel %d removed successfully.\n", stack[top]); 
        top--; 
    } 
} 
 
// Function to display the stack 
void display() { 
    if (top == -1) { 
        printf("\nStack is empty.\n"); 
    } else { 
        printf("\nCurrent parcels in stack:\n"); 
        for (int i = top; i >= 0; i--) { 
            printf("%d\n", stack[i]); 
        } 
    } 
} 
 
// Main function 
int main() { 
    int choice; 
    printf("=== Parcel Handling System (Using Stack) ===\n"); 
    do { 
        printf("\n1. Add Parcel (Push)"); 
        printf("\n2. Remove Parcel (Pop)"); 
        printf("\n3. Display Parcels"); 
        printf("\n4. Exit"); 
        printf("\nEnter your choice: "); 
        scanf("%d", &choice); 
 
        switch (choice) { 
            case 1: 
                push(); 
                break; 
            case 2: 
                pop(); 
                break; 
            case 3: 
                display(); 
                break; 
            case 4: 
                printf("Exiting the system.\n"); 
                break; 
            default: 
                printf("Invalid choice! Please try again.\n"); 
        } 
    } while (choice != 4); 
 
    return 0; 
} 