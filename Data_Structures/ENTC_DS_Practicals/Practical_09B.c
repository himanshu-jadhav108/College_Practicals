#include<stdio.h> 
#include<conio.h> 
#include<stdlib.h> 
 
struct Node 
 { 
 int Data; 
 struct Node* next; 
 }*rear, *front; 
 
void delQueue() 
{ 
       struct Node *temp, *var=rear; 
      if(var==rear) 
      { 
      rear = rear->next; 
      free(var); 
      } 
      else 
      printf("\nQueue Empty"); 
} 
 
 
void push(int value) 
{ 
     struct Node *temp; 
     temp=(struct Node *)malloc(sizeof(struct Node)); 
     temp->Data=value; 
     if (front == NULL) 
     { 
    front=temp; 
    front->next=NULL; 
    rear=front; 
     } 
     else 
     { 
    front->next=temp; 
    front=temp; 
    front->next=NULL; 
     } 
} 
 
 
void display() 
{ 
     struct Node *var=rear; 
     if(var!=NULL) 
     { 
    printf("\nElements are as:  "); 
    while(var!=NULL) 
    { 
  printf("\t%d",var->Data); 
  var=var->next; 
    } 
     printf("\n"); 
     } 
     else 
     printf("\nQueue is Empty"); 
} 
 
 
int main() 
{ 
     int i=0; 
     front=NULL; 
     printf(" \n1. Push to Queue"); 
     printf(" \n2. Pop from Queue"); 
     printf(" \n3. Display Data of Queue"); 
     printf(" \n4. Exit\n"); 
     while(1) 
     { 
   printf(" \nChoose Option: "); 
   scanf("%d",&i); 
   switch(i) 
   { 
  case 1: 
  { 
       int value; 
       printf("\nEnter a value  to push into Queue: "); 
       scanf("%d",&value); 
       push(value); 
       display(); 
       break; 
  } 
  case 2: 
  { 
       delQueue(); 
       display(); 
       break; 
  } 
  case 3: 
  { 
       display(); 
       break; 
  } 
  case 4: 
  { 
       exit(0); 
  } 
  default: 
  { 
       printf("\nwrong choice for operation"); 
  } 
   } 
     } 
} 