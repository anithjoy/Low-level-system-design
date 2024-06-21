# Description: This file contains the class definition for the Booking class. The Booking class is used to create booking objects. The booking object contains the following attributes:

class Booking:
    def __init__(self, b_id, guest, room, check_in, check_out, bookingStatus):
        if not bookingStatus.lower() in ["confirmed", "checked-in", "checked-out", "canceled"]:
            raise ValueError("Booking staus invalid")
        
        self.b_id = b_id
        self.guest = guest
        self.room = room
        self.check_in = check_in
        self.check_out = check_out
        self.bookingStatus = bookingStatus


    def cancel_booking(self, bookingStatus):
        if not bookingStatus.lower() in ["canceled"]:
            raise ValueError("Booking staus invalid")
        
        self.bookingStatus = bookingStatus


    def change_booking_status(self, bookingStatus):
        if not bookingStatus.lower() in ["confirmed", "checked-in", "checked-out"]:
            raise ValueError("Booking staus invalid")
        
        self.bookingStatus = bookingStatus

