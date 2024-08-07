import java.util.ArrayList;

public class EmployeeManagement {
    // ArrayList to store Employee objects
    private ArrayList<Employee> employees;

    // Constructor
    public EmployeeManagement() {
        employees = new ArrayList<>();
    }

    // Method to add an employee to the list
    public void addEmployee(Employee employee) {
        employees.add(employee);
        System.out.println("Employee added: " + employee);
    }

    // Method to remove an employee from the list by ID
    public void removeEmployee(int employeeId) {
        Employee employeeToRemove = null;
        for (Employee employee : employees) {
            if (employee.getId() == employeeId) {
                employeeToRemove = employee;
                break;
            }
        }
        if (employeeToRemove != null) {
            employees.remove(employeeToRemove);
            System.out.println("Employee removed: " + employeeToRemove);
        } else {
            System.out.println("Employee with ID " + employeeId + " not found.");
        }
    }

    // Method to update an employee's address by ID
    public void updateEmployee(int employeeId, String newAddress) {
        for (Employee employee : employees) {
            if (employee.getId() == employeeId) {
                employee.setAddress(newAddress);
                System.out.println("Employee updated: " + employee);
                return;
            }
        }
        System.out.println("Employee with ID " + employeeId + " not found.");
    }

    // Method to display all employees in the list
    public void displayEmployees() {
        if (employees.isEmpty()) {
            System.out.println("No employees in the system.");
        } else {
            System.out.println("Employee List:");
            for (Employee employee : employees) {
                System.out.println(employee);
            }
        }
    }
}
