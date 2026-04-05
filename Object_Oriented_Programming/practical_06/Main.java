package practical_06;

// Interface
interface Polygon {
    void getArea(int length, int breadth);
}

// Implementing the interface
class Rectangle implements Polygon {
    public void getArea(int length, int breadth) {
        int area = length * breadth;
        System.out.println("Area of Rectangle: " + area);
    }
}

// Main Class
public class Main {
    public static void main(String[] args) {
        Rectangle rect = new Rectangle();
        rect.getArea(5, 6);
    }
}