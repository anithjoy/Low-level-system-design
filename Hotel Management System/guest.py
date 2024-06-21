# Description: Guest class to store guest details and bookings. The Guest class has the following attributes:
class Guest:
    def __init__(self, g_id, name, email):
        self.g_id = g_id
        self.name = name
        self.email = email
        self.bookings = {}   # key - booking_id, value - booking obj

    def __str__(self):
        return f"Guest {self.name} created successfully"


    def view_booking(self):
        print(self.bookings)
        
        for bId, booking in self.bookings:
            print(f"bid - {bId}, booking-room {booking}")
        