from cart import Cart
from order import Order
import uuid

class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.orders = []
        self.cart = Cart()

    def add_to_cart(self, product_id, product, quantity):
        self.cart.add_to_cart(product_id, product, quantity)

    def remove_from_cart_by_quantity(self, product_id, product, quantity):
        self.cart.remove_from_cart_by_quantity(product_id, product, quantity)

    def remove_from_cart(self, product_id,product):
        self.cart.remove_from_cart(product_id, product)

    def view_cart(self):
        return self.cart.view_cart()
    
    def create_order(self):
        if not self.cart.check_cart():
            raise ValueError("Cart is empty")
        order_id = uuid.uuid4()
        # print(self.user_id)
        order = Order(order_id, self.user_id, self.cart.products,self.cart.total_amount)
        total_amount = self.cart.total_amount
        order.change_order_status()
        self.orders.append(order)
        self.cart = Cart()
        print("order created successfully")
        print(f"order id- {order.order_id}")
        for pId, quant in order.list_products:
            print(f"Product {pId}, Quantity {quant}")

        print(f"total_amount {total_amount}")


    def get_all_orders(self):
        if not self.orders:
            raise ValueError("No orders found")
        counter = 1
        for order in self.orders:
            print(f"order {counter} - \t amount:{order.total_amount}")
            counter += 1

        
            
