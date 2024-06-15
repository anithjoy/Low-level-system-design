from system import System
if __name__ == "__main__":
    
    system = System()

    # add movies 
    system.add_movie("m1", "Inception", "Sci-Fi", 148)
    system.add_movie("m2", "The Matrix", "Sci-Fi", 136)

    # Add theater
    system.add_theater("t1", "Regal Cinema", "Downtown", 200)
    system.add_theater("t2", "AMC", "Uptown", 150)

    # Add Shows
    system.schedule_show("s1", "m1", "t1", "2023-06-15 18:00")
    system.schedule_show("s2", "m2", "t2", "2023-06-16 20:00")

    # Add Users
    system.add_user("u1", "Alice")
    system.add_user("u2", "Bob")

    # Book tickets
    system.book_tickets("b1", "u1", "s1", 2)
    system.book_tickets("b2", "u2", "s2", 3)

     # List all movies
    (system.list_all_movies())

    # List all theaters
    (system.list_all_theaters())

    # List all movies
    (system.list_all_movies())

     # List all theater
    (system.list_all_theaters())

    # List shows by movie
    (system.list_all_shows_by_movieid("m1"))

    # List shows by theater
    (system.list_all_shows_by_theaterid("t1"))

    # List bookings by show
    (system.list_all_bookings_for_show("s1"))

    # List bookings by user
    (system.list_all_bookings_for_user("u1"))

    # Cancel booking
    system.cancel_booking("b1")

    