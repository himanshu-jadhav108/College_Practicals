// Practical 01

import java.util.Scanner;

public class Calculator {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int choice;
        double a, b, result;

        do {
            System.out.println("\n=== Caluclator ===\n");
            System.out.println("1. Addition");
            System.out.println("2. Subtraction");
            System.out.println("3. Multiplication");
            System.out.println("4. Division");
            System.out.println("5. Exit");

            System.out.print("ENter Choice: ");
            choice = sc.nextInt();

            try {
                if (choice >= 1 && choice <= 4) {

                    System.out.print("Enter First number: ");
                    a = sc.nextDouble();

                    System.out.print("Enter second number: ");
                    b = sc.nextDouble();

                    switch (choice) {

                        case 1:
                            result = a + b;
                            System.out.println("Result = " + result);
                            break;

                        case 2:
                            result = a - b;
                            System.out.println("Result = " + result);
                            break;

                        case 3:
                            result = a * b;
                            System.out.println("Result = " + result);
                            break;
                        
                        case 4:
                            if (b == 0) {
                                throw new ArithmeticException("Cannot divide by zero");
                            }

                            result = a/b;
                            System.out.println("Result = " + result);
                            break;
                        
                        default:
                            System.out.println("Invalid Choice");

                    }
                }
            }

            catch (ArithmeticException e) {
                System.out.println("Error: "+ e.getMessage());
            }

            catch (Exception e) {
                System.out.println("Invalid Input");
                sc.nextLine();
            }

            finally {
                System.out.println("Operation Completed");
            }
        } while (choice != 5);

        System.out.println("Calculator Closed");
        sc.close();
    }

}