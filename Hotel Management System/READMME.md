# Hotel Management System

## Problem Statement

Design a low-level system for managing hotel operations, focusing on the following core components:

### Guest Management

- Each guest has a unique ID, name, contact information, and booking history.
- Guests can book rooms.
- Guests can view their current and past bookings.

### Room Management

- Each room has a unique room number, type (e.g., single, double, suite), and status (e.g., available, booked, under maintenance).
- Rooms can be booked by guests.
- Rooms can have a list of amenities (e.g., Wi-Fi, TV, minibar).

### Booking Management

- Each booking has a unique booking ID, guest, room, check-in date, check-out date, and booking status (e.g., confirmed, checked-in, checked-out, canceled).
- Bookings can be created, updated, and canceled.

### Hotel Administration

- Ability to add/remove guests.
- Ability to add/remove rooms.
- Ability to update room status.
- Ability to view all current and past bookings.

## Requirements

### Classes and Attributes

- Define classes for `Guest`, `Room`, `Booking`, and `Hotel`.
- Each class should have appropriate attributes to store the required information.

### Methods

- Methods for guests to book rooms.
- Methods for updating booking status.
- Methods for adding/removing guests and rooms.
- Methods for viewing current and past bookings for a guest.
- Methods for updating room status and viewing room details.
- Methods for viewing all bookings.

### Relationships

- A guest can have multiple bookings.
- A room can be booked by multiple guests over time.
- A booking is associated with one guest and one room.

### Constraints

- Ensure that a room cannot be double-booked for overlapping dates.
- Ensure that only available rooms can be booked.
- Ensure that bookings can be updated or canceled based on their current status.

## Example Scenarios

### Adding a Guest

- Create a new guest with a unique ID, name, and contact information.
- Add the guest to the hotel system.

### Booking a Room

- Book a room for a guest for a specific date range.
- Check room availability and update room status accordingly.

### Updating Booking Status

- Update a booking status to checked-in, checked-out, or canceled.
- Ensure that room status is updated based on booking status.

### Viewing Bookings

- Allow a guest to view their current and past bookings.
- Allow hotel administration to view all bookings.

## Implementation

Design and implement the classes and methods needed to fulfill the requirements outlined above. Ensure that your code is modular, maintainable, and adheres to object-oriented principles.
