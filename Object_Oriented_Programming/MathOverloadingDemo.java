package Object_Oriented_Programming;

// Practical 03

public class MathOverloadingDemo {

    /* ---------- Absolute Value (Overloaded) ---------- */

    static int abs(int x) {
        return x < 0 ? -x : x;
    }
    
    static long abs(long x) {
        return x < 0 ? -x : x;
    }

    static float abs(float x) {
        return x < 0 ? -x : x;
    }

    static double abs(double x) {
        return x < 0 ? -x : x;
    }

    /* ---------- Power (Overloaded) ---------- */
    static int power(int base, int exp) {
        if (exp < 0)
            throw new IllegalArgumentException("Exponent must be non-negative for int power");

        int result = 1;
        for (int i = 0; i < exp; i++) {
            result *= base;
        }
        return result;
    }

    static double power(double base, double exp) {
        return Math.pow(base, exp);
    }
    /* ---------- Main ---------- */
    public static void main(String[] args) {

        System.out.println("abs(-5)      = " + abs(-5));
        System.out.println("abs(-10L)    = " + abs(-10L));
        System.out.println("abs(-3.5f)   = " + abs(-3.5f));
        System.out.println("abs(-7.25)   = " + abs(-7.25));

        System.out.println("power(2, 3)  = " + power(2, 3));
        System.out.println("power(2.5,2) = " + power(2.5, 2));
    }
}
