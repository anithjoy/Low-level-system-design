from admin import Admin



if __name__ == '__main__':
    hotel = Admin("Dwarka Hotel")
    print(hotel)

    # Create and add Guests
    guest1 = hotel.add_guest("G1", "Alice", "alice@example.com")
    guest2 = hotel.add_guest("G2", "Bob", "bob@example.com")
    print(guest1,guest2)

     # Create and add Rooms
    room1 = hotel.add_room("101", "Single", ["Wi-Fi", "TV"])
    room2 = hotel.add_room("102", "Double", ["Wi-Fi", "TV", "Minibar"])

    # Create Bookings
    hotel.create_booking("B1", "G1", "101", "2024-06-15", "2024-06-20")
    hotel.create_booking("B2", "G2", "102", "2024-06-18", "2024-06-22")


    # Update Booking Status
    hotel.update_booking_status("B1", "checked-in")
    hotel.update_booking_status("B1", "checked-out")

    #  need work
    # # View Guest Bookings
    # hotel.view_guest_booking("G1")
    # hotel.view_guest_booking("G2")

    # # View All Bookings
    # hotel.view_all_bookings()
    