from theater import Theater
from movie import Movie
from show import Show
from booking import Booking
from user import User

class System:
    def __init__(self):
        self.movies = {}
        self.theaters = {}
        self.users = {}
        self.shows = {}
        self.bookings = {}

    def add_movie(self, movie_id, title, genre, duration):
        if movie_id in self.movies:
            raise ValueError("Movie ID already exists")
        self.movies[movie_id] = Movie(movie_id, title, genre, duration)
        print(f"{title} created")

    def remove_movie(self, movie_id):
        movie = self.movies[movie_id]
        title = movie.title
        if movie_id not in self.movies:
            raise ValueError("Invalid movie ID")
        del self.movies[movie_id]
        print(f"{title} Movie removed")

    def add_theater(self, theater_id, name, location, seating_capacity):
        if theater_id in self.theaters:
            raise ValueError("Theater ID already exists")
        self.theaters[theater_id] = Theater(theater_id, name, location, seating_capacity)
        print(f"{name} theater created")

    def remove_theater(self, theater_id):
        theater = self.theaters[theater_id]
        name = theater.name
        if not theater_id in self.theaters:
            raise ValueError("Invalid theater ID")
        del self.theaters[theater_id]
        print(f"{name} theater removed")

    def add_user(self, user_id, name ):
        if user_id in self.users:
            raise ValueError("User ID already exists")
        user = User(user_id,name)
        self.users[user_id] = user
        print(f"{name} user created")

    def remove_user(self, user_id):
        user = self.users[user_id]
        name = user.name
        if not user_id in self.users:
            raise ValueError("Invalid user ID")
        del self.users[user_id]
        print(f"{name} user removed")
        
    def schedule_show(self, show_id, movie_id, theater_id, show_time, availability=30):
        if show_id in self.shows:
            raise ValueError("Show ID already exists")
        if movie_id not in self.movies:
            raise ValueError("Invalid movie ID")
        if theater_id not in self.theaters:
            raise ValueError("Invalid theater ID")
        
        show = Show(show_id, movie_id, theater_id, show_time, availability)
        self.shows[show_id] = show
        
        # update movie, theater
        movie = self.movies[movie_id]
        theater = self.theaters[theater_id]
        movie.add_show(show_id, show)
        theater.add_show(show_id, show)
        print(f"Show created for {movie.title} movie at {theater.name} theater")


    def book_tickets(self,booking_id, user_id, show_id, seatNumbers):
        booking = None
        # update show - availability and bookingList
        if show_id not in self.shows:
            raise ValueError("Invalid show ID")
        if user_id not in self.users:
            raise ValueError("Invalid user ID")
        
        show = self.shows[show_id] 
        if show.check_seats_available(seatNumbers):
            booking = Booking(booking_id, user_id, show_id, seatNumbers)
            self.bookings[booking_id] = booking
            show.add_booking_list(booking)
             # update user
            user = self.users[user_id] 
            user.add_booking_list(booking)
            print(f"Booking successfull")
        else:
            raise ValueError("Seats not available")
        

    def cancel_booking(self, booking_id):
        if booking_id not in self.bookings:
            raise ValueError("invalid booking ID")
        del self.bookings[booking_id]
        print(f"Booking {booking_id} cancelled")

    def list_all_movies(self):
        for movie_id, movie in self.movies.items():
            print(f"{movie_id} - {movie.title}")

    def list_all_theaters(self):
        for theater_id, theater in self.theaters.items():
            print(f"{theater_id} - {theater.name}")

    def list_all_shows_by_movieid(self, movie_id):
        if not movie_id in self.movies:
            raise ValueError("Invalid movie ID")
        movie = self.movies[movie_id]
        movieList = movie.get_all_shows()
        for show_id, show in movieList.items():
            print(f"{show_id} showid - {self.movies[show.movie_id].title} movie")

    

    def list_all_shows_by_theaterid(self, theater_id):
        if not theater_id in self.theaters:
            raise ValueError("Invalid theater ID")
        theater = self.theaters[theater_id]
        showlist = theater.get_all_shows()
        for show_id, show in showlist.items():
            print(f"{show_id} showid - {self.theaters[show.theater_id].name} movie")

    def list_all_bookings_for_show(self, show_id):
        if not show_id in self.shows:
            raise ValueError("Invalid show ID")
        show = self.shows[show_id]
        bookingList = show.get_all_bookings()
        for booking_id, booking in bookingList.items():
            print(f"{booking_id} booking_id - {self.bookings[booking_id].seatNumbers} seatNumbers - {self.bookings[booking_id].booking_time} booking_time")


    def list_all_bookings_for_user(self, user_id):
        if not user_id in self.users:
            raise ValueError("Invalid user ID")
        user = self.users[user_id]
        bookingList = user.get_all_bookings()
        for booking_id, booking in bookingList.items():
            print(f"{booking_id} booking_id - {self.bookings[booking_id].seatNumbers} seatNumbers - {self.bookings[booking_id].booking_time} booking_time")
       
