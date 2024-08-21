from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, order_amount):
        pass

class RegularDiscount(DiscountStrategy):
    def apply_discount(self, order_amount):
        return order_amount

class PremiumDiscount(DiscountStrategy):
    def apply_discount(self, order_amount):
        return order_amount * 0.9

class VIPDiscount(DiscountStrategy):
    def apply_discount(self, order_amount):
        return order_amount * 0.8

class Order:
    def __init__(self, customer_type, order_amount):
        self.customer_type = customer_type
        self.order_amount = order_amount

    def final_price(self):
        if self.customer_type == 'regular':
            strategy = RegularDiscount()
        elif self.customer_type == 'premium':
            strategy = PremiumDiscount()
        elif self.customer_type == 'vip':
            strategy = VIPDiscount()
        else:
            raise ValueError("Unknown customer type")
        return strategy.apply_discount(self.order_amount)

customer_type = input("Enter the customer type (regular, premium, vip): ").lower()
order_amount = float(input("Enter the order amount: "))

order = Order(customer_type, order_amount)
final_price = order.final_price()
print(f"Final price after discount: ${final_price:.2f}")
