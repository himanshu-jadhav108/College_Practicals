// Practical 05

import java.util.Scanner;

class Person {

    String name;
    int age;

    Person(String name, int age) {

        this.name = name;
        this.age = age;
    }

    void displayPerson() {

        System.out.println("Name : " + name);
        System.out.println("Age  : " + age);

    }
}

class Student extends Person {

    int rollNo;
    String course;

    Student(String name, int age, int rollNo, String course) {

        super(name, age);

        this.rollNo = rollNo;
        this.course = course;
    }

    void displayStudent() {
       
        super.displayPerson();
        System.out.println("Roll No : " + rollNo);
        System.out.println("Course  : " + course);
    }
}

public class Inheritance {
    
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("ENter Name: ");
        String name = sc.nextLine();

        System.out.print("ENter Age: ");
        int age = sc.nextInt();

        System.out.print("Enter Roll No: ");
        int roll = sc.nextInt();

        sc.nextLine();

        System.out.print("Enter Course: ");
        String course = sc.nextLine();

        Student s = new Student(name, age, roll, course);

        System.out.println("\n=== STUDENT DETAILS ===\n");

        s.displayStudent();

        sc.close();
    }
}
