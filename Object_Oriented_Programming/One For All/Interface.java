// Practical 06

import java.util.Scanner;

interface Shape {

    void area();
}

class Circle implements Shape {

    double radius;

    Circle(double radius) {
        this.radius = radius;
    }

    public void area() {

        double result = 3.14 * radius * radius;

        System.out.println("Area of Circle = "+ result);
    }
}

class Rectangle implements Shape {

    double length, width;

    Rectangle(double length, double width) {
        this.length = length;
        this.width = width;
    }

    public void area() {
       
        double result = length * width;

        System.out.println("Area of the Rectangle = "+ result);
    }
}

public class Interface {
    
    public static void main(String[] args ){

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter radius of the Circle: ");
        double r = sc.nextDouble();

        Shape s1 = new Circle(r);

        s1.area();

        System.out.print("\nEnter Length Of Rectangle: ");
        double l = sc.nextDouble();

        System.out.print("Enter Width Of Rectangle: ");
        double w = sc.nextDouble();

        Shape s2 = new Rectangle(l, w);

        s2.area();

        sc.close();
    }
}
