import java.util.Scanner;

class ArrayOperation {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter the size of array: ");
        int n = sc.nextInt();

        if (n <= 0) {
            System.out.println("Array Size must be Greater than 0");
            return;
        }

        int[] arr = new int[n];

        System.out.println("Enter the Elements: ");
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        System.out.print("Array Elements: ");
        for (int val : arr) {
            System.out.print(val + " ");
        }

        int sum = 0, min = arr[0], max = arr[0];

        for (int val : arr) {
            sum += val;
            if (val < min) min = val;
            if (val > max) max = val;
        }

        System.out.println("\nSum = " + sum);
        System.out.println("Average = " + (double) sum / n);
        System.out.println("Minimum = " + min);
        System.out.println("Maximum = " + max);

        System.out.print("Enter element to Search: ");
        int key = sc.nextInt();

        int index = -1;
        for (int i = 0; i < n; i++) {
            if (arr[i] == key) {
                index = i;
                break;
            }
        }

        System.out.println(
            index >= 0
                    ? "Element found at position " + (index + 1)
                    : "Element not found"
        );
        sc.close();
    }
}