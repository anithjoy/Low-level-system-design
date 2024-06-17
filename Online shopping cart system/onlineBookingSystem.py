from user import User
from product import Product
class System:
    def __init__(self) -> None:
        self.users = {}
        self.products = {}


    def register_user(self, user_id, name, email):
        if user_id in self.users:
            raise ValueError("User already registered")
        user = User(user_id, name, email)
        self.users[user_id] = user
        print(f"User created {user.name}")

    def remove_user(self, user_id):
        if not user_id in self.users:
            raise ValueError("User not registered")
        
        del self.users[user_id]
        print(f"User removed {user_id}")

    def add_product(self, product_id, name, description, price):
        if product_id in self.products:
            raise ValueError("Product already registered")
        self.products[product_id] = Product(product_id, name, description, price)
        print(f"Product added {name}")

    def remove_product(self, product_id):
        if product_id not in self.products:
            raise ValueError("Product not found")
        product = self.products[product_id]
        del self.products[product_id]
        for user in self.users:
            if product_id in user.cart.products:
                user.remove_from_cart(product_id, product)

        print(f"{product_id} Product removed successfully from the entrire system")

    def add_to_cart(self, user_id, product_id, quantity):
        if not user_id in self.users:
            raise ValueError("User not registered")
        if not product_id in self.products:
            raise ValueError("Product not found")
        if quantity < 1:
            raise ValueError("Quantity should be greater than 0")
        
        user = self.users[user_id]
        product = self.products[product_id]

        user.add_to_cart(product_id,product, quantity)

    def remove_from_cart_by_quantity(self, user_id, product_id, quantity):
        if not user_id in self.users:
            raise ValueError("User not registered")
        if not product_id in self.products:
            raise ValueError("Product not found")
        if quantity < 1:
            raise ValueError("Quantity should be greater than 0")
        
        user = self.users[user_id]
        product = self.products[product_id]

        user.remove_from_cart_by_quantity(product_id,product, quantity)

    def remove_from_cart(self, user_id, product_id):
        if not user_id in self.users:
            raise ValueError("User not registered")
        if not product_id in self.products:
            raise ValueError("Product not found")
        
        user = self.users[user_id]
        product = self.products[product_id]

        user.remove_from_cart(product_id, product)


    def view_cart(self, user_id):
        if not user_id in self.users:
            raise ValueError("User not registered")
        
        user = self.users[user_id]
        res = user.view_cart()
        for pId,quantity in res.items():
            product = self.products[pId]
            print(f"Product: {product.name} \t Quantity: {quantity}")



    def create_order(self, user_id):
        if not user_id in self.users:
            raise ValueError("User not registered")
        
        user = self.users[user_id]
        user.create_order()

    def list_user_orders(self, user_id):
        if not user_id in self.users:
            raise ValueError("User not registered")
        
        user = self.users[user_id]
        user.get_all_orders()
    
    def list_all_products(self):
        for pId, product in self.products.items():
            print(f"product Id - {pId}, name - {product.name}, price - {product.price}")