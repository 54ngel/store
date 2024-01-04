# from pprint import pprint
productList = []
class Product:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount= amount
        productList.append(self.__class__)
        
class Order:
    def __init__(self, productName, productAmount):
        pass

class Customer:
    def __init__(self, name, surename, adress, ):
        self.name = name
        self.surename = surename
        self.adress = adress

    #def CustomerOrders(self):
        #for i in
    def __init__(self, productName, productAmount, customer):
        for i in productList:
            if i.name == productName:
                if i.amount < productAmount:
                    print(f"Nie można zamówić {productAmount}. Ilość dostępnych sztuk: {i.amount}")
                    return
                else:
                    i.amount -= productAmount
                    customer.orders.append(self.__class__)
                    return
        print(f"Nie mamy takiego produktu jak {productName}")
        
product = Product("book", "20.40", 1)
order = Order("book")


for attribute, value in vars(product).items():
    print(f"{attribute}: {value}")
