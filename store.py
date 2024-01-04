# from pprint import pprint
productList = []
class Product:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount= amount
        
class Order:
    def __init__(self, productName, productAmount):
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


class Customer:
    def __init__(self, name, surename, adress, ):
        self.name = name
        self.surename = surename
        self.adress = adress

    #def CustomerOrders(self):
        #for i in
    
        
productList.append(Product("book", "20.40", 1))
order = Order("book")


for attribute, value in vars(productList[0]).items():
    print(f"{attribute}: {value}")
