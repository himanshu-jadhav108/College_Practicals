// Practical 02

import java.util.Scanner;
import java.util.ArrayList;

class Product {
    String name;
    double price;
    int qty;

    Product() {
        name = "Book";
        price = 200;
        qty = 1;
    }

    Product(String n, double p, int q) {
        name = n;
        price = p;
        qty = q;
    }

    double totalCost() {
        return price * qty;
    }
}

public class EcommerceOrder {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Product p1 = new Product();

        System.out.print("Enter product name: ");
        String name = sc.nextLine();
    
        System.out.print("Enter Price: ");
        double price = sc.nextDouble();

        System.out.print("Enter Quantity: ");
        int qty = sc.nextInt();

        Product p2 = new Product(name, price, qty);

        double total = p1.totalCost() + p2.totalCost();
        double discount = 0;

        if (total >= 1000) {
            discount = total * 0.10;
        }
        double finalAmount = total - discount;

        System.out.println("\n-----Invoice-----");
        System.out.println("Product 1: "+ p1.name + " = Rs. " + p1.totalCost());
        System.out.println("Product 2: "+ p2.name + " = Rs. " + p2.totalCost());
        System.out.println("Total: Rs."+ total);
        System.out.println("Discount: Rs."+ discount);
        System.out.println("Payable: Rs."+ finalAmount);

        sc.close();
    }
}

