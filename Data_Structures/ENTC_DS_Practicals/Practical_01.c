#include <stdio.h> 
#include <string.h> 
 
#define MAX 100  // Maximum number of students 
 
// Structure to store student details 
struct Student { 
    int rollno; 
    char name[50]; 
    char programCode[10]; 
    float marks[5]; 
    float total; 
    float average; 
}; 
 
void createDatabase(struct Student s[], int *n); 
void displayDatabase(struct Student s[], int n); 
void searchStudent(struct Student s[], int n, int roll); 
void sortDatabase(struct Student s[], int n); 
 
int main() { 
    struct Student students[MAX]; 
    int n = 0, choice, roll; 
 
    while (1) { 
        printf("\n===== STUDENT DATABASE MANAGEMENT SYSTEM =====\n"); 
        printf("1. Create Database\n"); 
        printf("2. Display Database\n"); 
        printf("3. Search Student (by Roll Number)\n"); 
        printf("4. Sort Database (by Roll Number)\n"); 
        printf("5. Exit\n"); 
        printf("Enter your choice: "); 
        scanf("%d", &choice); 
 
        switch (choice) { 
            case 1: 
                createDatabase(students, &n); 
                break; 
            case 2: 
                displayDatabase(students, n); 
                break; 
            case 3: 
                printf("Enter roll number to search: "); 
                scanf("%d", &roll); 
                searchStudent(students, n, roll); 
                break; 
            case 4: 
                sortDatabase(students, n); 
                printf("Database sorted successfully!\n"); 
                break; 
            case 5: 
                printf("Exiting program... Thank you!\n"); 
                return 0; 
            default: 
                printf("Invalid choice! Please try again.\n"); 
        } 
    } 
    return 0; 
} 
 
// Function to create student database 
void createDatabase(struct Student s[], int *n) { 
    int i, j, numSubjects; 
 
    printf("Enter number of students: "); 
    scanf("%d", n); 
    printf("Enter number of subjects for each student (max 5): "); 
    scanf("%d", &numSubjects); 
 
    for (i = 0; i < *n; i++) { 
        s[i].total = 0; 
        printf("\nEnter details of student %d\n", i + 1); 
        printf("Roll Number: "); 
        scanf("%d", &s[i].rollno); 
        printf("Name: "); 
        scanf(" %[^\n]", s[i].name); // reads string with spaces 
        printf("Program Code: "); 
        scanf("%s", s[i].programCode); 
 
        printf("Enter marks in %d subjects:\n", numSubjects); 
        for (j = 0; j < numSubjects; j++) { 
            printf("Subject %d: ", j + 1); 
            scanf("%f", &s[i].marks[j]); 
            s[i].total += s[i].marks[j]; 
        } 
        s[i].average = s[i].total / numSubjects; 
    } 
} 
 
// Function to display all student records 
void displayDatabase(struct Student s[], int n) { 
    int i, j; 
    if (n == 0) { 
        printf("No records found. Please create database first.\n"); 
        return; 
    } 
 
    printf("\n%-10s %-20s %-10s %-10s %-10s\n", "Roll No", "Name", "ProgCode", "Total", 
"Average"); 
    printf("--------------------------------------------------------------\n"); 
    for (i = 0; i < n; i++) { 
        printf("%-10d %-20s %-10s %-10.2f %-10.2f\n",  
                s[i].rollno, s[i].name, s[i].programCode, s[i].total, s[i].average); 
    } 
} 
 
// Function to search a student by roll number 
void searchStudent(struct Student s[], int n, int roll) { 
    int i, found = 0; 
    for (i = 0; i < n; i++) { 
        if (s[i].rollno == roll) { 
            printf("\nStudent found!\n"); 
            printf("Roll No: %d\n", s[i].rollno); 
            printf("Name: %s\n", s[i].name); 
            printf("Program Code: %s\n", s[i].programCode); 
            printf("Total Marks: %.2f\n", s[i].total); 
            printf("Average Marks: %.2f\n", s[i].average); 
            found = 1; 
            break; 
        } 
    } 
    if (!found) 
        printf("Student with Roll No %d not found.\n", roll); 
} 
 
// Function to sort the database by roll number (ascending) 
void sortDatabase(struct Student s[], int n) { 
    int i, j; 
    struct Student temp; 
 
    for (i = 0; i < n - 1; i++) { 
        for (j = i + 1; j < n; j++) { 
            if (s[i].rollno > s[j].rollno) { 
                temp = s[i]; 
                s[i] = s[j]; 
                s[j] = temp; 
            } 
        } 
    } 
} 