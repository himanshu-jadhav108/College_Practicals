package practical_07;

// Abstract Class Declaration
abstract class Animal {
    // Abstract Methd
    public abstract void makeSound();

    // Concrete Method
    public void sleep() {
        System.out.println("Zzz");
    }
}

// Subclass (Inherits from Animal)
class Dog extends Animal {
    // Implementing the abstract method
    @Override
    public void makeSound() {
        System.out.println("The dog says: Woof Woof");
    }
}

// Main Class
public class Main {
    public static void main(String[] args) {
        // Object Creation
        Dog myDog = new Dog();

        // Calling the methods
        myDog.makeSound();

        // Calling the concrete method from the abstract class
        myDog.sleep();
    }
}
