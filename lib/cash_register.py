#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.transactions = []

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        self.transactions.append((item, price, quantity))
        self.items.extend([item] * quantity)

    def apply_discount(self):
        if self.discount:
            discount_amount = (self.total * self.discount) / 100
            self.total -= discount_amount
            self.total = round(self.total, 2)  # Ensure the total is rounded to 2 decimal places
            # Formatting the output to match the test case exactly
            if self.total.is_integer():
                print(f"After the discount, the total comes to ${int(self.total)}.")
            else:
                print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.transactions:
            item, price, quantity = self.transactions.pop()
            self.total -= price * quantity
            for _ in range(quantity):
                self.items.remove(item)
        else:
            return "No transactions to void."
pass
