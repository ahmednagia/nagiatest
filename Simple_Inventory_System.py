class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_product_info(self):
        """Displays the product information."""
        print(f"Product: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Quantity: {self.quantity}")

    def update_quantity(self, quantity_sold):
        """Updates the quantity when products are sold or restocked."""
        if self.quantity >= quantity_sold:
            self.quantity -= quantity_sold
            print(f"Updated quantity of {self.name}: {self.quantity}")
        else:
            print(f"Not enough stock of {self.name}. Only {self.quantity} available.")

    def restock(self, quantity_added):
        """Restocks the product with additional quantity."""
        self.quantity += quantity_added
        print(f"Restocked {quantity_added} units of {self.name}. New quantity: {self.quantity}")

    def total_value(self):
        """Calculates the total value of the product (price * quantity)."""
        return self.price * self.quantity

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        """Adds a new product to the inventory."""
        self.products.append(product)
        print(f"Product {product.name} added to inventory.")

    def display_inventory(self):
        """Displays the information of all products in the inventory."""
        for product in self.products:
            product.display_product_info()
            print("-" * 30)

    def calculate_inventory_value(self):
        """Calculates the total value of all products in the inventory."""
        total = 0
        for product in self.products:
            total += product.total_value()
        return total

def main():
    # Creating an inventory system
    inventory = Inventory()

    # Adding products
    product1 = Product("Laptop", 1000, 50)
    product2 = Product("Smartphone", 500, 100)
    product3 = Product("Headphones", 100, 200)

    inventory.add_product(product1)
    inventory.add_product(product2)
    inventory.add_product(product3)

    # Displaying inventory
    print("Inventory Information:")
    inventory.display_inventory()

    # Updating quantities
    print("\nSelling 10 laptops...")
    product1.update_quantity(10)

    print("\nRestocking 20 smartphones...")
    product2.restock(20)

    # Calculating and displaying total inventory value
    print("\nTotal value of inventory:")
    total_value = inventory.calculate_inventory_value()
    print(f"${total_value:.2f}")

if __name__ == "__main__":
    main()
