#include <stdio.h> 
#include <string.h> 
 
#define MAX 50 
 
// Function for Sequential Search 
int sequentialSearch(char contacts[][50], int n, char key[]) { 
    for (int i = 0; i < n; i++) { 
        if (strcmp(contacts[i], key) == 0) 
            return i; // Found 
    } 
    return -1; // Not found 
} 
 
// Function for Binary Search (on sorted contacts) 
int binarySearch(char contacts[][50], int n, char key[]) { 
    int low = 0, high = n - 1, mid; 
    while (low <= high) { 
        mid = (low + high) / 2; 
        int cmp = strcmp(contacts[mid], key); 
        if (cmp == 0) 
            return mid; // Found 
        else if (cmp > 0) 
            high = mid - 1; 
        else 
            low = mid + 1; 
    } 
    return -1; // Not found 
} 
 
// Function to sort contacts alphabetically 
void sortContacts(char contacts[][50], int n) { 
    char temp[50]; 
    for (int i = 0; i < n - 1; i++) { 
        for (int j = i + 1; j < n; j++) { 
            if (strcmp(contacts[i], contacts[j]) > 0) { 
                strcpy(temp, contacts[i]); 
                strcpy(contacts[i], contacts[j]); 
                strcpy(contacts[j], temp); 
            } 
        } 
    } 
} 
 
int main() { 
    char contacts[MAX][50], key[50]; 
    int n, choice, pos; 
 
    printf("Enter number of contacts: "); 
    scanf("%d", &n); 
 
    printf("Enter contact names:\n"); 
    for (int i = 0; i < n; i++) { 
        printf("Contact %d: ", i + 1); 
        scanf("%s", contacts[i]); 
    } 
 
    while (1) { 
        printf("\n--- Contact Manager Search Menu ---\n"); 
        printf("1. Sequential Search\n"); 
        printf("2. Binary Search\n"); 
        printf("3. Display Contact List\n"); 
        printf("4. Exit\n"); 
        printf("Enter your choice: "); 
        scanf("%d", &choice); 
 
        switch (choice) { 
            case 1: 
                printf("Enter name to search: "); 
                scanf("%s", key); 
                pos = sequentialSearch(contacts, n, key); 
                if (pos == -1) 
                    printf("Contact not found (Sequential Search)\n"); 
                else 
                    printf("Contact '%s' found at position %d (Sequential Search)\n", key, pos + 1); 
                break; 
 
            case 2: 
                sortContacts(contacts, n); 
                printf("Enter name to search: "); 
                scanf("%s", key); 
                pos = binarySearch(contacts, n, key); 
                if (pos == -1) 
                    printf("Contact not found (Binary Search)\n"); 
                else 
                    printf("Contact '%s' found at position %d (Binary Search)\n", key, pos + 1); 
                break; 
 
            case 3: 
                printf("\nContact List:\n"); 
                for (int i = 0; i < n; i++) 
                    printf("%d. %s\n", i + 1, contacts[i]); 
                break; 
 
            case 4: 
                printf("Exiting program...\n"); 
                return 0; 
 
            default: 
                printf("Invalid choice! Try again.\n"); 
        } 
    } 
 
    return 0; 
}