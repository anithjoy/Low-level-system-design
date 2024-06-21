from guest import Guest
from room import Room
from booking import Booking

class Admin:
    def __init__(self, name):
        self.name = name
        self.guests ={}
        self.booking = {}
        self.rooms = {}

    def __str__(self):
        return f"Hotel {self.name} created successfully"
    # Guest
    def add_guest (self, g_id, name, email):
        if g_id in self.guests:
            raise ValueError("Guest already exists")
        self.guests[g_id] = Guest(g_id, name, email) 
        return self.guests[g_id]

    def remove_guest (self, g_id):
        if g_id not in self.guests:
            raise ValueError("Guest does not exist")
        
        del self.guests[g_id]


    # Room
    def add_room(self, r_id, type, amenties,status="available"):
        if r_id  in self.rooms:
            raise ValueError("Room already exists")
        
        self.rooms[r_id] = Room(r_id, type, status, amenties)
        return self.rooms[r_id]

    def remove_room(self, r_id):
        if r_id not in self.rooms:
            raise ValueError("Room does not exist")
        
        del self.rooms[r_id]

    #  booking
    def create_booking(self, b_id, g_id, r_id, check_in, check_out, bookingStatus="confirmed"):
        if b_id in self.booking:
            raise ValueError("Booking already exists")
        if g_id not in self.guests:
            raise ValueError("Guest does not exist")
        if r_id not in self.rooms:
            raise ValueError("Room does not exist")
        
        guest = self.guests[g_id]
        room = self.rooms[r_id]
        self.booking[b_id] = Booking(b_id, g_id, r_id, check_in, check_out, bookingStatus)

        guest.bookings[b_id] = {
            "room": r_id,
            "booking": b_id,
            "check_in": check_in,
            "check_out": check_out,
            "bookingStatus": bookingStatus
        }

        room.status = "booked"
        print(f"Room{r_id} is booked for guest {g_id}")

    def update_booking_status(self, b_id, bookingStatus):
        if b_id not in self.booking:
            raise ValueError("Booking does not exist")
        
        booking = self.booking[b_id]
        booking.change_booking_status(bookingStatus)
        print(f"Booking status of {b_id} updated to {bookingStatus}")

    #  this function doesnt work well. I have to work on this in future
    def view_guest_booking(self, g_id):
        if g_id not in self.guests:
            raise ValueError("Guest does not exist")
        
        guest = self.guests[g_id]
        guest.view_booking()

    def view_all_bookings(self):
        for b_id, booking in self.booking:

            print(f"bid - {b_id}, booking-room {booking}")
