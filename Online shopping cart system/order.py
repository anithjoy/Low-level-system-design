
class Order:
    def __init__(self, order_id, user_id, list_products, total_amount):
        self.order_id = order_id
        self.user = user_id
        self.list_products = list_products
        self.total_amount = total_amount
        self.order_status = False


    def change_order_status(self):
        self.order_status = not self.order_status
        if self.order_status:
            print("Order is confirmed")
        else:
            print("Order is cancelled")
        