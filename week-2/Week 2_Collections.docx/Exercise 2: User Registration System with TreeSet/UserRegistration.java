import java.util.TreeSet;

public class UserRegistration {
    private TreeSet<String> users;

    public UserRegistration() {
        users = new TreeSet<>();
    }

    // Method to register a user
    public boolean registerUser(String userName) {
        return users.add(userName);
    }

    // Method to remove a user
    public boolean removeUser(String userName) {
        return users.remove(userName);
    }

    // Method to display all users
    public void displayUsers() {
        if (users.isEmpty()) {
            System.out.println("No registered users.");
        } else {
            System.out.println("Registered Users:");
            for (String user : users) {
                System.out.println(user);
            }
        }
    }
}
