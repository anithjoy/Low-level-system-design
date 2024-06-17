class Product:
    def __init__(self,product_id, name, description, price):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price


    def change_name(self, name):
        if self.name == name:
            raise ValueError("Name is already set to {}".format(name))
        old_name = name
        self.name = name
        print(f"Your name {old_name} changed to {self.name}")


    def change_price(self, price):
        if self.price == price:
            raise ValueError("Price is already set to {}".format(price))
        old_price = price
        self.price = price
        print(f"Your price {old_price} changed to {self.price}")