from product import Product

class Cart:
    def __init__(self):
        self.products = {}  #key - product_id, value -  quantity
        self.total_amount = 0

    def add_to_cart(self, product_id, product:Product, quantity ):
        if product_id in self.products:
            self.products[product_id] += quantity

        else:
            self.products[product_id] = quantity
        curr_amount = product.price * quantity
        self.total_amount += curr_amount
        print(f"{product.name} added to cart. new total Amount {self.total_amount}")


    def remove_from_cart_by_quantity(self, product_id, product, quantity):
        if product_id not in self.products:
            raise ValueError("Product not in cart")
        else:
            if self.products[product_id] < quantity:
                raise ValueError("Quantity not available in cart")
            else:
                self.products[product_id] -= quantity
                if self.products[product_id] == 0:
                    del self.products[product_id]
                curr_amount = product.price * quantity
                self.total_amount -= curr_amount

        print(f"{product.name} removed from cart. new total Amount {self.total_amount}")

    def remove_from_cart(self, product_id, product):
        if product_id not in self.products:
            raise ValueError("Product not in cart")
        else:
            quantity = self.products[product_id]
            del self.products[product_id]
            curr_amount = product.price * quantity
            self.total_amount -= curr_amount
        print(f"{product.name} removed from cart. new total Amount {self.total_amount}")


    def check_cart(self):
        if not self.products:
            return False
        return True

    def view_cart(self):
        if not self.check_cart():
            raise ValueError("Cart is empty")
        return self.products
    


 
