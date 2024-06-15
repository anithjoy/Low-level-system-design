from datetime import datetime

class Booking:
    def __init__(self, booking_id, user_id, show_id, seatNumbers=1):
        self.booking_id = booking_id
        self.user_id = user_id
        self.show_id = show_id
        self.seatNumbers = seatNumbers
        self.booking_time = datetime.now()

        
