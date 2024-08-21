class Employee:
    def __init__(self, name, hours_worked, hourly_rate):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
    
    def calculate_pay(self):
        overtime_hours = max(0, self.hours_worked - 40)
        regular_hours = self.hours_worked - overtime_hours
        regular_pay = regular_hours * self.hourly_rate
        overtime_pay = overtime_hours * self.hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay
        return total_pay

class Manager(Employee):
    def __init__(self, name, hours_worked, hourly_rate, bonus):
        super().__init__(name, hours_worked, hourly_rate)
        self.bonus = bonus
    
    def calculate_pay(self):
        total_pay = super().calculate_pay() + self.bonus
        return total_pay

name = input("Enter the employee's name: ")
hours_worked = float(input(f"Enter the number of hours {name} worked: "))
hourly_rate = float(input(f"Enter the hourly rate for {name}: "))

employee = Employee(name, hours_worked, hourly_rate)
employee_pay = employee.calculate_pay()
print(f"Total pay for {employee.name}: ${employee_pay:.2f}")

name = input("\nEnter the manager's name: ")
hours_worked = float(input(f"Enter the number of hours {name} worked: "))
hourly_rate = float(input(f"Enter the hourly rate for {name}: "))
bonus = float(input(f"Enter the bonus for {name}: "))

manager = Manager(name, hours_worked, hourly_rate, bonus)
manager_pay = manager.calculate_pay()
print(f"Total pay for {manager.name}: ${manager_pay:.2f}")
