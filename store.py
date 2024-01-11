import tkinter as tk
from tkinter import simpledialog

class Product:
    allProducts = []
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount= amount
        Product.allProducts.append(self)

class Customer:
    customers = []

    def __init__(self, first_name, last_name, address, password):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.password = password
        self.orders = []
        Customer.customers.append(self)

    def place_order(self):
        products = []
        while True:
            product_name = simpledialog.askstring("Input", "Enter product name (or 'done' to finish): ")
            if product_name.lower() == 'done':
                break
            price = float(simpledialog.askstring("Input", "Enter product price: "))
            quantity = int(simpledialog.askstring("Input", "Enter product quantity: "))
            product = Product(product_name, price, quantity)
            products.append(product)

        order = Order(products)
        self.orders.append(order)
        print(f"Placed order for {len(order.products)} product(s)")

    def list_orders(self):
        orders_info = f"Orders for {self.first_name} {self.last_name}:\n"
        for i, order in enumerate(self.orders, 1):
            orders_info += f"Order {i}:\n"
            for product in order.products:
                orders_info += f"- {product.name}, price: {product.price}, quantity: {product.quantity}\n"
        return orders_info

    def register_new_customer(self):
        register_window = tk.Tk()
        register_window.title("Register New Customer")

        # Entry widgets for registration information
        tk.Label(register_window, text="First Name:").grid(row=0, column=0)
        tk.Label(register_window, text="Last Name:").grid(row=1, column=0)
        tk.Label(register_window, text="Address:").grid(row=2, column=0)
        tk.Label(register_window, text="Password:").grid(row=3, column=0)

        first_name_entry = tk.Entry(register_window)
        last_name_entry = tk.Entry(register_window)
        address_entry = tk.Entry(register_window)
        password_entry = tk.Entry(register_window, show="*")

        first_name_entry.grid(row=0, column=1)
        last_name_entry.grid(row=1, column=1)
        address_entry.grid(row=2, column=1)
        password_entry.grid(row=3, column=1)

        def register():
            first_name = first_name_entry.get()
            last_name = last_name_entry.get()
            address = address_entry.get()
            password = password_entry.get()

            new_customer = Customer(first_name, last_name, address, password)
            print(f"New user registered: {new_customer.first_name} {new_customer.last_name}")
            register_window.destroy()

        tk.Button(register_window, text="Register", command=register).grid(row=4, column=0, columnspan=2)

        register_window.mainloop()

    def login_or_register(self):
        root = tk.Tk()
        root.withdraw()  # Hide the main window

        login_register_window = tk.Tk()
        login_register_window.title("Login or Register")

        def login():
            login_register_window.destroy()
            return self.login()

        def register():
            login_register_window.destroy()
            return self.register_new_customer()

        tk.Button(login_register_window, text="Login", command=login).grid(row=0, column=0)
        tk.Button(login_register_window, text="Register", command=register).grid(row=0, column=1)

        login_register_window.mainloop()

    def login(self):
        first_name = simpledialog.askstring("Input", "Enter your first name: ")
        last_name = simpledialog.askstring("Input", "Enter your last name: ")
        entered_password = simpledialog.askstring("Input", "Enter password: ")

        for customer in Customer.customers:
            if customer.first_name == first_name and customer.last_name == last_name:
                if customer.password == entered_password:
                    print("Logged in successfully!")
                    return customer
                else:
                    print("Incorrect password. Login failed.")
                    return None
        print("User not found.")
        return None

class Order:
    allOrders = []
    def __init__(self, productName, productAmount):
        for i in Product.allProducts:
            if i.name == productName:
                if i.amount < productAmount:
                    print(f"Nie można zamówić {productAmount}. Ilość dostępnych sztuk: {i.amount}")
                    return
                else:
                    i.amount -= productAmount
                    Order.allOrders.append(self)
                    return
        print(f"Nie mamy takiego produktu jak {productName}")

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Example usage:
    customer1 = Customer("Jan", "Kowalski", "ul. Kwiatowa 5", "a")
    customer2 = Customer("Anna", "Nowak", "ul. Słoneczna 10", "mojehaslo")

    # Login or register a new customer using GUI dialogs
    logged_in_customer = customer1.login_or_register()


if __name__ == "__main__":
    main()
