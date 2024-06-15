from show import Show

class Theater:
    def __init__(self, theater_id, name, location, seating_capacity=30):
        self.theater_id = theater_id
        self.name = name
        self.location = location
        self.seating_capacity = seating_capacity
        self.show_list = {}      # showId = show()


    def add_show(self, show_id, show:Show):
        self.show_list[show_id] = show
        return True
    
    def remove_show(self, show_id):
        if show_id not in self.show_list:
            return False
        del self.show_list[show_id]
        return True
    
    def get_all_shows(self):
        return self.show_list