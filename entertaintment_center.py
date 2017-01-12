import Media
import fresh_tomatoes


# creating instances
# Movie takes- Media.Movie(movie_title, Image_url, trailer_url)

pursuit_of_happyness = Media.Movie("The Pursuit of Happyness",
                                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ5NjQ0NDI3NF5BMl5BanBnXkFtZTcwNDI0MjEzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg",  # NOQA
                                   "https://www.youtube.com/watch?v=89Kq8SDyvfg&t=71s")  # NOQA

forest_gump = Media.Movie("Forrest Gump",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BYThjM2MwZGMtMzg3Ny00NGRkLWE4M2EtYTBiNWMzOTY0YTI4XkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_UY268_CR10,0,182,268_AL_.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=uPIEn0M8su0")  # NOQA

predestination = Media.Movie("Predestination",
                             "https://images-na.ssl-images-amazon.com/images/M/MV5BMTAzODc3NjU1NzNeQTJeQWpwZ15BbWU4MDk5NTQ4NTMx._V1_UX182_CR0,0,182,268_AL_.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=-FcK_UiVV40")  # NOQA

up = Media.Movie("UP",
                 "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk3NDE2NzI4NF5BMl5BanBnXkFtZTgwNzE1MzEyMTE@._V1_UX182_CR0,0,182,268_AL_.jpg",  # NOQA
                 "https://www.youtube.com/watch?v=pkqzFUhGPJg")  # NOQA


prestige = Media.Movie("The Prestige",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA4NDI0MTIxNF5BMl5BanBnXkFtZTYwNTM0MzY2._V1_UX182_CR0,0,182,268_AL_.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=o4gHCmTQDVI")  # NOQA

notebook = Media.Movie("The Notebook",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk3OTM5Njg5M15BMl5BanBnXkFtZTYwMzA0ODI3._V1_UX182_CR0,0,182,268_AL_.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=FC6biTjEyZw")  # NOQA


# creating movies list
movies_list = [pursuit_of_happyness, forest_gump,
               predestination, up, prestige, notebook]


# creating webpage with fresh_tomatoes

fresh_tomatoes.open_movies_page(movies_list)
