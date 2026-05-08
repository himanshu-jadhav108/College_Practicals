// practical 03

import java.util.Scanner;

class Calculator {

    static double power(int a, int b) {
        return Math.pow(a, b);
    }

    static double power(double a, double b) {
        return Math.pow(a, b);
    }

    static int absolute(int n) {
        return Math.abs(n);
    }

    static double absolute(double n) {
        return Math.abs(n);
    }
}

public class Overloading {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("=== POWER FUNCTION ===");

        System.out.print("Enter integer base: ");
        int a = sc.nextInt();

        System.out.print("Enter integer exponent: ");
        int b = sc.nextInt();

        System.out.println("Power = " + Calculator.power(a, b));

        System.out.print("\nEnter double base: ");
        double x = sc.nextDouble();

        System.out.print("Enter double exponent: ");
        double y = sc.nextDouble();

        System.out.println("Power = " + Calculator.power(x, y));

        System.out.println("\n=== ABSOLUTE FUNCTION ===");

        System.out.print("Enter integer number: ");
        int n1 = sc.nextInt();

        System.out.println("Absolute = " + Calculator.absolute(n1));

        System.out.print("\nEnter double number: ");
        double n2 = sc.nextDouble();

        System.out.println("Absolute = " + Calculator.absolute(n2));

        sc.close();
    }
    
}
