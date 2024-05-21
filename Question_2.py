#Task 1

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_product(self):
        print(f"Name: {self.name}\nProduct ID: {self.product_id}\nPrice: {self.price:.2f}")


#Task 2

class Book(Product):
    def __init__(self, product_id, name, price, author):
        super().__init__(product_id, name, price)
        self.author = author
    
    def display_product(self):
        print(f"Title: {self.name}\nProduct ID: {self.product_id}\nAuthor: {self.author}\nPrice: {self.price:.2f}")

class Electronic(Product):
    def __init__(self, product_id, name, price, storage):
        super().__init__(product_id, name, price)
        self.storage = storage
    
    def display_product(self):
        print(f"Device: {self.name}\nProduct ID: {self.product_id}\nStorage: {self.storage} GB\nPrice: {self.price:.2f}")


class Clothing(Product):
    def __init__(self, product_id, name, price, size):
        super().__init__(product_id, name, price)
        self.size = size

    def display_product(self):
        print(f"Item: {self.name}\nProduct ID: {self.product_id}\nSize: {self.size}\nPrice: {self.price:.2f}")

phone = Product('123ABC', "iPhone", 100)

book = Book('ADFAS55', 'Red Rising', 25.99, 'Pierce Brown')

tv = Electronic('456SDSAF', 'LG 60 in. Flatscreen', 200, 100)

shirt = Clothing('4ASD5AWE', 'Gucci Shirt', 500, 'Large')

phone.display_product()
    #output:
    # Name: iPhone
    # Product ID: 123ABC
    # Price: 100.00

book.display_product()
    #output:
    # Title: Red Rising
    # Product ID: ADFAS55
    # Author: Pierce Brown
    # Price: 25.99

tv.display_product()
    #output:
    # Device: LG 60 in. Flatscreen
    # Product ID: 456SDSAF
    # Storage: 100 GB
    # Price: 200.00

shirt.display_product()
    #output:
    # Item: Gucci Shirt
    # Product ID: 4ASD5AWE
    # Size: Large
    # Price: 500.00