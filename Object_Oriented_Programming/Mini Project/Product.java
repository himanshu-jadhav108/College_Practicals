/**
 * Entity class representing a single Product in the inventory.
 * Demonstrates Encapsulation and Data Hiding.
 */
public class Product {
    private String productId;
    private String productName;
    private int quantity;
    private double unitCost;
    private double unitPrice;
    private double totalRevenue;
    private double totalCostIncurred;

    public Product(String productId, String productName, int quantity, double unitCost, double unitPrice) {
        this.productId = productId;
        this.productName = productName;
        this.quantity = quantity;
        this.unitCost = unitCost;
        this.unitPrice = unitPrice;
        this.totalCostIncurred = quantity * unitCost;
        this.totalRevenue = 0;
    }

    // Getters
    public String getProductId() { return productId; }
    public String getProductName() { return productName; }
    public int getQuantity() { return quantity; }
    public double getTotalRevenue() { return totalRevenue; }
    public double getTotalCostIncurred() { return totalCostIncurred; }

    // Business Logic Methods
    public void addStock(int amount) {
        if(amount > 0) {
            this.quantity += amount;
            this.totalCostIncurred += (amount * unitCost);
            System.out.println("Stock updated successfully.");
        }
    }

    public boolean removeStock(int amount) {
        if (amount <= this.quantity) {
            this.quantity -= amount;
            this.totalRevenue += (amount * unitPrice);
            return true;
        }
        return false;
    }

    @Override
    public String toString() {
        return String.format("ID: %-5s | Name: %-15s | Stock: %-5d | Price: $%.2f", 
                productId, productName, quantity, unitPrice);
    }
}