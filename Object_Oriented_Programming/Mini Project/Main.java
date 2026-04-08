import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Inventory shopInventory = new Inventory();
        Scanner sc = new Scanner(System.in);
        
        // Initializing dummy data
        shopInventory.addProduct(new Product("P01", "Laptop", 10, 500, 750));
        shopInventory.addProduct(new Product("P02", "Mouse", 50, 10, 25));

        while (true) {
            System.out.println("\n===== INVENTORY MANAGEMENT SYSTEM =====");
            System.out.println("1. View All Products");
            System.out.println("2. Purchase Stock (Restock)");
            System.out.println("3. Ship Product (Sale)");
            System.out.println("4. Check Profit/Loss");
            System.out.println("5. Exit");
            System.out.print("Enter Choice: ");
            
            int choice = sc.nextInt();
            sc.nextLine(); // consume newline

            switch (choice) {
                case 1:
                    shopInventory.showAllProducts();
                    break;
                case 2:
                    System.out.print("Enter Product ID: ");
                    String pid = sc.nextLine();
                    Product p = shopInventory.findProduct(pid);
                    if (p != null) {
                        System.out.print("Enter quantity to purchase: ");
                        int qty = sc.nextInt();
                        p.addStock(qty);
                    } else System.out.println("Product not found!");
                    break;
                case 3:
                    System.out.print("Enter Product ID: ");
                    String sid = sc.nextLine();
                    Product sp = shopInventory.findProduct(sid);
                    if (sp != null) {
                        System.out.print("Enter quantity to ship: ");
                        int sqty = sc.nextInt();
                        if (sp.removeStock(sqty)) System.out.println("Shipment successful!");
                        else System.out.println("Insufficient stock!");
                    } else System.out.println("Product not found!");
                    break;
                case 4:
                    shopInventory.calculateFinancials();
                    break;
                case 5:
                    System.out.println("Exiting System...");
                    System.exit(0);
                default:
                    System.out.println("Invalid Choice!");
            }
        }
    }
}