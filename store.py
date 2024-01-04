class Product:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount= amount
        
class Order:
    def __init__(self, productName, productAmount):
        
        