# Description: This file contains the Room class which is used to create room objects. The Room class has the following attributes:

class Room:
    def __init__(self, r_id, type, amenities, status="available"):
        if type.lower() not in ['single', 'double', 'suite']:
            raise ValueError('Invalid room type.')
        # if status.lower() not in ['available', 'booked', 'under maintenance']:
        #     raise ValueError('Invalid room status type.')
        # if not type(amenities) == type([]):
        #     raise ValueError('Invalid amenities type.')
        
        self.r_id = r_id
        self.type = type
        self.status = status
        self.amenities = amenities



    # add change amenities, status, type
    def updateRoom(self,status):
        if status.lower() not in ['available', 'booked', 'under maintenance']:
            raise ValueError('Invalid room status type.')
        
        self.status = status