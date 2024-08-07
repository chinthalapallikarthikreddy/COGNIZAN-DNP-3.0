import java.util.Scanner;

public class ProductCatalogTest {
    public static void main(String[] args) {
        ProductCatalog catalog = new ProductCatalog();
        Scanner scanner = new Scanner(System.in);
        boolean exit = false;

        while (!exit) {
            System.out.println("\nProduct Catalog Menu:");
            System.out.println("1. Add Product");
            System.out.println("2. Remove Product");
            System.out.println("3. Search Product");
            System.out.println("4. Display Products");
            System.out.println("5. Exit");
            System.out.print("Choose an option: ");
            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume the newline

            switch (choice) {
                case 1:
                    System.out.print("Enter product name to add: ");
                    String addProduct = scanner.nextLine();
                    if (catalog.addProduct(addProduct)) {
                        System.out.println("Product added successfully.");
                    } else {
                        System.out.println("Product already exists in the catalog.");
                    }
                    break;
                case 2:
                    System.out.print("Enter product name to remove: ");
                    String removeProduct = scanner.nextLine();
                    if (catalog.removeProduct(removeProduct)) {
                        System.out.println("Product removed successfully.");
                    } else {
                        System.out.println("Product not found in the catalog.");
                    }
                    break;
                case 3:
                    System.out.print("Enter product name to search: ");
                    String searchProduct = scanner.nextLine();
                    if (catalog.searchProduct(searchProduct)) {
                        System.out.println("Product found in the catalog.");
                    } else {
                        System.out.println("Product not found in the catalog.");
                    }
                    break;
                case 4:
                    catalog.displayProducts();
                    break;
                case 5:
                    exit = true;
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }

        scanner.close();
    }
}
