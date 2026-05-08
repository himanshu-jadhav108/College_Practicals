// practical 02

import java.util.ArrayList;
import java.util.Scanner;

class Product {

    int id;
    String name;
    double price;
    int quantity;

    Product() {
        id = 0;
        name = "Unknown";
        price = 0;
        quantity = 0;
    }

    Product(int id, String name, double price, int quantity) {

        this.id = id;
        this.name = name;
        this.price = price;
        this.quantity = quantity;
    }

    double calculateTotal() {
        return price * quantity;
    }

    void display() {
        System.out.println(
            id + " " + name + " " +
            price + " " + quantity + " " + 
            calculateTotal()
        );
    }
}

public class Ecommerce {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        ArrayList<Product> products = new ArrayList<>();

        System.out.print("Enter number of Products: ");
        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {

            System.out.println("\nEnter Product Details\n");

            System.out.print("ENter Id: ");
            int id = sc.nextInt();
            
            sc.nextLine();

            System.out.print("Enter Name: ");
            String name = sc.nextLine();

            System.out.print("Enter Price: ");
            double price = sc.nextDouble();

            System.out.print("Enter Quantity: ");
            int quantity = sc.nextInt();

            Product p = new Product(id, name, price, quantity);

            products.add(p);
        }

        double grandTotal = 0;

        System.out.println("\n=== Invoice ===\n");

        System.out.println("ID  Name  Price  Qty  Total");

        for (Product p : products) {

            p.display();

            grandTotal += p.calculateTotal();
        }

        double discount = 0;

        if (grandTotal > 5000) {
            discount = grandTotal * 0.10;
        }

        double finalAmount = grandTotal - discount;

        System.out.println("\nGrand Total = "+ grandTotal);
        System.out.println("Discount = "+ discount);
        System.out.println("Final Amount = " + finalAmount);

        sc.close();
    }
    
}
