from booking import Booking
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.booking_list = {}      # bookingId = booking()


    def add_booking_list(self, booking:Booking):
        self.booking_list[booking.booking_id] = booking

    def remove_booking_list(self, booking:Booking):
        if booking.booking_id in booking.booking_list:
            del self.booking_list[booking.booking_id]
            return True
        return False

    def get_all_bookings(self):
        return self.booking_list