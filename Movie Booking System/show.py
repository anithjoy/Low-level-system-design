from booking import Booking
class Show:
    def __init__(self, show_id, movie_id, theater_id, show_time,availability=30):
        self.show_id = show_id
        self.movie_id = movie_id
        self.theater_id = theater_id
        self.show_time = show_time
        self.availability = availability
        self.booking_list = {}      # bookingId = booking()



    def check_seats_available(self, seatNumbers):
        if self.availability - seatNumbers >= 0:
            return True
        return False
    
    def add_booking_list(self, booking:Booking):
        self.booking_list[booking.booking_id] = booking

    def remove_booking_list(self, booking:Booking):
        if booking.booking_id in booking.booking_list:
            del self.booking_list[booking.booking_id]
            return True
        return False

    def get_all_bookings(self):
        return self.booking_list



