#include<stdio.h> 
#include<stdlib.h> 
struct node 
{ 
int data; 
struct node *link; 
}*start=NULL; 
void create(void); 
void add_beg(void); 
void add_end(void); 
void add_middle(void); 
void search(void); 
void display(void); 
void del_first(void); 
void del_middle(void); 
void del_last(void); 
void main() 
{ 
int ch; 
while(1) 
{ 
printf("\n 1. Create list"); 
printf("\n 2. Add node at begining"); 
printf("\n 3. Add node at last"); 
printf("\n 4. Insert node at between"); 
printf("\n 5. Search node"); 
printf("\n 6. Display list"); 
printf("\n 7. Delete first node"); 
printf("\n 8. Delete last node"); 
printf("\n 9. Delete middle node"); 
printf("\n 10. Exit"); 
printf("\n Enter ur choice:"); 
scanf("%d",&ch); 
switch(ch) 
{ 
case 1: create(); 
break; 
case 2: 
case 3: 
case 4: 
case 5: 
case 6: 
case 7: 
case 8: 
add_beg(); 
break; 
add_end(); 
break; 
add_middle(); 
break; 
search(); 
break; 
display(); 
break; 
del_first(); 
break; 
del_last(); 
break; 
case 9: del_middle(); 
 break; 
case 10: 
 exit(0); 
 break; 
default: 
 printf("\n Wrong choice"); 
 break; 
 } 
 } 
 } 
 
void create(void) 
{ 
  int i,n; 
  printf("\nEnter how many nodes you want to create"); 
  scanf("%d",&n); 
  for(i=0;i<n;i++) 
    { 
      struct node *tmp,*q; 
      tmp=(struct node *)malloc(sizeof(struct node)); 
      printf("\nEnter data"); 
      scanf("%d",&tmp->data); 
      tmp->link=NULL; 
      if(start==NULL) 
 start=tmp; 
      else 
       { 
       q=start; 
       while(q->link !=NULL) 
   { 
   q=q->link; 
   } 
   q->link=tmp; 
 } 
      } 
    } 
  void display(void) 
   { 
     struct node *tmp,*q; 
     if(start==NULL) 
     { 
     printf("\nList is Empty"); 
     } 
     q=start; 
     printf("\n"); 
     while(q->link !=NULL) 
     { 
     printf("%d\t",q->data); 
     q=q->link; 
     } 
     printf("%d\t",q->data); 
   } 
  void add_beg(void) 
  { 
     struct node *tmp,*q; 
     tmp=(struct node *)malloc(sizeof(struct node)); 
     printf("\nEnter data:"); 
     scanf("%d",&tmp->data); 
     tmp->link=NULL; 
     if(start==NULL) 
     { 
       start=tmp; 
     } 
     else 
     { 
      q=start; 
      while(q->link != NULL) 
      { 
  q=q->link; 
      } 
      q->link=tmp; 
      tmp->link=NULL; 
      display(); 
  } 
 } 
  void add_end(void) 
  { 
  struct node *tmp,*q; 
  tmp=(struct node *)malloc(sizeof(struct node)); 
  printf("\n Enter data"); 
  scanf("%d",&tmp->data); 
  tmp->link=NULL; 
  if(start==NULL) 
  { 
  start=tmp; 
  } 
  else 
  { 
  q=start; 
  while(q->link != NULL) 
     { 
     q=q->link; 
     } 
     q->link=tmp; 
     tmp->link=NULL; 
     display(); 
 } 
 } 
  void add_middle(void) 
  { 
  struct node *tmp,*q; 
  int i,pos; 
  display(); 
  tmp=(struct node *)malloc(sizeof(struct node)); 
  printf("\nEnter Data"); 
  scanf("%d",&tmp->data); 
  printf("\nEnter possition:"); 
  scanf("%d",&pos); 
  q=start; 
  for(i=1;i<pos;i++) 
  { 
    q=q->link; 
    if(q==NULL) 
    { 
      printf("\nLess elements in list..."); 
      return; 
    } 
  } 
  tmp->link=q->link; 
  q->link=tmp; 
  display(); 
  } 
void search(void) 
  { 
    struct node *q; 
      int num; 
      int position=1; 
      printf("\nEnter element to be searched:"); 
       scanf("%d",&num); 
       if(start==NULL) 
  printf("\nEnter element to be searched:"); 
  else 
  { 
    q=start; 
   while(q->link != NULL) 
   { 
     if(q->data==num) 
     { 
       printf("\n Item found at possition%d",position++); 
       return; 
       } 
   q=q->link; 
   position++; 
   } 
   } 
       } 
  void del_first(void) 
  { 
    struct node *q; 
    q=start; 
    start=q->link; 
    free(q); 
    display(); 
  } 
void del_last(void) 
 { 
   struct node *tmp,*q; 
   if(start==NULL) 
    printf("\nList is Empty"); 
   else 
   { 
   q=start; 
   while(q->link->link != NULL) 
   { 
    q=q->link; 
   } 
   tmp=q->link; 
    free(tmp); 
    q->link=NULL; 
    } 
 display(); 
 } 
 
 void del_middle(void) 
  { 
   struct node *tmp,*q; 
   int num,i; 
   printf("\nEnter no want to delete"); 
   scanf("%d",&num); 
   q=start; 
   while(q->link->link != NULL) 
   { 
     if(q->link->data==num) 
     { 
     tmp=q->link; 
     q->link=tmp->link; 
     free(tmp); 
     } 
     else 
   q=q->link; 
   } 
     display(); 
 } 
