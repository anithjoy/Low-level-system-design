# Movie Booking System

## Problem Statement

Design a Movie Booking System to manage the booking of movie tickets. The system should be able to handle the following functionalities:

### Movies Management:

- Add new movies to the system.
- Remove movies from the system.
- List all movies currently available.

### Theater Management:

- Add new theaters.
- Remove theaters.
- List all theaters.

### Show Management:

- Schedule a show for a movie in a theater.
- List all shows for a particular movie.
- List all shows for a particular theater.

### Booking Management:

- Book tickets for a show.
- Cancel tickets for a show.
- List all bookings for a particular show.
- List all bookings for a particular user.

## Key Entities

- **Movie**: Represents a movie with attributes like title, genre, duration, etc.
- **Theater**: Represents a theater with attributes like name, location, and seating capacity.
- **Show**: Represents a scheduled show of a movie in a theater with attributes like show time and available seats.
- **Booking**: Represents a booking with attributes like user details, show details, and number of seats booked.
- **User**: Represents a user who can book tickets with attributes like name and user ID.

## Requirements

### Add a Movie:

- **Inputs**: Title, Genre, Duration
- **Outputs**: Confirmation of movie addition

### Remove a Movie:

- **Inputs**: Movie ID
- **Outputs**: Confirmation of movie removal

### Add a Theater:

- **Inputs**: Name, Location, Seating Capacity
- **Outputs**: Confirmation of theater addition

### Remove a Theater:

- **Inputs**: Theater ID
- **Outputs**: Confirmation of theater removal

### Schedule a Show:

- **Inputs**: Movie ID, Theater ID, Show Time
- **Outputs**: Confirmation of show scheduling

### Book Tickets:

- **Inputs**: User ID, Show ID, Number of Seats
- **Outputs**: Confirmation of booking or error message if not available

### Cancel Tickets:

- **Inputs**: Booking ID
- **Outputs**: Confirmation of booking cancellation

### List All Movies:

- **Inputs**: None
- **Outputs**: List of all movies

### List All Theaters:

- **Inputs**: None
- **Outputs**: List of all theaters

### List All Shows for a Movie:

- **Inputs**: Movie ID
- **Outputs**: List of shows for the movie

### List All Shows for a Theater:

- **Inputs**: Theater ID
- **Outputs**: List of shows for the theater

### List All Bookings for a Show:

- **Inputs**: Show ID
- **Outputs**: List of bookings for the show

### List All Bookings for a User:

- **Inputs**: User ID
- **Outputs**: List of bookings for the user

## Design Considerations

- Use object-oriented principles to design the system.
- Ensure data consistency and integrity.
- Consider scalability and potential future extensions of the system.

## Design

Design the classes, attributes, and methods that you would use to implement this Movie Booking System. Consider how the different entities interact with each other and ensure the system meets the specified requirements.
