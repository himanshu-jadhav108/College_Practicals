// Practical 07

import java.util.Scanner;

abstract class Shape {

    abstract void area();

    void message() {
        System.out.println("Area Calculation Program");

    }
}

class Circle extends Shape {

    double radius;

    Circle(double radius) {
        this.radius = radius;
    }

    void area() {

        double result = 3.14 * radius * radius;

        System.out.println("Area of Circle = " + result);
    }
}

class Rectangle extends Shape {

    double length, width;

    Rectangle(double length, double width) {

        this.length = length;
        this.width  = width;
    }

    void area() {

        double result = length * width;

        System.out.println("Area of Rectangle = " + result);
    }
}

public class Abstract {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        Shape s;

        System.out.print("Enter radius: ");
        double r = sc.nextDouble();

        s = new Circle(r);

        s.message();
        s.area();

        System.out.print("\nEnter Length: ");
        double l = sc.nextDouble();

        System.out.print("Enter width: ");
        double w = sc.nextDouble();

        s = new Rectangle(l, w);

        s.message();
        s.area();

        sc.close();
    }
    
}
