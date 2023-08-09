#creat #product class,
#each product has name, ctogary, and price ---> instance variable
#clss is able to return a discription of product --> method
#for each product be able to compute discount of givin amount
#(compute price aftr discount of amount%)


class Product:
    def __init__(self, name, category, price):
        self.productName = name
        self.category = category
        self.price = price
    
    def descripe(self):
        return f"Product Name: {self.productName} is {self.category} cost {self.price} Omani Riyals"
        
    def discount(self, amount):
        self.price = self.price - self.price * (amount/100)
        if self.category == 'Electronics':
            self.price += 10
    def getName(self):
        return self.productName
    def getCategory(self):
        return self.category
    def getPrice(self):
        return self.price