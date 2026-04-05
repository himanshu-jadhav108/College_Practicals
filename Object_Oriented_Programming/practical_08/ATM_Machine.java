package practical_08;

import java.util.Scanner;
import java.util.InputMismatchException;

public class ATM_Machine {
    private static double balance = 1000.00;
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        boolean continueRunning = true;

        System.out.println("Welcome to the ATM Machine!");

        while (continueRunning) {
            displayMenu();
            try {
                System.out.print("Choose an option: ");
                int choice = getUserChoice();

                switch (choice) {
                    case 1:
                        checkBalance();
                        break;
                    case 2:
                        depositMoney();
                        break;
                    case 3:
                        withdrawMoney();
                        break;
                    case 4:
                        continueRunning = false;
                        System.out.println("Thank You For Using The ATM. GoodBye!");
                        break;
                    default:
                        throw new IllegalAccessError("Invalid Menu Option Selected. Please Choose 1-4.");         
                }
            } catch (InputMismatchException e) {
                System.out.println("Error: Invalid Input. Please ENter A Valid Number (1-4).");
                scanner.next();
            } catch (IllegalArgumentException | ArithmeticException e) {
                System.out.println("Error: " + e.getMessage());
            } finally {
                System.out.println("\n--- Operation Attempt Completed ---\n");
            }
        }
        scanner.close(); 
    }

    private static void displayMenu() {
        System.out.println("\nSelect an operation: ");
        System.out.println("1. Check Balance");
        System.out.println("2. Deposit Money");
        System.out.println("3. Withdraw Money");
        System.out.println("4. Exit");
    }

    private static int getUserChoice() throws InputMismatchException {
        return scanner.nextInt();
    }

    private static void checkBalance() {
        System.out.printf("Current Balance: Rs.%.2f\n", balance);
    }

    private static void depositMoney() {
        System.out.print("ENter Amount To Deposit: Rs.");
        try {
            double amount = scanner.nextDouble();
            if (amount <= 0) {
                throw new IllegalArgumentException("Deposit Amount Must Be Greater Than Zero.");
            }
            balance += amount;
            System.out.printf("Successfully deposited Rs.%.2f. New Balance: Rs.%.2f\n", amount, balance);
        } catch (InputMismatchException e) {
            System.out.println("Error: Invalid Input. Please Enter A Valid Number.");
            scanner.next();
        }
    }

    private static void withdrawMoney() {
        System.out.print("Enter Amount To Withdraw: Rs.");
        try {
            double amount = scanner.nextDouble();
            if (amount <= 0) {
                throw new IllegalArgumentException("Withdrawal Amount Must Be Greater Than Zero.");
            }
            if (amount > balance) {
                throw new ArithmeticException("Insufficient Funds. Cannot Withdraw More Than Current Balance.");
            }
            balance -= amount;
            System.out.printf("Successfully withdrew Rs.%.2f. New Balance: Rs.%.2f\n", amount, balance);
        } catch (InputMismatchException e) {
            System.out.println("Error: Invalid Input. Please Enter A Valid Number.");
            scanner.next();
        }
    }
}
