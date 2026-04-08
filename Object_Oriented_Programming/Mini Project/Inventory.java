import java.util.ArrayList;

/**
 * Controller class managing the collection of products.
 */
public class Inventory {
    private ArrayList<Product> products;

    public Inventory() {
        products = new ArrayList<>();
    }

    public void addProduct(Product p) {
        products.add(p);
    }

    public void showAllProducts() {
        System.out.println("\n--- Current Inventory Status ---");
        for (Product p : products) {
            System.out.println(p);
        }
    }

    public Product findProduct(String id) {
        for (Product p : products) {
            if (p.getProductId().equalsIgnoreCase(id)) return p;
        }
        return null;
    }

    public void calculateFinancials() {
        double grandRevenue = 0;
        double grandCost = 0;
        for (Product p : products) {
            grandRevenue += p.getTotalRevenue();
            grandCost += p.getTotalCostIncurred();
        }
        System.out.println("\n--- Financial Report ---");
        System.out.println("Total Sales Revenue: $" + grandRevenue);
        System.out.println("Total Cost Incurred: $" + grandCost);
        System.out.println("Net Profit/Loss:     $" + (grandRevenue - grandCost));
    }
}