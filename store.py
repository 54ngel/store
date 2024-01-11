import tkinter as tk

class Product:
    allProducts = []
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount= amount
        Product.allProducts.append(self)
    


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


class Customer:
    allCustomers = []
    def __init__(self, name, surename, adress):
        self.name = name
        self.surename = surename
        self.adress = adress
        Customer.allCustomers.append(self)
        

    def ReturnCustomerList(self):
        return

    #def CustomerOrders(self):
        #for i in 
        
class App(tk.Tk):
    def __init__(self):
        super.__init__()
        self.logInWindow = tk.Tk(); self.logInWindow.geometry("400x300")
        self.nameEntry = tk.Entry(self.logInWindow); self.nameEntry.pack()
        self.surenameEntry = tk.Entry(self.logInWindow); self.surenameEntry.pack()
        self.adressEntry = tk.Entry(self.logInWindow); self.adressEntry.pack()
        
        self.logInButton = tk.Button(self.logInWindow, text="Zaloguj", command= self.onLogInButtonClick())
        self.logInButton.pack()

    def onLogInButtonClick(self):
        Customer(self.nameEntry.get(), self.surenameEntry.get(), self.adressEntry.get())

        
Product("book", "20.40", 1)
Order("book", 1)

# def logIn():
# Customer(nameEntry.get(), surenameEntry.get(), adressEntry.get())
# logInWindow.destroy()
# mainWindow = tk.Tk(); mainWindow.title("Sklep"); mainWindow.geometry("400x300")
# mainWindow.mainloop()
# logInWindow.mainloop()