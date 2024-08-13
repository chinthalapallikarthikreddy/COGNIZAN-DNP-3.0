# sales_report.py

def generate_report(sales):
    total_sales = 0
    print("Sales Report:")
    for sale in sales:
        if sale > 500:
            print(f"Sale: ${sale:.2f} - Highlighted")
        else:
            print(f"Sale: ${sale:.2f}")
        total_sales += sale
    return total_sales

sales = []

n = int(input("Enter the number of sales records: "))

for _ in range(n):
    sale = float(input("Enter the sale amount: "))
    sales.append(sale)

total_sales = generate_report(sales)

print(f"Total sales for the month: ${total_sales:.2f}")
