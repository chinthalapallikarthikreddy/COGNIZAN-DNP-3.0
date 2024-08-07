import java.util.Scanner;

public class BookCollectionTest {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        BookCollection collection = new BookCollection();

        while (true) {
            System.out.println("\nChoose an option:");
            System.out.println("1. Add a book");
            System.out.println("2. Remove a book");
            System.out.println("3. Display all books");
            System.out.println("4. Exit");

            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline

            switch (choice) {
                case 1:
                    System.out.print("Enter the name of the book to add: ");
                    String addBook = scanner.nextLine();
                    collection.addBook(addBook);
                    break;
                
                case 2:
                    System.out.print("Enter the name of the book to remove: ");
                    String removeBook = scanner.nextLine();
                    collection.removeBook(removeBook);
                    break;
                
                case 3:
                    System.out.println("Current book collection:");
                    collection.displayBooks();
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
