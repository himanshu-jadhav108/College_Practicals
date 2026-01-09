#include <stdio.h> 
 
int main() { 
    int i, j, k, space; 
    int n = 4;  // You can change n if needed 
 
    // 1. Right-angled triangle with numbers 
    printf("Pattern 1: Right-angled Triangle with Numbers\n"); 
    for (i = 1; i <= n; i++) { 
        for (j = 1; j <= i; j++) { 
            printf("%d", j); 
        } 
        printf("\n"); 
    } 
 
    printf("\n"); 
 
    // 2. Diamond shape with asterisks 
    printf("Pattern 2: Diamond Shape with Asterisks\n"); 
    for (i = 1; i <= n; i++) { 
        for (space = i; space < n; space++) 
            printf(" "); 
        for (j = 1; j <= (2 * i - 1); j++) 
            printf("*"); 
        printf("\n"); 
    } 
    for (i = n - 1; i >= 1; i--) { 
        for (space = n; space > i; space--) 
            printf(" "); 
        for (j = 1; j <= (2 * i - 1); j++) 
            printf("*"); 
        printf("\n"); 
    } 
 
    printf("\n"); 
 
    // 3. Pyramid with numbers 
    printf("Pattern 3: Pyramid with Numbers\n"); 
    for (i = 1; i <= n; i++) { 
        for (space = i; space < n; space++) 
            printf(" "); 
        for (j = 1; j <= (2 * i - 1); j++) 
            printf("%d", i); 
        printf("\n"); 
    } 
 
    printf("\n"); 
 
    // 4. Pyramid with alphabets 
    printf("Pattern 4: Pyramid with Alphabets\n"); 
    for (i = 1; i <= n; i++) { 
        for (space = i; space < n; space++) 
            printf(" "); 
        char ch = 'A'; 
        for (j = 1; j <= i; j++) 
            printf("%c", ch++); 
        ch -= 2; 
        for (j = 1; j < i; j++) 
            printf("%c", ch--); 
        printf("\n"); 
    } 
return 0; 
} 
