package practical_05;

// Superclass
class Person {
    void show() {
        System.out.println("This is a person.");
    }
}

// Subclass
class Student extends Person {
    void study() {
        System.out.println("Student is studying");
    }
}

// Main Class
public class SingleInheritance {
    public static void main(String[] args) {

        Student s = new Student();

        s.show();       // method from superclass
        s.study();      // method from subclass
    }
}
