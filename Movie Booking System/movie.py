from show import Show

class Movie:
    def __init__(self, movie_id, title, genre, duration):
        self.movie_id = movie_id
        self.title = title
        self.genre = genre
        self.duration = duration
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