#include <stdio.h> 
#include <stdlib.h> 
 
#define MAX 10 
 
int adj[MAX][MAX];   // adjacency matrix 
int visited[MAX]; 
int queue[MAX]; 
int front = -1, rear = -1; 
int n;               // number of vertices 
 
// Function to create adjacency matrix 
void createGraph() { 
    int i, j; 
    printf("Enter number of vertices: "); 
    scanf("%d", &n); 
 
    printf("\nEnter adjacency matrix (%d x %d):\n", n, n); 
    for (i = 0; i < n; i++) { 
        for (j = 0; j < n; j++) { 
            scanf("%d", &adj[i][j]); 
        } 
    } 
} 
 
// Function to perform BFS traversal 
void BFS(int start) { 
    int i; 
    if (start < 0 || start >= n) { 
        printf("Invalid starting vertex!\n"); 
        return; 
    }

    for (i = 0; i < n; i++) 
        visited[i] = 0;
    front = 0;
    rear = -1;

    queue[++rear] = start;
    visited[start] = 1;

    printf("\nBFS Traversal starting from vertex %d: ", start);

    while (front <= rear) {
        int current = queue[front++];  // dequeue
        printf("%d ", current);

        for (i = 0; i < n; i++) {
            if (adj[current][i] == 1 && visited[i] == 0) {
                queue[++rear] = i;  // enqueue
                visited[i] = 1;
            }
        }
    }
    printf("\n");
} 
 
// Function to perform DFS traversal (recursive) 
void DFS(int start) { 
    int i; 
    printf("%d ", start); 
    visited[start] = 1; 
 
    for (i = 0; i < n; i++) { 
        if (adj[start][i] == 1 && visited[i] == 0) 
            DFS(i); 
    } 
} 
 
// Main function 
int main() { 
    int start, choice; 
 
    createGraph(); 
 
    while (1) { 
        printf("\n--- Graph Traversal Menu ---\n"); 
        printf("1. Display Adjacency Matrix\n"); 
        printf("2. Breadth First Search (BFS)\n"); 
        printf("3. Depth First Search (DFS)\n"); 
        printf("4. Exit\n"); 
        printf("Enter your choice: "); 
        scanf("%d", &choice); 
 
        switch (choice) { 
            case 1: 
                printf("\nAdjacency Matrix:\n"); 
                for (int i = 0; i < n; i++) { 
                    for (int j = 0; j < n; j++) 
                        printf("%d ", adj[i][j]); 
                    printf("\n"); 
                } 
                break; 
 
            case 2: 
                printf("Enter starting vertex (0 to %d): ", n - 1); 
                scanf("%d", &start); 
                BFS(start); 
                break; 
 
            case 3: 
                printf("Enter starting vertex (0 to %d): ", n - 1); 
                scanf("%d", &start); 
                for (int i = 0; i < n; i++) 
                    visited[i] = 0; 
                printf("\nDFS Traversal starting from vertex %d: ", start); 
                DFS(start); 
                printf("\n"); 
                break; 
 
            case 4: 
                printf("Exiting...\n"); 
                exit(0); 
 
            default: 
                printf("Invalid choice! Try again.\n"); 
        } 
    } 
 
    return 0; 
}