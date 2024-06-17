## Online Shopping Cart System

Design an Online Shopping Cart System to manage users, products, and their shopping carts. The system should be able to handle the following functionalities:

### User Management

- Register a new user.
- Remove a user.
- List all registered users.

### Product Management

- Add a new product.
- Remove a product.
- List all products.

### Cart Management

- Add a product to a user's cart.
- Remove a product from a user's cart.
- View the contents of a user's cart.

### Order Management

- Create an order from a user's cart.
- List all orders for a user.

### Key Entities

- **User:** Represents a user with attributes like user ID, name, and email.
- **Product:** Represents a product with attributes like product ID, name, description, and price.
- **Cart:** Represents a shopping cart associated with a user, containing products and their quantities.
- **Order:** Represents an order created from the contents of a user's cart with attributes like order ID, user, list of products, total amount, and order status.

### Requirements

#### Register a User

- **Inputs:** User ID, Name, Email
- **Outputs:** Confirmation of user registration

#### Remove a User

- **Inputs:** User ID
- **Outputs:** Confirmation of user removal

#### Add a Product

- **Inputs:** Product ID, Name, Description, Price
- **Outputs:** Confirmation of product addition

#### Remove a Product

- **Inputs:** Product ID
- **Outputs:** Confirmation of product removal

#### Add Product to Cart

- **Inputs:** User ID, Product ID, Quantity
- **Outputs:** Confirmation of product addition to cart

#### Remove Product from Cart

- **Inputs:** User ID, Product ID
- **Outputs:** Confirmation of product removal from cart

#### View Cart

- **Inputs:** User ID
- **Outputs:** List of products in the user's cart with their quantities

#### Create Order

- **Inputs:** User ID
- **Outputs:** Confirmation of order creation and order details

#### List User Orders

- **Inputs:** User ID
- **Outputs:** List of orders for the user

### Design Considerations

- Use object-oriented principles to design the system.
- Ensure data consistency and integrity.
- Consider scalability and potential future extensions of the system.

Design the classes, attributes, and methods that you would use to implement this Online Shopping Cart System. Consider how the different entities interact with each other and ensure the system meets the specified requirements.
