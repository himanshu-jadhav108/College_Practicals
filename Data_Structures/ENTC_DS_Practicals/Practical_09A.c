#include <stdio.h> 
#include <stdlib.h>
#include <conio.h> 
#define MAXSIZE  5 
struct stack 
{      
int data; 
struct stack *prev; 
}*top=NULL; 
/* Function declaration/Prototype*/ 
void push();    
void pop();   
void main() 
{ 
int choice; 
// clrscr(); 
top = NULL;    
while (1) { 
/* Structure definition for stack */ 
/* Put data in Stack Array. data is kept on top */ 
/* Take data out from Stack Array */ 
/* Initialize TOP of stack to NULL */ 
printf ("Select stack operation \n Enter 1. PUSH 2. POP 3. EXIT \n"); 
scanf ("%d", &choice); 
switch (choice) 
{ 
case 1: 
push(); 
break; 
case 2: 
pop(); 
break; 
case 3: 
return; 
} 
} 
} 
/*Function to add an element to the stack*/ 
void push() 
{ 
struct stack *temp,*q; 
temp = (struct stack *) malloc(sizeof(struct stack)); 
printf("Enter the data to put in stack \n"); 
scanf("%d", &temp->data); /* top is a pointer, hence -> operator is used */ 
temp->prev = top; 
top = temp; 
if(top==NULL) 
     { 
     printf("\nList is Empty"); 
     } 
     q=top; 
     printf("\n"); 
     while(q->prev !=NULL)// 
     { 
     printf("%d\n",q->data); 
     q=q->prev; 
     } 
     printf("%d\n",q->data); 
return; 
} 
 
/*Function to delete an element from the stack*/ 
void pop() 
{ 
struct stack *temp; 
if (top == NULL) 
{ 
printf ("Stack is Empty\n"); 
return; 
}  
else 
{ 
printf ("poped element is = %d\n", top->data); 
temp = top->prev; 
free(top); 
top = temp; 
} 
return; 
}