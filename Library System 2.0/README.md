# Library Management System 2.0

## Problem Statement

### Design a Library Management System to manage the books in a library and the interactions with the library members. The system should be able to handle the following functionalities:

#### Books Management:

Add new books to the library.
Remove books from the library.
Search for books by title, author, or ISBN.
Keep track of the number of copies of each book.

#### Member Management:

Register new members.
Remove members.
Search for members by name or member ID.
Keep track of the books borrowed by each member.

#### Borrowing and Returning Books:

Allow members to borrow available books.
Allow members to return books.

#### System Constraints:

Ensure that a member cannot borrow more than a certain number of books at a time.
Ensure that a member cannot borrow the same book more than once.
Key Entities

**Book:** Represents a book in the library with attributes like title, author, ISBN, and number of copies.
**Member:** Represents a library member with attributes like name, member ID, and borrowed books.
**Library:** Manages the collection of books and members, and handles borrowing and returning books.

#### Requirements

**Add a Book:**
Inputs: Title, Author, ISBN, Number of Copies
Outputs: Confirmation of book addition

**Remove a Book:**
Inputs: ISBN
Outputs: Confirmation of book removal

**Search for a Book:**
Inputs: Title or Author or ISBN
Outputs: List of books matching the search criteria

**Register a Member:**
Inputs: Name, Member ID
Outputs: Confirmation of member registration

**Remove a Member:**
Inputs: Member ID
Outputs: Confirmation of member removal

**Borrow a Book:**
Inputs: Member ID, ISBN
Outputs: Confirmation of book borrowing or error message if not available

**Return a Book:**
Inputs: Member ID, ISBN
Outputs: Confirmation of book return or penalty for late return

**Design Considerations**
Use object-oriented principles to design the system.
Ensure data consistency and integrity.
Think about scalability and potential future extensions of the system.

**_Design the classes, attributes, and methods that you would use to implement this Library Management System. Consider how the different entities interact with each other and ensure the system meets the specified requirements._**
