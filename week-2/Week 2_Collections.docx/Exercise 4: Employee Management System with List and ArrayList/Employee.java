public class Employee {
    private int id;
    private String name;
    private String address;

    // Constructor
    public Employee(int id, String name, String address) {
        this.id = id;
        this.name = name;
        this.address = address;
    }

    // Getters and setters
    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    // Display employee details
    public void display() {
        System.out.println("ID: " + id + ", Name: " + name + ", Address: " + address);
    }
}
