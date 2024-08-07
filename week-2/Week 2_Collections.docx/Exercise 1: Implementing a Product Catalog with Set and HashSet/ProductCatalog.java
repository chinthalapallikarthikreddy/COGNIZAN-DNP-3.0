import java.util.HashSet;
import java.util.Set;

public class ProductCatalog {
    private Set<String> products;

    public ProductCatalog() {
        products = new HashSet<>();
    }

    // Method to add a product to the catalog
    public boolean addProduct(String productName) {
        return products.add(productName);
    }

    // Method to remove a product from the catalog
    public boolean removeProduct(String productName) {
        return products.remove(productName);
    }

    // Method to search for a product in the catalog
    public boolean searchProduct(String productName) {
        return products.contains(productName);
    }

    // Method to display all products in the catalog
    public void displayProducts() {
        if (products.isEmpty()) {
            System.out.println("The product catalog is empty.");
        } else {
            System.out.println("Product Catalog:");
            for (String product : products) {
                System.out.println(product);
            }
        }
    }
}
