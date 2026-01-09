# include <stdio.h> 
# include <stdlib.h> 
 
typedef struct BST { 
   int data; 
   struct BST *left, *right; 
}node; 
 
void insert(node *, node *); 
void inorder(node *); 
void preorder(node *); 
void postorder(node *); 
node *search(node *, int, node **); 
 
void main() 
{ 
   int choice; 
   char ans = 'N'; 
   int key,i,n; 
   node *New,*root,*temp,*parent; 
   node *get_node(); 
   root=NULL; 
   printf("\nProgram For Binary Search Tree "); 
   do 
{ 
      printf("\n1.Create"); 
      printf("\n2.Search"); 
      printf("\n3.Recursive Traversals"); 
      printf("\n4. Display"); 
      printf("\n5.Exit"); 
      printf("\nEnter your choice :"); 
      scanf("%d",&choice); 
switch (choice) 
 { 
      case 1: 
  printf("\n How many elements you want to enter"); 
  scanf("%d",&n); 
  for(i=1;i<=n;i++) 
  { 
  New=get_node(); 
  printf("\nEnter The Element "); 
  scanf("%d",&New->data); 
  if(root==NULL) /* Tree is not Created */ 
  root=New; 
     else 
     { 
       insert(root,New); 
        } 
       // printf("\nWant To enter More Elements?(y/n)"); 
 
     }//ans = getch(); 
   break; 
      case 2: 
  printf("\nEnter Element to be searched :"); 
  scanf("%d", &key); 
  temp=search(root,key,&parent); 
  printf("\nParent of node %d is %d",temp->data,parent->data); 
  break; 
      case 3: 
  if (root == NULL) 
     printf("Tree Is Not Created"); 
  else { 
     printf("\nThe Inorder display : "); 
     inorder(root); 
     printf("\nThe Preorder display : "); 
     preorder(root); 
     printf("\nThe Postorder display : "); 
     postorder(root); 
  } 
  break; 
      case 4:if(root==NULL) 
      printf("\n Tree is not created"); 
      else 
      { 
      printf("\n The tree is;"); 
      inorder(root); 
      } 
      break; 
      } 
   } while (choice!=5); 
} 
/* 
 Get new Node 
 */ 
node *get_node() 
{ 
   node *temp; 
   temp=(node *) malloc(sizeof(node)); 
   temp->left=NULL; 
   temp->right=NULL; 
   return temp; 
} 
/* 
 This function is for creating a binary search tree 
 */ 
void insert(node *root,node *New) 
{ 
if (New->data < root->data) 
{ 
     if (root->left == NULL) 
  root->left = New; 
      else 
  insert(root->left,New); 
   } 
   if (New->data > root->data) 
   { 
      if (root->right==NULL) 
  root->right = New; 
      else 
  insert(root->right,New); 
   } 
} 
/* 
 This function is for searching the node from 
 binary Search Tree 
 */ 
node *search(node *root,int key,node **parent) 
{ 
   node *temp; 
   temp=root; 
   while(temp!=NULL) 
    { 
      if(temp->data==key) 
      { 
  printf("\nThe %d Element is Present", temp->data); 
  return temp; 
      } 
      *parent=temp; 
      if(temp->data>key) 
  temp=temp->left; 
      else 
  temp = temp->right; 
   } 
   return NULL; 
} 
/* 
 This function displays the tree in inorder fashion 
 */ 
void inorder(node *temp) 
{ 
   if (temp != NULL) { 
      inorder(temp->left); 
      printf("%d  ", temp->data); 
      inorder(temp->right); 
   } 
} 
/* 
 This function displays the tree in preorder fashion 
 */ 
void preorder(node *temp) { 
   if (temp != NULL) { 
      printf("%d  ", temp->data); 
      preorder(temp->left); 
preorder(temp->right); 
} 
} 
/* 
This function displays the tree in postorder fashion 
*/ 
void postorder(node *temp) { 
if (temp != NULL) { 
postorder(temp->left); 
postorder(temp->right); 
printf("%d  ", temp->data); 
} 
} 