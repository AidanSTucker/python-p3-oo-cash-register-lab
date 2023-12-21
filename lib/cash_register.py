class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction = 0

    def add_item(self, item_name, price, quantity=1):
        self.total += price * quantity
        self.last_transaction = price * quantity
        for _ in range(quantity):
            self.items.append(item_name)

    def void_last_transaction(self):
        if self.last_transaction != 0:
            self.total -= self.last_transaction
            self.items = self.items[:-1]  # Remove the last item from the list
            self.last_transaction = 0

    def apply_discount(self):
        if self.discount != 0:
            discount_amount = (self.discount / 100.0) * self.total
            self.total -= discount_amount
            return f"After the discount, the total comes to ${self.total:.2f}.\n"
        else:
            return "There is no discount to apply.\n"

    def get_total(self):
        return self.total

    def get_items(self):
        return self.items
