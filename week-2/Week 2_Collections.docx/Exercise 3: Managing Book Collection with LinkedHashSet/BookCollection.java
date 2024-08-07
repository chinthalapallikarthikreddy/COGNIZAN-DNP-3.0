import java.util.LinkedHashSet;
import java.util.Set;

public class BookCollection {
    private Set<String> books;

    public BookCollection() {
        books = new LinkedHashSet<>();
    }

    // Method to add a book to the collection
    public boolean addBook(String bookTitle) {
        return books.add(bookTitle);
    }

    // Method to remove a book from the collection
    public boolean removeBook(String bookTitle) {
        return books.remove(bookTitle);
    }

    // Method to display all books in the collection
    public void displayBooks() {
        if (books.isEmpty()) {
            System.out.println("The book collection is empty.");
        } else {
            System.out.println("Book Collection:");
            for (String book : books) {
                System.out.println(book);
            }
        }
    }
}
