package Object_Oriented_Programming;

// Practical 01

import java.util.Scanner;
import java.util.InputMismatchException;

public class Calculator {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean continueCalc = true;

        System.out.println("=== Java Calculator ===");

        while (continueCalc) {
            try {
                double num1 = readNumber(sc, "Enter first number: ");
                char operator = readOperator(sc);
                double num2 = readNumber(sc, "Enter second number: ");

                double result = calculate(num1, num2, operator);
                System.out.printf("Result: %.2f%n", result);

            } catch (ArithmeticException | IllegalArgumentException e) {
                System.out.println("Error: " + e.getMessage());
            }

            System.out.print("Continue? (y/n): ");
            continueCalc = sc.next().trim().equalsIgnoreCase("y");
        }

        sc.close();
        System.out.println("Calculator closed.");
    }

    private static double readNumber(Scanner sc, String message) {
        while (true) {
            try {
                System.out.print(message);
                return sc.nextDouble();
            } catch (InputMismatchException e) {
                System.out.println("Invalid number. Try again.");
                sc.next(); // clear buffer
            }
        }
    }

    private static char readOperator(Scanner sc) {
        while (true) {
            System.out.print("Enter operator (+, -, *, /, %): ");
            char op = sc.next().charAt(0);
            if ("+-*/%".indexOf(op) != -1) {
                return op;
            }
            System.out.println("Invalid operator. Try again.");
        }
    }

    private static double calculate(double a, double b, char op) {
        switch (op) {
            case '+': return a + b;
            case '-': return a - b;
            case '*': return a * b;
            case '/':
                if (b == 0) throw new ArithmeticException("Division by zero!");
                return a / b;
            case '%':
                if (b == 0) throw new ArithmeticException("Modulo by zero!");
                return a % b;
            default:
                throw new IllegalArgumentException("Unexpected operator.");
        }
    }
}
