// Practical 08

import java.util.Scanner;

class ATM {

    double balance = 10000;

    void checkBalance() {

        System.out.println("Current Balance = " + balance);
    }

    void deposit(double amount) {

        if (amount <= 0) {

            throw new IllegalArgumentException("Invalid Deposit Amount");
        }

        balance += amount;

        System.out.println("Amount Deposited Successfully");
    }

    void withdraw(double amount) {

        if (amount <= 0) {

            throw new IllegalArgumentException("Invalid Withdrawal Amount");
        }

        if (amount > balance) {

            throw new ArithmeticException("Insufficient Balance");
        }

        balance -= amount;

        System.out.println("Withdrawal Successful");
    }
}

public class ATMSimulation {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        ATM atm = new ATM();

        int choice;

        do {

            System.out.println("\n===== ATM MENU =====");

            System.out.println("1. Check Balance");
            System.out.println("2. Deposit");
            System.out.println("3. Withdraw");
            System.out.println("4. Exit");

            System.out.print("Enter choice: ");

            choice = sc.nextInt();

            try {

                switch (choice) {

                    case 1:

                        atm.checkBalance();
                        break;

                    case 2:

                        System.out.print("Enter deposit amount: ");

                        double deposit = sc.nextDouble();

                        atm.deposit(deposit);

                        break;

                    case 3:

                        System.out.print("Enter withdrawal amount: ");

                        double withdraw = sc.nextDouble();

                        atm.withdraw(withdraw);

                        break;

                    case 4:

                        System.out.println("Thank You");
                        break;

                    default:

                        System.out.println("Invalid Choice");
                }
            }

            catch (IllegalArgumentException e) {

                System.out.println("Error: " + e.getMessage());
            }

            catch (ArithmeticException e) {

                System.out.println("Error: " + e.getMessage());
            }

            catch (Exception e) {

                System.out.println("Invalid Input");
                sc.nextLine();
            }

            finally {

                System.out.println("Transaction Completed");
            }

        } while (choice != 4);

        sc.close();
    }
}