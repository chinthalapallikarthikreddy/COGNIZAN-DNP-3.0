# order_processing.py


def apply_discount(order_amount):
    if order_amount > 100:
        discount = order_amount * 0.10  # 10% discount
        order_amount -= discount  # Apply the discount
    return order_amount

order_amount = 150  # Example order amount

final_price = apply_discount(order_amount)


print(f"Final price after discount: ${final_price:.2f}")
