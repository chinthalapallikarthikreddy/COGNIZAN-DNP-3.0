public class EmployeeManagementTest {
    public static void main(String[] args) {
        EmployeeManagement employeeManagement = new EmployeeManagement();

        // Add employees
        Employee emp1 = new Employee(1, "Alice Smith", "123 Main St");
        Employee emp2 = new Employee(2, "Bob Johnson", "456 Elm St");
        Employee emp3 = new Employee(3, "Charlie Brown", "789 Oak St");
        employeeManagement.addEmployee(emp1);
        employeeManagement.addEmployee(emp2);
        employeeManagement.addEmployee(emp3);

        // Display employees
        employeeManagement.displayEmployees();

        // Update an employee's address
        employeeManagement.updateEmployee(2, "123 Elm St");

        // Display employees
        employeeManagement.displayEmployees();

        // Remove an employee
        employeeManagement.removeEmployee(1);

        // Display employees
        employeeManagement.displayEmployees();
    }
}
