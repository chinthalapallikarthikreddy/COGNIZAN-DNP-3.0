import java.util.Scanner;

public class UserRegistrationTest {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        UserRegistration registration = new UserRegistration();

        while (true) {
            System.out.println("\nChoose an option:");
            System.out.println("1. Register a user");
            System.out.println("2. Remove a user");
            System.out.println("3. Display all users");
            System.out.println("4. Exit");

            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline character

            switch (choice) {
                case 1:
                    System.out.print("Enter the name of the user to register: ");
                    String registerUser = scanner.nextLine();
                    registration.registerUser(registerUser);
                    break;
                
                case 2:
                    System.out.print("Enter the name of the user to remove: ");
                    String removeUser = scanner.nextLine();
                    registration.removeUser(removeUser);
                    break;
                
                case 3:
                    System.out.println("Current registered users:");
                    registration.displayUsers();
                    break;
                
                case 4:
                    System.out.println("Exiting...");
                    scanner.close();
                    return;

                default:
                    System.out.println("Invalid choice. Please enter a number between 1 and 4.");
            }
        }
    }
}
