#include <stdio.h> 
#define MAX 5   // Maximum number of parcels in queue 
 
int queue[MAX]; 
int front = -1, rear = -1; 
 
// Function to add parcel 
void enqueue() { 
    int item; 
    if (rear == MAX - 1) { 
        printf("\nQueue Overflow! No more parcels can be added.\n"); 
    } else { 
        printf("Enter parcel ID to add: "); 
        scanf("%d", &item); 
        if (front == -1) front = 0; 
        rear++; 
        queue[rear] = item; 
        printf("Parcel %d added successfully.\n", item); 
    } 
} 
 
// Function to delete parcel 
void dequeue() { 
    if (front == -1 || front > rear) { 
        printf("\nQueue Underflow! No parcels left to remove.\n"); 
    } else { 
        printf("Parcel %d removed successfully.\n", queue[front]); 
        front++; 
    } 
} 
 
// Function to display parcels 
void display() { 
    if (front == -1 || front > rear) { 
        printf("\nQueue is empty.\n"); 
    } else { 
        printf("\nCurrent parcels in queue:\n"); 
        for (int i = front; i <= rear; i++) { 
            printf("%d ", queue[i]); 
        } 
        printf("\n"); 
    } 
} 
 
// Main function 
int main() { 
    int choice; 
    printf("=== Parcel Handling System (Using Queue) ===\n"); 
    do { 
        printf("\n1. Add Parcel (Enqueue)"); 
        printf("\n2. Remove Parcel (Dequeue)"); 
        printf("\n3. Display Parcels"); 
        printf("\n4. Exit"); 
        printf("\nEnter your choice: "); 
        scanf("%d", &choice); 
 
        switch (choice) { 
            case 1: 
                enqueue(); 
                break; 
            case 2: 
                dequeue(); 
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

