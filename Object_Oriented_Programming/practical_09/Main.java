import java.sql.*;
import java.util.InputMismatchException;
import java.util.Scanner;

public class Main {
	// Change according to your DB
	static final String URL = "jdbc:mysql://localhost:3306/testdb";
	static final String USER = "root";
	static final String PASSWORD = "password";

	public static Connection getConnection() throws SQLException {
		return DriverManager.getConnection(URL, USER, PASSWORD);
	}

	public static void addEmployee(Scanner sc) {
		String sql = "INSERT INTO employees (id, name, department, salary) VALUES (?, ?, ?, ?)";
		try (Connection con = getConnection(); PreparedStatement ps = con.prepareStatement(sql)) {
			System.out.print("Enter ID: ");
			int id = sc.nextInt();
			sc.nextLine();

			System.out.print("Enter Name: ");
			String name = sc.nextLine();

			System.out.print("Enter Department: ");
			String dept = sc.nextLine();

			System.out.print("Enter Salary: ");
			double salary = sc.nextDouble();

			ps.setInt(1, id);
			ps.setString(2, name);
			ps.setString(3, dept);
			ps.setDouble(4, salary);

			ps.executeUpdate();
			System.out.println("Employee added successfully.");
		} catch (InputMismatchException e) {
			System.out.println("Invalid input. Please enter correct data types.");
			sc.nextLine();
		} catch (SQLException e) {
			System.out.println("Database error: " + e.getMessage());
		}
	}

	public static void viewEmployees() {
		String sql = "SELECT * FROM employees";
		try (Connection con = getConnection();
			 PreparedStatement ps = con.prepareStatement(sql);
			 ResultSet rs = ps.executeQuery()) {

			System.out.println("\nEmployee Records");
			while (rs.next()) {
				System.out.println(
					rs.getInt("id") + " | " +
					rs.getString("name") + " | " +
					rs.getString("department") + " | " +
					rs.getDouble("salary")
				);
			}
		} catch (SQLException e) {
			System.out.println("Database error: " + e.getMessage());
		}
	}

	public static void updateEmployee(Scanner sc) {
		String sql = "UPDATE employees SET salary = ? WHERE id = ?";
		try (Connection con = getConnection(); PreparedStatement ps = con.prepareStatement(sql)) {
			System.out.print("Enter Employee ID: ");
			int id = sc.nextInt();

			System.out.print("Enter New Salary: ");
			double salary = sc.nextDouble();

			ps.setDouble(1, salary);
			ps.setInt(2, id);

			int rows = ps.executeUpdate();
			if (rows > 0) {
				System.out.println("Employee updated successfully.");
			} else {
				System.out.println("Employee not found.");
			}
		} catch (InputMismatchException e) {
			System.out.println("Invalid input. Please enter numeric values.");
			sc.nextLine();
		} catch (SQLException e) {
			System.out.println("Database error: " + e.getMessage());
		}
	}

	public static void deleteEmployee(Scanner sc) {
		String sql = "DELETE FROM employees WHERE id = ?";
		try (Connection con = getConnection(); PreparedStatement ps = con.prepareStatement(sql)) {
			System.out.print("Enter Employee ID: ");
			int id = sc.nextInt();

			ps.setInt(1, id);
			int rows = ps.executeUpdate();
			if (rows > 0) {
				System.out.println("Employee deleted successfully.");
			} else {
				System.out.println("Employee not found.");
			}
		} catch (InputMismatchException e) {
			System.out.println("Invalid input. Employee ID must be a number.");
			sc.nextLine();
		} catch (SQLException e) {
			System.out.println("Database error: " + e.getMessage());
		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int choice = 0;

		do {
			System.out.println("\n===== EMPLOYEE MANAGEMENT =====");
			System.out.println("1. Add Employee");
			System.out.println("2. View Employees");
			System.out.println("3. Update Employee");
			System.out.println("4. Delete Employee");
			System.out.println("5. Exit");
			System.out.print("Enter choice: ");

			try {
				choice = sc.nextInt();
			} catch (InputMismatchException e) {
				System.out.println("Invalid choice. Enter a number from 1 to 5.");
				sc.nextLine();
				continue;
			}

			switch (choice) {
				case 1:
					addEmployee(sc);
					break;
				case 2:
					viewEmployees();
					break;
				case 3:
					updateEmployee(sc);
					break;
				case 4:
					deleteEmployee(sc);
					break;
				case 5:
					System.out.println("Exiting...");
					break;
				default:
					System.out.println("Invalid choice.");
			}
		} while (choice != 5);

		sc.close();
	}
}