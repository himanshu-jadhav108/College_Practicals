import java.sql.*;
import java.util.InputMismatchException;
import java.util.Scanner;

public class Main {
	// Change according to your database
	static final String URL = "jdbc:mysql://localhost:3306/studentdb";
	static final String USER = "root";
	static final String PASSWORD = "password";

	public static Connection getConnection() throws SQLException {
		return DriverManager.getConnection(URL, USER, PASSWORD);
	}

	private static void printSqlError(SQLException e) {
		System.out.println("Database error: " + e.getMessage());
		System.out.println("SQLState: " + e.getSQLState() + ", ErrorCode: " + e.getErrorCode());
	}

	// CREATE
	public static void addStudent(Scanner sc) {
		String sql = "INSERT INTO students (name, course, marks) VALUES (?, ?, ?)";
		try (Connection con = getConnection(); PreparedStatement ps = con.prepareStatement(sql)) {
			con.setAutoCommit(false);

			System.out.print("Enter Name: ");
			sc.nextLine();
			String name = sc.nextLine();

			System.out.print("Enter Course: ");
			String course = sc.nextLine();

			System.out.print("Enter Marks: ");
			double marks = sc.nextDouble();

			if (marks < 0 || marks > 100) {
				System.out.println("Marks must be between 0 and 100.");
				con.rollback();
				return;
			}

			ps.setString(1, name);
			ps.setString(2, course);
			ps.setDouble(3, marks);
			ps.executeUpdate();

			con.commit();
			System.out.println("Student added successfully.");
		} catch (InputMismatchException e) {
			System.out.println("Invalid input. Marks must be numeric.");
			sc.nextLine();
		} catch (SQLException e) {
			printSqlError(e);
		}
	}

	// READ
	public static void viewStudents() {
		String sql = "SELECT id, name, course, marks FROM students ORDER BY id";
		try (Connection con = getConnection();
			 PreparedStatement ps = con.prepareStatement(sql);
			 ResultSet rs = ps.executeQuery()) {

			System.out.println("\nStudent Records");
			while (rs.next()) {
				System.out.println(
					rs.getInt("id") + " | " +
					rs.getString("name") + " | " +
					rs.getString("course") + " | " +
					rs.getDouble("marks")
				);
			}
		} catch (SQLException e) {
			printSqlError(e);
		}
	}

	// UPDATE
	public static void updateStudent(Scanner sc) {
		String sql = "UPDATE students SET marks = ? WHERE id = ?";
		try (Connection con = getConnection(); PreparedStatement ps = con.prepareStatement(sql)) {
			con.setAutoCommit(false);

			System.out.print("Enter Student ID: ");
			int id = sc.nextInt();

			System.out.print("Enter New Marks: ");
			double marks = sc.nextDouble();

			if (marks < 0 || marks > 100) {
				System.out.println("Marks must be between 0 and 100.");
				con.rollback();
				return;
			}

			ps.setDouble(1, marks);
			ps.setInt(2, id);

			int rows = ps.executeUpdate();
			if (rows > 0) {
				con.commit();
				System.out.println("Student updated successfully.");
			} else {
				con.rollback();
				System.out.println("Student not found.");
			}
		} catch (InputMismatchException e) {
			System.out.println("Invalid input. Use numeric values for ID and marks.");
			sc.nextLine();
		} catch (SQLException e) {
			printSqlError(e);
		}
	}

	// DELETE
	public static void deleteStudent(Scanner sc) {
		String sql = "DELETE FROM students WHERE id = ?";
		try (Connection con = getConnection(); PreparedStatement ps = con.prepareStatement(sql)) {
			con.setAutoCommit(false);

			System.out.print("Enter Student ID: ");
			int id = sc.nextInt();

			ps.setInt(1, id);
			int rows = ps.executeUpdate();
			if (rows > 0) {
				con.commit();
				System.out.println("Student deleted successfully.");
			} else {
				con.rollback();
				System.out.println("Student not found.");
			}
		} catch (InputMismatchException e) {
			System.out.println("Invalid input. Student ID must be numeric.");
			sc.nextLine();
		} catch (SQLException e) {
			printSqlError(e);
		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int choice = 0;

		do {
			System.out.println("\n===== STUDENT MANAGEMENT =====");
			System.out.println("1. Add Student");
			System.out.println("2. View Students");
			System.out.println("3. Update Student");
			System.out.println("4. Delete Student");
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
					addStudent(sc);
					break;
				case 2:
					viewStudents();
					break;
				case 3:
					updateStudent(sc);
					break;
				case 4:
					deleteStudent(sc);
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
