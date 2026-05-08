// practical 04

import java.util.Scanner;

public class ArrayOperations {
    
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter size of array: ");
        int n = sc.nextInt();

        int arr[] = new int[n];

        System.out.println("Enter array elements: ");

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int choice;

        do {
            System.out.println("\n===== ARRAY MENU =====");
            System.out.println("1. Display Array");
            System.out.println("2. Find Sum and Average");
            System.out.println("3. Find Maximum");
            System.out.println("4. Find Minimum");
            System.out.println("5. Search Element");
            System.out.println("6. Exit");

            System.out.print("Enter choice: ");
            choice = sc.nextInt();

            switch (choice) {

                case 1:

                    System.out.println("Array Elements: ");

                    for (int i=0; i<n; i++) {
                        System.out.print(arr[i] + " ");
                    }

                    System.out.println();
                    break;

                case 2:

                    int sum = 0;

                    for (int i=0; i<n; i++) {
                        sum += arr[i];
                    }

                    double avg = (double) sum / n;

                    System.out.println("Sum = " + sum);
                    System.out.println("Average = "+ avg);

                    break;

                case 3:

                    int max = arr[0];

                    for (int i = 1; i < n; i++) {

                        if (arr[i] > max) {
                            max = arr[i];
                        }
                    }

                    System.out.println("Maxium = "+ max);

                    break;

                case 4:

                    int min = arr[0];

                    for (int i = 1; i < n; i++) {

                        if (arr[i] < min) {
                            min = arr[i];
                        }
                    }

                    System.out.println("Minimum = "+ min);

                    break;

                case 5:

                    System.out.print("Enter element to search: ");
                    int key = sc.nextInt();

                    boolean found = false;

                    for (int i=0; i<n; i++) {
                        if (arr[i] == key) {
                            System.out.println("Element Found at Index" + i);

                            found = true;

                            break;
                        }
                    }

                    if (!found) {
                        System.out.println("ELement Not Found");
                    }

                    break;

                case 6:

                    System.out.println("Program Ended");
                    break;

                default:
                    System.out.println("Invalid Choice");

            }
        } while (choice != 6);

        sc.close();
    }
}
