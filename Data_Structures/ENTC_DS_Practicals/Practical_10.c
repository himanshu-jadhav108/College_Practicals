#include <stdio.h> 
#include <stdlib.h> 
 
// Structure for a node 
struct node { 
    int data; 
    struct node *left, *right; 
}; 
 
// Function to create a new node 
struct node* createNode(int value)  
{ 
    struct node* newNode = (struct node*)malloc(sizeof(struct node)); 
    newNode->data = value; 
    newNode->left = newNode->right = NULL; 
    return newNode; 
} 
 
// Function to insert a node into the BST 
struct node* insert(struct node* root, int value) 
 { 
    if (root == NULL) 
        return createNode(value); 
 
    if (value < root->data) 
        root->left = insert(root->left, value); 
    else if (value > root->data) 
        root->right = insert(root->right, value); 
    return root; 
} 
 
// Function to find height of the tree 
int height(struct node* root)  
{ 
    if (root == NULL) 
        return -1; // Height of empty tree is -1 
    int leftHeight = height(root->left); 
    int rightHeight = height(root->right); 
    return 1 + (leftHeight > rightHeight ? leftHeight : rightHeight); 
} 
 
// Function to find depth of a given node 
int depth(struct node* root, int value, int level) { 
    if (root == NULL) 
        return -1; // Node not found 
 
    if (root->data == value) 
        return level; 
 
    int d = depth(root->left, value, level + 1); 
    if (d != -1) 
        return d; 
 
    return depth(root->right, value, level + 1); 
} 
 
int main() { 
    struct node* root = NULL; 
    int n, value, i, nodeValue; 
 
    printf("Enter number of nodes: "); 
    scanf("%d", &n); 
 
    printf("Enter %d values to insert into BST:\n", n); 
    for (i = 0; i < n; i++) { 
        scanf("%d", &value); 
        root = insert(root, value); 
    } 
    printf("\nHeight of the tree: %d\n", height(root)); 
    printf("Enter node value to find its depth: "); 
    scanf("%d", &nodeValue); 
    int d = depth(root, nodeValue, 0); 
    if (d != -1) 
        printf("Depth of node %d is: %d\n", nodeValue, d); 
    else 
        printf("Node not found in the tree.\n"); 
 
    return 0; 
} 