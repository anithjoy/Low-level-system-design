from onlineBookingSystem import System

if __name__ == '__main__':
    system = System()
    
    # Register users
    system.register_user("u1", "John Doe", "john@example.com")
    system.register_user("u2", "Jane Doe", "jane@example.com")

    # Add products
    system.add_product("p1", "Laptop", "High performance laptop", 1200)
    system.add_product("p2", "Smartphone", "Latest model smartphone", 800)

    # Add products to cart
    system.add_to_cart("u1", "p1", 1)
    system.add_to_cart("u1", "p2", 2)

     # View cart
    (system.view_cart("u1"))

    # Create order
    system.create_order("u1")

    # List user orders
    system.list_user_orders("u1")

    # Remove product from cart
    system.add_to_cart("u2", "p1", 1)
    system.remove_from_cart_by_quantity("u2", "p1", 1)

    # List all products
    system.list_all_products()